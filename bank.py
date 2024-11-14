
from bank_account import BankAccount

class Bank:
    def __init__(self, name):
        self.__accounts = {}
        if type(name) != str:
            raise ValueError("Имя должно быть строчным значением!")
        self.name = name
        self.__not_found_account_error = "Счет не найден!"


    def create_account(self, account_number, account_type, initial_balance=0, interest_rate=0):
        """Создать новый счет
        :param account_number: номер счета, любая строка
        :param account_type: тип счета, либо "debit", либо "credit"
        :param initial_balance: Начальный баланс счета, строка
        :param interest_rate: процентная ставка
        """
        if account_number not in self.__accounts:
            self.__accounts[account_number] = BankAccount(account_number, account_type, initial_balance, interest_rate)
        else:
            raise IndexError("Счет с таким номером уже существует!")

    def deposit_to_account(self, account_number, amount):
        """Вносит деньги на счет по номеру
        :param account_number: номер счета, строка
        :param amount: сумма, число > 0"""
        if amount <= 0:
            raise ValueError("Сумма должна быть больше нуля!")
        account = self.__accounts.get(account_number)
        if account:
            account.deposit(amount)
        else:
            raise IndexError(self.__not_found_account_error)

    def withdraw_from_account(self, account_number, amount):
        """Снимает деньги с указанного счета.
        :param account_number: номер аккаунта, строка
        :param amount: сумма, число больше 0"""
        if amount <= 0:
            raise ValueError("Сумма должна быть больше нуля!")
        account = self.__accounts.get(account_number)
        if account:
            account.withdraw(amount)
        else:
            raise IndexError(self.__not_found_account_error)

    def get_account_balance(self, account_number):
        """Вывести баланс по номеру счета"""
        account = self.__accounts.get(account_number)
        if account:
            return account.get_balance()
        else:
            raise IndexError(self.__not_found_account_error)

    def apply_interest_to_all_accounts(self):
        """Начислить проценты по всем счетам"""
        for account in self.__accounts.values():
            account.apply_interest()

    def apply_interest_to_account(self, account_number):
        account = self.__accounts.get(account_number)
        if account:
            account.apply_interest()
        else:
            raise IndexError(self.__not_found_account_error)

    def set_account_interest_rate(self, account_number, rate):
        """Установить новую процентную ставку для указанного счета."""
        account = self.__accounts.get(account_number)
        if account:
            account.set_interest_rate(rate)
        else:
            raise IndexError(self.__not_found_account_error)

    def get_account_interest_rate(self, account_number):
        account = self.__accounts.get(account_number)
        if account:
            return account.get_interest_rate()
        else:
            raise IndexError(self.__not_found_account_error)

    def delete_account(self, account_number):
        account = self.__accounts.get(account_number)
        if account:
            self.__accounts.pop(account_number)
        else:
            raise IndexError(self.__not_found_account_error)

    def get_accounts_names(self):
        return list(self.__accounts.keys())

    def set_account_credit_value(self, account_number, value):
        account = self.__accounts.get(account_number)
        if account:
            account.set_credit_value(value)
        else:
            raise IndexError(self.__not_found_account_error)

    def get_account_credit_value(self, account_number):
        account = self.__accounts.get(account_number)
        if account:
            return account.get_credit_value()
        else:
            raise IndexError(self.__not_found_account_error)

