class Account:
    def __init__(self, name: str) -> None:
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float):
        if amount > 0:
            self.__account_balance = float(self.__account_balance + amount)
            return True
        else:
            return False

    def withdraw(self, amount: float):
        if amount > 0:
            if amount<= self.__account_balance:
                self.__account_balance = float(self.__account_balance - amount)
                return True
            else:
                return False
        else:
            return False

    def get_balance(self) -> str:
        return self.__account_balance

    def get_name(self) -> str:
        return self.__account_name