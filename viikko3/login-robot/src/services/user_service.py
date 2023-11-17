from entities.user import User
import sys, pdb


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):

        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        if not username.isalpha() or not len(username) >= 3:
            raise UserInputError("Username is not valid")
        if password.isalpha() or not len(password) >= 8:
            raise UserInputError("Password is not valid")
        exists = self._user_repository.find_by_username(username)
        if exists:
            raise UserInputError("Username already exists")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
