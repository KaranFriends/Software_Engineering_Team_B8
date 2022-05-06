# project/token.py

from itsdangerous import URLSafeTimedSerializer

#from project import app


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer('blahblahblah')
    return serializer.dumps(email, salt='email-confirm')


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer('blahblahblah') #app.config['SECRET_KEY']
    try:
        email = serializer.loads(
            token,
            salt='email-confirm', #app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email