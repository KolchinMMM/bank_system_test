class BankAccount:
    def __init__(self, account_number, account_type, initial_balance=0, interest_rate=0):
        """
        Создает банковский счет с номером, типом и начальным балансом.
        :param account_number: номер счета, любая строка
        :param account_type: тип счета, либо "debit", либо "credit"
        :param initial_balance: Начальный баланс счета, число
        :param interest_rate: процентная ставка, число не меньше 0
        """
        if account_type not in ["debit", "credit"]:
            raise ValueError("account_type может быть только debit или credit")
        if interest_rate < 0:
            raise ValueError("interest_rate не меньше нуля")
        self.__account_type = account_type
        self.__balance = initial_balance
        self.__interest_rate = interest_rate
        self.__credit_value = 10000


    def set_credit_value(self, value):
        if self.__account_type != "credit":
            raise TypeError("Неверный тип аккаунта.")
        if type(value) not in [int, float]:
            raise ValueError("Неверное значение value.")
        if value <= 0:
            raise ValueError("Значение value должно быть неотрицательным.")
        self.__credit_value = value

    def get_credit_value(self):
        return self.__credit_value

    def deposit(self, amount):
        """Внесение денег на счет"""
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        """Снять деньги со счета."""
        if self.__account_type == 'debit' and amount > self.__balance:
            raise ValueError("Недостаточно денег на счете!")
        elif amount > 0:
            self.__balance -= amount
        else:
            raise ValueError("Сумма снятия должна быть положительной.")

    def apply_interest(self):
        """Начисляет проценты на счет в соответствии с установленной ставкой."""
        if self.__interest_rate == 0:
            return
        if self.__account_type == "credit":
            self.__balance -= (self.__credit_value - self.__balance) * self.__interest_rate / 100
        else:
            self.__balance += self.__balance * self.__interest_rate / 100

    def set_interest_rate(self, rate):
        """Устанавливает новую процентную ставку для счета."""
        if rate >= 0:
            self.__interest_rate = rate
        else:
            raise ValueError("Ставка должна быть положительной.")

    def get_balance(self):
        """Метод для получения баланса счета."""
        return self.__balance

    def get_interest_rate(self):
        return self.__interest_rate
