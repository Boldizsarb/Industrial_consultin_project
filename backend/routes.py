from flask import request, jsonify, make_response
import bcrypt
from database import *
import jwt
from email_sending import send_verification_email, send_password_reset_email
import traceback
import sys
import hashlib
import carApi
import bus_api
import train_api


JWT_SECRETS = os.getenv('JWT_SECRET')
def configure_routes(app, mail):

    @app.route('/signup', methods=['POST', 'OPTIONS'])
    def signup():
        if request.method == 'OPTIONS':
            response = make_response(jsonify({'status': 'OK'}), 200)
            response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8081'
            response.headers['Access-Control-Allow-Methods'] = 'POST'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
            return _build_cors_preflight_response()
        try:
            data = request.get_json()
            print("Received data:", data)
            first_name = data.get('firstName')
            last_name = data.get('lastName')
            email = data.get('email')
            phone_number = data.get('phoneNumber')
            password = data.get('password')

            if not all([first_name, last_name, email, phone_number, password]):
                return jsonify({'error': 'All fields must be filled'}), 400
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            verification_token = generate_jwt_token(email)
             
            print("Verification token generated:", verification_token)
            if verification_token is None:
                print("Failed to generate verification token")
                return jsonify({'error': 'Failed to generate verification token'}), 500

            store_user_result = store_user_in_database(first_name, last_name, email, phone_number, hashed_password, verification_token)
            if isinstance(store_user_result, tuple):
                # Unpacking for clarity
                error_message, status_code = store_user_result
                print(f"Error storing user: {error_message}")
                return jsonify({'error': error_message}), status_code

            email_sent = send_verification_email(email, verification_token, mail, app)
            if email_sent: 
                return jsonify({'success': f'User created successfully. Please check your inbox or spam folder for a verification email'}), 201
            return jsonify({'message': 'User created successfully, verification email sent', 'token': verification_token}), 201
        except Exception as e:
            error_traceback = traceback.format_exc()
            logger.exception(f"Exception in signup: {e}\n{error_traceback}")
            return jsonify({
                'error': 'Failed to signup',
                'message': str(e),
                'traceback': error_traceback
            }), 500
    
    
    @app.route('/login', methods=['POST', 'OPTIONS'])
    def login():
        print("Received login request", file=sys.stderr)
        if request.method == 'OPTIONS':
            response = make_response(jsonify({'status': 'OK'}), 200)
            response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8081'
            response.headers['Access-Control-Allow-Methods'] = 'POST'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
            return _build_cors_preflight_response()

        try:
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')

            # Logging for debugging purposes
            print(f"Received login request for user: {email}", file=sys.stderr)
            print(f"Received login request for user: {password}", file=sys.stderr)
            print(f"Received login request for user: {data}", file=sys.stderr)

            if not all([email, password]):
                return jsonify({'error': 'All fields must be filled'}), 400

            stored_password_hash = verify_password(email)
            token = hashlib.sha256(email.encode()).hexdigest()
            # Retrieve user data from the database using the email
            user_data = get_user_data_by_email(email)
            if not user_data:
                return jsonify({'error': 'User not found'}), 404
            # Extract the user's first name
            print("Checking:",user_data, file=sys.stderr)
            firstname = user_data.get('first_name')
            print("Checking:",firstname, file=sys.stderr)
            print(f"Received login request for user: {token}", file=sys.stderr)
            # Generate token with expiration
            session_token = generate_token(firstname, email, JWT_SECRET)
            print("Try:",session_token, file=sys.stderr)
            store_sesssion_token(session_token, email)
            if stored_password_hash:
                password_hash = hashlib.sha256(password.encode()).hexdigest()
                print(f"Received login request for user: {password_hash}", file=sys.stderr)

                if password_hash == stored_password_hash:
                    return jsonify({'Success': 'Logged in', 'token' : session_token }), 200
                else:
                    return jsonify({'error': 'Invalid email or password'}), 401

            stored_password_hash = verify_password(email)

            if stored_password_hash:
                password_hash = hashlib.sha256(password.encode()).hexdigest()
                print(f"Received login request for user: {password_hash}", file=sys.stderr)

                if password_hash == stored_password_hash:
                    return jsonify({'Success': 'Logged in', 'token': session_token}), 200
                else:
                    return jsonify({'error': 'Invalid email or password'}), 401
            
        except Exception as e:
            logger.exception(f"Exception in login: {e}")
            return jsonify({'error': 'Failed to login'}), 500

        
    @app.route('/verify-token', methods=['POST'])
    def verify_token():
        # Get the token from the request headers
        token = request.headers.get('Authorization')

        if token:
            try:
                # Retrieve the stored token for the user from the database or storage
                stored_token = get_stored_token(token)
                print(f"my stored_tcoken {stored_token}",file=sys.stderr)
                print(f"my tcoken{token}", file=sys.stderr)
                if token == stored_token:
                    # Token is valid
                    return jsonify({'status': 'valid'})
                else:
                    # Token is invalid
                    return jsonify({'status': 'invalid'})
            except jwt.ExpiredSignatureError:
                return jsonify({'status': 'expired'})
            except jwt.InvalidTokenError:
                return jsonify({'status': 'invalid'})
        else:
            return jsonify({'status': 'missing'})


    @app.route('/logout', methods=['POST'])
    def logout():
        try:
            # Get the token from the request headers
            token_header = request.headers.get('Authorization')
            if not token_header:
                return jsonify({'error': 'Missing token'}), 401
            
            token = token_header.split(' ')[1]
            # Decode the token to extract the email
            decoded_token = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            email = decoded_token.get('email')
            if not email:
                return jsonify({'error': 'Missing email in token'}), 401

            # Remove the token from the database
            if remove_stored_token(email):
                # Create a response object and clear the cookie
                response = make_response(jsonify({'status': 'success'}))
                response.set_cookie('token', '', expires=0, path='/')
                return response
            else:
                return jsonify({'error': 'Failed to remove token'}), 500

        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Expired token'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401
        except Exception as e:
            return jsonify({'error': str(e)}), 500

        

    # This endpoint confirms the password reset using the token and updates the password
    @app.route('/confirm_password_reset', methods=['POST'])
    def confirm_password_reset():
        data = request.get_json()
        token = data.get('resetToken')
        new_password = data.get('password')
        if not token or not new_password:
            return jsonify({'error': 'Token and new password are required'}), 400
        user_id, error = check_password_reset_token(token)
        if user_id:
            if update_user_password(user_id, new_password):
                return jsonify({'message': 'Password reset successfully'}), 200
            else:
                return jsonify({'error': 'Failed to update password'}), 500
        else:
            return jsonify({'error': error}), 400


    @app.route('/user/firstname', methods=['GET'])
    def get_user_firstname():
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith("Bearer "):
            logging.warning('No token provided', file=sys.stderr)
            return jsonify({'error': 'Missing token'}), 401
        
        token = auth_header.split(" ")[1]
        try:
            logging.info('Attempting to decode token', file=sys.stderr)
            decoded_token = jwt.decode(token, JWT_SECRETS, algorithms=['HS256'])
            logging.info('Token decoded successfully')
        except jwt.ExpiredSignatureError:
            logging.error('Token expired')
            return jsonify({'error': 'Expired token'}), 401
        except jwt.InvalidTokenError:
            logging.error('Invalid token')
            return jsonify({'error': 'Invalid token'}), 401
        except Exception as e:
            logging.exception('Error decoding token')
            return jsonify({'error': 'Internal server error'}), 500

        email = decoded_token.get('email')
        if not email:
            logging.warning('Email not found in token')
            return jsonify({'error': 'Email not found in token'}), 401

        user_data = get_user_data_by_email(email)
        if not user_data:
            logging.warning('User data not found')
            return jsonify({'error': 'User not found'}), 404

        first_name = user_data.get('first_name')
        print("FIrstName in the get_user_firstname:", first_name, file=sys.stderr)
        if not first_name:
            logging.warning('First name not found for user')
            return jsonify({'error': 'First name not found for user'}), 500

        return jsonify({'first_name': first_name}), 200

          



    def _build_cors_preflight_response():
            response = make_response()
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
            return response
        


    @app.route('/request_password_reset', methods=['POST'])
    def request_password_reset():
        data = request.get_json()
        app.logger.info(f"Received data: {data}")
        email = data.get('email')
        app.logger.info(f"Email extracted: {email}")
        user_id = check_user_email(email)
        if user_id:
            token = generate_password_reset_token(email)
            if token:
                send_password_reset_email(email, token, mail, app)
                return jsonify({'message': 'Password reset email sent'}), 200
            return jsonify({'error': 'Failed to generate password reset token'}), 500
        return jsonify({'error': 'User not found'}), 404
    

    @app.route('/calculate_emission', methods=['POST'])
    def calculate_emission():
        data = request.json
        reg = data.get('reg')
        miles = data.get('miles', 0)  # Default to 0 if not provided
        pesssangers = data.get('num_pessangers',1) ## need to take the value, input needed in the front end

        total_emmission_in_miles, total_emission = carApi.final_emition(reg, miles, pesssangers)
        return jsonify({ ### both the mile and the km is going up
            "total_emmission_in_miles": total_emmission_in_miles,
            "total_emission": total_emission
        }), 200


    @app.route('/calculate_bus_emission', methods=['POST'])
    def calculate_bus_emission():
        data = request.json
        miles = data.get('miles', 0)
        total_number_emition = bus_api.calculate_bus_emissions_standardized(miles,100) ## the 2nd parameter is the avarage! no need to touch
        return jsonify({'message': total_number_emition}), 200


    @app.route('/calculate_train_emission', methods=['POST'])
    def calculate_train_emission():
        data = request.json
        miles = data.get('miles', 0)
        total_number_emition = train_api.calculate_train_emissions_standardized(miles,35) ## same, 2nd parameter is an avarage
        return jsonify({'message': total_number_emition}), 200

