from flask import Flask, request, jsonify, make_response 
import bcrypt
from database import *
from flask_cors import CORS
from flask_mail import Mail
import os 
from dotenv import load_dotenv
from email_sending import *
from routes import configure_routes


load_dotenv()


app = Flask(__name__)
mail = Mail(app)


## POOL IS IN THE DATABASE FILE
# Mail configuration
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['JWT_SECRET'] = os.environ.get('JWT_SECRET')   


  # This will configure the mail instance with the app

# Allow CORS for requests from 'http://localhost:8080'
CORS(app)

configure_routes(app, mail)
@app.route('/message', methods=['GET'])
def get_message():
    return jsonify({'message': 'Hello, World!'})

@app.route('/database', methods=['GET']) ## checking if database is connecting
def get_database():
    return test_db_connection()


@app.route('/email_sending', methods=['POST'])
def send_verification_email():
    return jsonify({'message': 'Verification email sent successfully'}), 200


# Calling the function of the create table to ensure that database is created on startup 
with app.app_context():
    create_table_user_if_not_exists()
    create_table_password_reset_tokens_if_not_exists()


@app.route('/users', methods=['GET'])
def get_users():
    try:
        with DBPool.get_instance().getconn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM \"user\"")
                rows = cur.fetchall()
                users = []
                for row in rows:
                    user = {
                        'id': row[0],
                        'first_name': row[1],
                        'last_name': row[2],
                        'email': row[3],
                        'number': row[4],
                        'password': row[5],
                        'verified': row[8],
                        'created': row[9]
                    }
                    users.append(user)
                return jsonify(users), 200
    except Exception as e:
        logger.exception(f"Error fetching users: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500
    

@app.route('/tokens', methods=['GET'])
def get_tokens():
    try:
        with DBPool.get_instance().getconn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM \"password_reset_tokens\"")
                rows = cur.fetchall()
                tokens = []
                for row in rows:
                    token = {
                        'id': row[0],
                        'user_id': row[1],
                        'token': row[2],
                        'expiration': row[3],
                        'created': row[4]
                    }
                    tokens.append(token)
                return jsonify(tokens), 200
    except Exception as e:
        logger.exception(f"Error fetching tokens: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500
    

if __name__ == '__main__':
     # Initialize the database connection pool
    DBPool.get_instance()
    print('Starting the application')
    app.run(host='0.0.0.0', port=5000, debug=True)
