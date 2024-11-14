import unittest
from bank_account import BankAccount
from bank import Bank


class TestBankAccount(unittest.TestCase):
	def test_init_account_with_balance_and_rate(self):
		account = BankAccount("1", "debit", 100, 10)
		self.assertEqual(account.get_balance(), 100)
		self.assertEqual(account.get_interest_rate(), 10)

		account = BankAccount("1", "debit", initial_balance=100)
		self.assertEqual(account.get_balance(), 100)
		self.assertEqual(account.get_interest_rate(), 0)

		account = BankAccount("1", "debit", interest_rate=10)
		self.assertEqual(account.get_balance(), 0)
		self.assertEqual(account.get_interest_rate(), 10)

	def test_init_wrong_type(self):
		with self.assertRaises(ValueError):
			BankAccount("1", "abc")

	def test_deposit(self):
		account = BankAccount("1", "debit")
		account.deposit(500)
		self.assertEqual(account.get_balance(), 500)

		account = BankAccount("1", "credit", 100)
		account.deposit(200.5)
		self.assertEqual(account.get_balance(), 300.5)

	def test_deposit_negative(self):
		account = BankAccount("1", "debit")
		with self.assertRaises(ValueError):
			account.deposit(-500)

	def test_debit_withdraw(self):
		account = BankAccount("1", "debit", 100)
		account.withdraw(92.5)
		self.assertEqual(account.get_balance(), 7.5)

		account = BankAccount("1", "debit", 100)
		account.withdraw(100)
		self.assertEqual(account.get_balance(), 0)

	def test_debit_withdraw_more_than_balance(self):
		account = BankAccount("1", "debit", 100)
		with self.assertRaises(ValueError):
			account.withdraw(101)

	def test_credit_withdraw(self):
		account = BankAccount("1", "credit", 100)
		account.withdraw(100)
		self.assertEqual(account.get_balance(), 0)

		account = BankAccount("1", "credit", 100)
		account.withdraw(195)
		self.assertEqual(account.get_balance(), -95)

	def test_apply_interest_debit(self):
		account = BankAccount("1", "debit", 100, 10)
		account.apply_interest()
		self.assertEqual(account.get_balance(), 110)

		account = BankAccount("1", "debit", 100)
		account.apply_interest()
		self.assertEqual(account.get_balance(), 100)

	def test_set_credit_value_to_credit(self):
		account = BankAccount("1", "credit", 100, 10)
		account.set_credit_value(200)
		self.assertEqual(account.get_credit_value(), 200)

	def test_set_negative_credit_value_to_credit(self):
		account = BankAccount("1", "credit", 100, 10)
		with self.assertRaises(ValueError):
			account.set_credit_value(-200)

	def test_set_non_numeric_credit_value_to_credit(self):
		account = BankAccount("1", "credit", 100, 10)
		with self.assertRaises(ValueError):
			account.set_credit_value("abc")

	def test_set_credit_value_to_debit(self):
		account = BankAccount("1", "debit", 100, 10)
		with self.assertRaises(TypeError):
			account.set_credit_value(200)

	def test_apply_interest_credit(self):
		account = BankAccount("1", "credit", 100, 10)
		account.set_credit_value(200)
		account.apply_interest()
		self.assertEqual(account.get_balance(), 90)

		account = BankAccount("1", "credit", 200, 10)
		account.set_credit_value(200)
		account.apply_interest()
		self.assertEqual(account.get_balance(), 200)

		account = BankAccount("1", "credit", -800, 10)
		account.set_credit_value(200)
		account.apply_interest()
		self.assertEqual(account.get_balance(), -900)

		account = BankAccount("1", "credit", 100)
		account.set_credit_value(200)
		account.apply_interest()
		self.assertEqual(account.get_balance(), 100)

	def test_get_interest(self):
		account = BankAccount("1", "credit", 100, 10)
		self.assertEqual(account.get_interest_rate(), 10)

		account = BankAccount("1", "debit", 100)
		self.assertEqual(account.get_interest_rate(), 0)

	def test_change_interest(self):
		account = BankAccount("1", "credit", 100, 10)
		account.set_interest_rate(5)
		self.assertEqual(account.get_interest_rate(), 5)

	def test_change_interest_negative(self):
		account = BankAccount("1", "credit", 100, 10)
		with self.assertRaises(ValueError):
			account.set_interest_rate(-5)


	def test_cannot_get_private_fields(self):
		account = BankAccount("1", "credit", 100, 10)
		with self.assertRaises(AttributeError):
			account.__balance
		with self.assertRaises(AttributeError):
			account.__account_number
		with self.assertRaises(AttributeError):
			account.__initial_balance
		with self.assertRaises(AttributeError):
			account.__interest_rate

	def test_init_interest_below_zero(self):
		with self.assertRaises(ValueError):
			BankAccount("1", "credit", 100, -10)

	def test_withdraw_negative(self):
		account = BankAccount("1", "credit", 100, 10)
		with self.assertRaises(ValueError):
			account.withdraw(-10)


class TestBank(unittest.TestCase):
	def test_create_bank_no_accounts(self):
		bank = Bank("MyBank")
		self.assertEqual(bank.get_accounts_names(), [])

	def test_create_bank_correct_name(self):
		bank = Bank("MyBank")
		self.assertEqual(bank.name, "MyBank")

	def test_create_bank_wrong_name(self):
		with self.assertRaises(ValueError):
			Bank(True)

	def test_cannot_access_accounts(self):
		bank = Bank("MyBank")
		with self.assertRaises(AttributeError):
			bank.__accounts

	def test_deposit_to_nonexistent_account(self):
		bank = Bank("MyBank")
		with self.assertRaises(IndexError):
			bank.deposit_to_account("1", 12)

	def test_get_interest_of_nonexistent_account(self):
		bank = Bank("MyBank")
		with self.assertRaises(IndexError):
			bank.get_account_interest_rate("1")