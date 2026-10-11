import bcrypt

class Hash:
    @staticmethod
    def bcrypt(password: str):
        # hash
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def verify(plain_password, hashed_password):
        # plain first, hashed second
        try:
            return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
        except Exception as e:
            print("Verify error:", e)
            return False