from pytest import *
from account import Account

class Test:
    def setup_method(self):
        self.a1 = Account("Shayne")

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == "Shayne"

    def test_deposit(self):
        assert self.a1.deposit(-10) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(10) is True
        assert self.a1.get_balance() == 10

    def test_withdraw(self):
        assert self.a1.deposit(100) is True

        assert self.a1.withdraw(-25) is False
        assert self.a1.get_balance() == 100

        assert self.a1.withdraw(250) is False
        assert self.a1.get_balance() == 100

        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == 100

        assert self.a1.withdraw(25) is True
        assert self.a1.get_balance() == 75
