from passtype import *
from user import *
class PassSystem:
    def __init__(self):
        self.users = []  # List of users in the system
        self.pass_types = []  # Available pass types

    def add_user(self, name, email):
        """Add a user to the system"""
        user = User(name, email)
        self.users.append(user)
        return user

    def add_pass_type(self, name, validity_period_days):
        """Add a pass type to the system"""
        pass_type = PassType(name, validity_period_days)
        self.pass_types.append(pass_type)
        return pass_type