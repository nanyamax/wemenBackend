from werkzeug.security import generate_password_hash, check_password_hash

def hashPassword(password):
        return generate_password_hash(password, method='scrypt')

def checkHashedPassword(hashedPassword, plaintextPassword ):
        return check_password_hash(hashedPassword, plaintextPassword)