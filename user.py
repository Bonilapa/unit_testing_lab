from skypass import *
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.passes = []  # List of passes issued to this user

    def issue_pass(self, pass_type):
        """Issue a new pass to the user"""
        new_pass = SkyPass(pass_type, self)
        self.passes.append(new_pass)
        return new_pass
