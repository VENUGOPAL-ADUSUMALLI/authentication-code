


class AuthenticationError(Exception):

    pass


class InvalidCredentialsError(AuthenticationError):

    pass


class UserAlreadyExistsError(AuthenticationError):

    pass


class ValidationError(AuthenticationError):

    pass
