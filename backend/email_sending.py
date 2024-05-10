import smtplib 




def send_verification_email(user_email, verification_token, mail, app):
    with app.app_context():
        try:
            server = smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT'])
            server.ehlo()  
            server.starttls()  # For secure connections
            server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])  

            message = f"Subject: Verify Your Account\n\nYour verification code is: http://localhost:8081/${verification_token}" 
            server.sendmail(app.config['MAIL_USERNAME'], user_email, message)
            print('Email sent successfully') 
        except Exception as e:
            print(f'Failed to send verification email: {e}')
        finally:
            server.quit() 

def send_password_reset_email(email, token, mail, app):
    with app.app_context():
        try:
            server = smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT'])
            server.ehlo()  
            server.starttls()  # For secure connections
            server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])  

            message = f"Subject: Password Reset\n\nClick the following link to reset your password: http://localhost:8081/confirmPassword/${token}"
            server.sendmail(app.config['MAIL_USERNAME'], email, message)
            print('Email sent successfully') 
        except Exception as e:
            print(f'Failed to send password reset email: {e}')
        finally:
            server.quit()