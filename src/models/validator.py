import re

class ValidateUser:
    ''' Class to validate user attributes '''

    def __init__(self, username, password):
        self.username = username        
        self.password = password

    def validate_username(self):
        '''
        Method validates a user's username
        '''

        if not self.username or self.username.isspace() or not isinstance(
                self.username, str):
            return False
        else:
            return True



    def validate_password(self):
        ''' Method validates a user's password '''      

        lower_case = re.search(r"[a-z]", self.password)
        upper_case = re.search(r"[A-Z]", self.password)
        numbers = re.search(r"[0-9]", self.password)

        if not self.password or not all((lower_case, upper_case, numbers))\
                or not len(self.password) > 5:
            return False
        else:
            return True