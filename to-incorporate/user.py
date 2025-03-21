class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password  # need to add more to password to make it hash for safty
        self.email = email

    def check_password(self, input_password):
        return self.password == input_password

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "email": self.email
        }