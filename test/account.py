class Account:
    def __init__(self, name: str) -> None:
        '''
        init function declares name and balance
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float):
        '''
        Function takes a value from amount and tests to see if its valid then adds it to account balance
        :param amount (float): This is the value added to balance
        :return: Relays if the value went through or not
        '''
        if amount > 0:
            self.__account_balance = float(self.__account_balance + amount)
            return True
        else:
            return False

    def withdraw(self, amount: float):
        '''
        Function takes a value from amount and tests to see if its valid and then subtracts it from the balance
        :param amount (float): This is the value taken from balance
        :return: Relays if the value went through or not
        '''
        if amount > 0:
            if amount<= self.__account_balance:
                self.__account_balance = float(self.__account_balance - amount)
                return True
            else:
                return False
        else:
            return False

    def get_balance(self) -> str:
        '''
        Function gets the balance of the account
        :return: Gets the balance of the account
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Function gets the name of the account
        :return: Gets the name of the account
        '''
        return self.__account_name
