import psycopg2
from psycopg2 import pool
import jwt
import datetime
import logging
import os
from dotenv import load_dotenv
from flask import jsonify
import sys
import bcrypt


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
                        user_id INTEGER NOT NULL,
                        reg VARCHAR(255) NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES "user"(id)
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
                        user_id INTEGER NOT NULL,
                        distance INTEGER NOT NULL,
                        footprint INTEGER NOT NULL,
                        car_id INTEGER NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES "user"(id),
                        FOREIGN KEY (car_id) REFERENCES "car"(id)
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
    
   
def update_user_password(email, new_password):
    print(f"Updating password for email: {email}, new password: {new_password}")
    with DBPool.get_instance().getconn() as conn:
        with conn.cursor() as cur:
            try:
                hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                cur.execute('UPDATE "user" SET password = %s WHERE email = %s', (hashed_password, email))
                conn.commit()
                return "Password updated successfully."
            except psycopg2.Error as e:
                logger.error(f"Failed to update password: {e}", exc_info=True)
                conn.rollback()
                return "Failed to update password.", 500
            except Exception as e:
                logger.exception(f"Unexpected error: {e}")
                conn.rollback()
                return "Unexpected error.", 500
            




def generate_password_reset_token(user_id):
    # Generate a unique token
    token = generate_jwt_token()
    # Calculate token expiration (e.g., 1 hour from now)
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
    # Store the token in the database
    with DBPool.get_instance().getconn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO password_reset_tokens (user_id, token, expiration)
                VALUES (%s, %s, %s)
            """, (user_id, token, expiration))
            conn.commit()
    return token


def check_password_reset_token(email, token):
    print(f"Checking password reset token for email: {email}, token: {token}")
    with DBPool.get_instance().getconn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, expiration FROM "password_reset_tokens" 
                WHERE user_id = (SELECT id FROM "user" WHERE email = %s) 
                AND token = %s
            """, (email, token))
            result = cur.fetchone()

            if result:
                logger.info(f"Password reset token found: {result}")
                user_id, expiration = result
                if datetime.datetime.utcnow() < expiration:
                    return user_id  # Token valid and not expired
                else:
                    return False  # Token expired 
            else:
                return False  # Token not found


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
            
def verify_password(email, password):
    if not email or not password:
        return False
    if not check_user_email(email):
        return False
    with DBPool.get_instance().getconn() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT password FROM "user" WHERE email = %s', (email,))
            print("Password verified", file=sys.stderr)
            stored_password = cur.fetchone()[0]
            print("the password hash from DB is", stored_password, file=sys.stderr) 
            # Ensure the stored password hash is encoded to bytes
            stored_password_bytes = stored_password.encode('utf-8')
            return stored_password_bytes

