""" This class validates the email addresses and password when logging on."""

class Validation:
    """ This class contains methods for validating email addresses and passwords."""
    @staticmethod
    # TODO: Implement the validate_email method using the staticmethod decorator.
    # TODO: The method should take an email parameter and return True if the email contains an "@" symbol.
    def validate_email (email):
        if "@" in email:
            return True
        else:
            return False
        
    @staticmethod
    def validate_password (password):
        """
        This method validates a password based on the following criteria:
        - The password must be at least 8 characters long.
        - The password must contain at least one uppercase letter,
          one lowercase letter, one digit, and one special character (!@#$%^&*).

        Args:
          password (str): The password to be validated.

        Returns:
          bool: True if the password is valid, False otherwise.
        """
        """
        This method validates a password based on the following criteria:
        - The password must be at least 8 characters long.
        - The password must contain at least one uppercase letter,
          one lowercase letter, one digit, and one special character (!@#$%^&*).

        Args:
          password (str): The password to be validated.

        Returns:
          bool: True if the password is valid, False otherwise.
        """
        # TODO: Implement the password length validation logic.
        # TODO: Check if the password is at least 8 characters long if not return False.
        if len(password) < 8:
            return False
        has_upper = False if not any(char.isupper() for char in password) else True
        has_lower = False if not any(char.islower() for char in password) else True
        has_digit = False if not any(char.isdigit() for char in password) else True
        has_special = False if not any(char in "!@#$%^&*" for char in password) else True
        # Return the boolean value based on the conditions.
        return has_upper and has_lower and has_digit and has_special
