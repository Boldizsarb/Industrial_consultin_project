import psycopg2
from psycopg2 import pool
import jwt
import datetime
import logging
import os
from dotenv import load_dotenv
import hashlib
from flask import jsonify
import sys
import bcrypt
import hashlib


logger = logging.getLogger(__name__) 
load_dotenv()
JWT_SECRET = os.getenv('JWT_SECRET')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
# DATABASE_URL = os.getenv("DATABASE_URL")

class DBPool:
    _instance = None
    @staticmethod
    def get_instance():
        if DBPool._instance is None:
            DBPool._instance = pool.ThreadedConnectionPool(minconn=1, maxconn=10,
                                                            user="postgres",
                                                            password="postgres",
                                                            host="postgresql",
                                                            port="5432",
                                                            database='industrial_consulting')
        return DBPool._instance

    def create_table_user_if_not_exists():
        with DBPool.get_instance().getconn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'user')")
                table_exists = cur.fetchone()[0]

                if not table_exists:
                    cur.execute("""
                        CREATE TABLE "user" (
                            id SERIAL PRIMARY KEY,
                            first_name VARCHAR(255) NOT NULL,
                            last_name VARCHAR(255) NOT NULL,
                            email VARCHAR(255) NOT NULL UNIQUE,
                            number VARCHAR(20),
                            password VARCHAR(255) NOT NULL,
                            token VARCHAR(255) DEFAULT NULL,
                            verification_token VARCHAR(255),
                            token_expiration TIMESTAMP,
                            verified BOOLEAN NOT NULL DEFAULT FALSE,
                            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )
                    """)
                    conn.commit()
                    return "Table 'user' created successfully."
                else:
                    return "Table 'user' already exists."
                
                
                
    def create_table_password_reset_tokens_if_not_exists():
        with DBPool.get_instance().getconn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'password_reset_tokens')")
                table_exists = cur.fetchone()[0]

                if not table_exists:
                    cur.execute("""
                        CREATE TABLE password_reset_tokens (
                            id SERIAL PRIMARY KEY,
                            user_id INTEGER REFERENCES "user" (id),
                            token VARCHAR(255) NOT NULL,
                            expiration TIMESTAMP NOT NULL,
                            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )
                    """)
                    conn.commit()
                    return "Table 'password_reset_tokens' created successfully."
                else:
                    return "Table 'password_reset_tokens' already exists."
            

    def create_table_car_if_not_exists():
        conn = None
        try:
            conn = DBPool.get_instance().getconn()
            cur = conn.cursor()

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'car')")
            table_exists = cur.fetchone()[0]

            if not table_exists:
                cur.execute("""
                    CREATE TABLE "car" (
                        id SERIAL PRIMARY KEY,
                        user_id INTEGER REFERENCES "user" (id),
                        reg VARCHAR(255) NOT NULL
                    )
                """)
                conn.commit()

            if cur is not None:
                cur.close()
            if conn is not None:
                DBPool.get_instance().putconn(conn)

            return "Table 'car' created successfully."

        except psycopg2.Error as e:
            return f"Unable to create table 'car': {e}"


    def create_table_trip_if_not_exists():
        conn = None
        try:
            conn = DBPool.get_instance().getconn()
            cur = conn.cursor()

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'trip')")
            table_exists = cur.fetchone()[0]

            if not table_exists:
                cur.execute("""
                    CREATE TABLE "trip" (
                        id SERIAL PRIMARY KEY,
                        user_id INTEGER REFERENCES "user" (id),
                        car_id INTEGER REFERENCES "car" (id),
                        distance INTEGER NOT NULL,
                        footprint INTEGER NOT NULL
                        
                    )
                """)
                conn.commit()

            if cur is not None:
                cur.close()
            if conn is not None:
                DBPool.get_instance().putconn(conn)

            return "Table 'trip' created successfully."

        except psycopg2.Error as e:
            return f"Unable to create table 'car': {e}"


    def create_table_public_transport_if_not_exists():
        conn = None
        try:
            conn = DBPool.get_instance().getconn()
            cur = conn.cursor()

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'public_transport')")
            table_exists = cur.fetchone()[0]

            if not table_exists:
                cur.execute("""
                    CREATE TABLE "public_transport" (
                        id SERIAL PRIMARY KEY,
                        user_id INTEGER REFERENCES "user" (id),
                        type VARCHAR(255),
                        footprint INTEGER NOT NULL
                    )
                """)
                conn.commit()

            if cur is not None:
                cur.close()
            if conn is not None:
                DBPool.get_instance().putconn(conn)

            return "Table 'public_transport' created successfully."

        except psycopg2.Error as e:
            return f"Unable to create table 'public_transport': {e}"


# Generating JWT token              
def generate_jwt_token(email):
    try:
        expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        token = jwt.encode({'email': email, 'exp': expiration_time}, JWT_SECRET, algorithm='HS256')
        # Ensure the token is a string
        token = token.decode('utf-8') if isinstance(token, bytes) else token
        print("Verification token generated:", token)
        return token
    except Exception as e:
        print("Error generating JWT token:", str(e))
        return None


# Decoding JWT Token
def decode_jwt_token(token):
    try:
        print("Token to decode:", token)  # Debug statement
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        print("Decoded payload:", payload)  # Debug statement
        return payload, None
    except jwt.ExpiredSignatureError:
        print("Token has expired")  # Debug statement
        return None, "Token has expired"
    except jwt.InvalidTokenError:
        print("Invalid token received:", token)  # Debug statement
        return None, "Invalid token"
    except Exception as e:
        print("Error in decoding token:", str(e))  # Debug statement
        return None, "Error processing your request"


#Insert queries
def create_new_public_transport(transport_type, footprint):
    conn = None
    try:
        conn = DBPool.get_instance().getconn()
        cur = conn.cursor()

        #psycopg2 sanitises inputs automatically so should be safe from SQL injections
        cur.execute("INSERT INTO public_transport(type, footprint) VALUES (%s, %s)", (transport_type, footprint))
        conn.commit()

        if cur is not None:
            cur.close()
        if conn is not None:
            DBPool.get_instance().putconn(conn)

        return "New transport created successfully."

    except psycopg2.Error as e:
        return f"Unable to create new user: {e}"



#Generic database connection test
def test_db_connection():
    conn = None
    try:
        conn = DBPool.get_instance().getconn()
        cur = conn.cursor()
     
        if cur is not None:
            cur.close()
        if conn is not None:
            DBPool.get_instance().putconn(conn)

        return "Database connection successful"
    except psycopg2.Error as e:
        return f"Unable to connect to the database: {e}"



def store_user_in_database(first_name, last_name, email, phone_number, hashed_password, verification_token):
    token_expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    with DBPool.get_instance().getconn() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""
                    INSERT INTO "user" (first_name, last_name, email, number, password, verification_token, token_expiration, verified)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (first_name, last_name, email, phone_number, hashed_password, verification_token, token_expiration, False))
                if not phone_number.isdigit() or len(phone_number) != 10:
                    conn.rollback()
                    return "Invalid phone number format.", 400  # Bad Request
                conn.commit()
                print("User stored with verification token:", verification_token)
                return "User stored successfully."
            except psycopg2.errors.UniqueViolation as e:
                logger.error("Duplicate email address", exc_info=True)
                return "Failed to insert user: Email address already exists.", 409
            except psycopg2.Error as e:
                logger.error(f"Failed to insert user: {e}", exc_info=True)  # Log the error with stack trace
                # Rollback the transaction on error
                conn.rollback() 
                return f"Failed to insert user:", 500
            except Exception as e:
                logger.exception(f"Unexpected error: {e}")  # Log unexpected errors with full context 
                # Rollback the transaction on error
                conn.rollback() 
                return f"Unexpected error: {e}", 500
        

        
def check_user_email(email):
    with DBPool.get_instance().getconn() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT EXISTS (SELECT 1 FROM "user" WHERE email = %s)', (email,))
            user_exists = cur.fetchone()[0]
            return user_exists



def verify_reset_token(email, token):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms='HS256')
        return decoded_token['email'] == email
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
    

   
def update_user_password(user_id, new_password):
    hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
    try:
        with DBPool.get_instance().getconn() as conn:
            with conn.cursor() as cur:
                # Ensure the table name is correctly specified here as "user"
                cur.execute("UPDATE \"user\" SET password = %s WHERE id = %s", (hashed_password, user_id))
                conn.commit()
                return True
    except Exception as e:
        print(f"Error updating password: {e}")
        return False




def generate_password_reset_token(email):
    # Check if the user ID exists based on email 
    with DBPool.get_instance().getconn() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT id FROM "user" WHERE email = %s', (email,))
            users_id = cur.fetchone()
            logger.info("User ID result:", users_id)
            if users_id:
                # Correctly retrieve user_id
                user_id = users_id[0]
                logger.info("User ID:", user_id)

                # Delete any existing tokens for the user
                cur.execute('DELETE FROM password_reset_tokens WHERE user_id = %s', (user_id,))

                # Generate a unique token
                token = generate_jwt_token(email)
                logger.info("Generated token:", token)
                # Calculate token expiration (e.g., 1 hour from now)
                expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
                # Store the token in the database
                cur.execute("""
                    INSERT INTO password_reset_tokens (user_id, token, expiration)
                    VALUES (%s, %s, %s)
                """, (user_id, token, expiration))
                conn.commit()
                logger.info("Token inserted into database.")
                return token
            else:
                return None


def check_password_reset_token(token):
    print(f"Received token for validation: {token}")
    # Ensure token is clean and without the '$' prefix
    clean_token = token.strip('$')
    print(f"Cleaned token: {clean_token}")

    try:
        payload = jwt.decode(clean_token, JWT_SECRET, algorithms=["HS256"])
        print("Decoded payload:", payload)
        email = payload['email']
        return check_token_in_database(email, clean_token)
    except jwt.ExpiredSignatureError:
        return None, "Token has expired"
    except jwt.InvalidTokenError:
        return None, "Invalid token"
    except Exception as e:
        return None, f"Error processing your request: {str(e)}"


def check_token_in_database(email, token):
    try:
        print("Checking token in database for email:", email)  # Debug statement
        with DBPool.get_instance().getconn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT user_id FROM password_reset_tokens 
                    WHERE token = %s AND expiration > NOW()
                """, (token,))
                result = cur.fetchone()
                if result:
                    print("Token is valid and not expired, user_id:", result[0])  # Debug statement
                    return result[0], None
                else:
                    print("No matching token found or token has expired")  # Debug statement
                    return None, "No token found or token does not match"
    except Exception as e:
        print(f"Error checking token in database: {e}")  # Debug statement
        return None, "Error processing your request"



def verify_user_account(email, verification_token):
    with DBPool.get_instance().getconn() as conn:
        with conn.cursor() as cur:
            # Checking if the code matches 
            cur.execute("""
                        SELECT verification_token, token_expiration FROM "user" WHERE email = %s
                        """, (email,))
            stored_code = cur.fetchone()
            if stored_code: 
                stored_token, expiration_time = stored_code 
                if stored_token == verification_token and datetime.datetime.now() < expiration_time:
                    # Updating the user's verification status
                    cur.execute("""
                        UPDATE "user" SET verified = %s WHERE email = %s
                            """, (True, email))
                    conn.commit()
                    return "User Verified successfully."
                else:
                    return "Verification token expired or invalid."
            else:
                return "User not found."
            

def verify_password(email):
    if not email:
        return None
    if not check_user_email(email):
        return None
    with DBPool.get_instance().getconn() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT password FROM "user" WHERE email = %s', (email,))
            print("Password verified", file=sys.stderr)
            stored_password = cur.fetchone()
        if stored_password:
            stored_password_hash = stored_password[0]
            print("the password hash from DB is", stored_password_hash, file=sys.stderr)
            return stored_password_hash
        else:
            return None

def store_sesssion_token(token, email):
    with DBPool.get_instance().getconn() as conn:
        with conn.cursor() as cur:
            print("Original Token:", token)  # Print the original token value

            cur.execute("""
                UPDATE "user" SET token = %s WHERE email = %s
            """, (token, email))
            conn.commit()

            cur.execute("""
                SELECT token FROM "user" WHERE email = %s
            """, (email,))
            stored_token = cur.fetchone()
            print("Stored Token:", stored_token, file=sys.stderr)  # Print the stored token value
            return stored_token[0] if stored_token   else None


def get_stored_token(token):
    with DBPool.get_instance().getconn() as conn:
        print("Token to retrieve:", token, file=sys.stderr)
        with conn.cursor() as cur:
            cur.execute('SELECT token, first_name FROM "user" WHERE token = %s', (token,))
            stored_token, first_name = cur.fetchone()   
            print("Token retrieved ", stored_token, file=sys.stderr)
            return stored_token, first_name if stored_token else None


def get_user_data_by_email(email):
    with DBPool.get_instance().getconn() as conn:
        cursor = conn.cursor()
        query = 'SELECT first_name FROM "user" WHERE email = %s'
        cursor.execute(query, (email,))
        user_data = cursor.fetchone()
        cursor.close()
        
        if user_data:
            # Return user data as a dictionary
            return {'first_name': user_data[0]}
        else:
            return None


def delete_token(email):
    """
    Delete the token associated with the given email address.
    """
    try:
        with DBPool.get_instance().getconn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE "user" SET token = %s WHERE email = %s
                """, (None, email))
                conn.commit()
        return "Token deleted successfully."
    except Exception as e:
        print("Error deleting token associated with email:", e)
        return None  # Indicate failure to delete token


# Function to generate JWT token with expiration time
def generate_token(first_name, email, secret_key, expiration_hours=3):
    # Convert the secret_key to a string if it's not already
    secret_key_str = str(secret_key)

    # Set expiration time to 3 hours from now
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=expiration_hours)
    payload = {'first_name': first_name, 'email': email, 'exp': expiration_time}
    token = jwt.encode(payload, secret_key_str, algorithm='HS256')
    return token  


def remove_stored_token(email):
    """
    Remove the token from the database associated with the given email address.
    """
    try:
        with DBPool.get_instance().getconn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE "user" SET token = NULL WHERE email = %s
                """, (email,))
                conn.commit()
        return True  # Indicate successful token removal
    except Exception as e:
        print("Error removing token from storage:", e)
        return False  # Indicate failure to remove token