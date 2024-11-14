import unittest
from bank import Bank


class TestIntegration(unittest.TestCase):
	def test_duplicate_accounts(self):
		bank = Bank("myBank")
		bank.create_account("1", "credit")
		with self.assertRaises(IndexError):
			bank.create_account("1", "credit")

	def test_create_several_accounts(self):
		bank = Bank("myBank")
		bank.create_account("1", "debit", 10, 20)
		bank.create_account("2", "credit", 10)
		bank.create_account("3", "debit", interest_rate=20)
		bank.create_account("4", "credit")
		self.assertEqual(len(bank.get_accounts_names()), 4)

	def test_can_get_balance(self):
		bank = Bank("myBank")
		bank.create_account("1", "debit", 10, 20)
		self.assertEqual(bank.get_account_balance("1"), 10)

	def test_cannot_get_balance_from_nonexistent_account(self):
		bank = Bank("myBank")
		with self.assertRaises(IndexError):
			bank.get_account_balance("1")

	def test_deposit_to_existent_account(self):
		bank = Bank("myBank")
		bank.create_account("1", "debit", 10, 20)
		bank.create_account("2", "credit", 10)
		bank.deposit_to_account("1", 100)
		bank.deposit_to_account("2", 200)
		self.assertEqual(bank.get_account_balance("1"), 110)
		self.assertEqual(bank.get_account_balance("2"), 210)

	def test_deposit_negative(self):
		bank = Bank("myBank")
		bank.create_account("1", "debit", 10, 20)
		with self.assertRaises(ValueError):
			bank.deposit_to_account("1", -1)

	def test_withdraw_from_credit(self):
		bank = Bank("myBank")
		bank.create_account("1", "credit", 10, 20)
		bank.withdraw_from_account("1", 100)
		self.assertEqual(bank.get_account_balance("1"), -90)

	def test_withdraw_from_debit(self):
		bank = Bank("myBank")
		bank.create_account("1", "debit", 100, 20)
		bank.withdraw_from_account("1", 100)
		self.assertEqual(bank.get_account_balance("1"), 0)

	def test_withdraw_negative(self):
		bank = Bank("myBank")
		bank.create_account("1", "debit", 100, 20)
		with self.assertRaises(ValueError):
			bank.withdraw_from_account("1", -100)

	def test_withdraw_from_debit_not_enough_money(self):
		bank = Bank("myBank")
		bank.create_account("1", "debit", 100, 20)
		with self.assertRaises(ValueError):
			bank.withdraw_from_account("1", 101)

	def test_withdraw_from_nonexistent_account(self):
		bank = Bank("myBank")
		with self.assertRaises(IndexError):
			bank.withdraw_from_account("1", 101)

	def test_set_account_credit_value(self):
		bank = Bank("myBank")
		bank.create_account("1", "credit", 100, 20)
		bank.set_account_credit_value("1", 1000)
		self.assertEqual(bank.get_account_credit_value("1"), 1000)

	def test_set_credit_value_to_nonexistent_account(self):
		bank = Bank("myBank")
		with self.assertRaises(IndexError):
			bank.set_account_credit_value("1", 1000)

	def test_apply_interest_to_credit(self):
		bank = Bank("myBank")
		bank.create_account("1", "credit", 100, 20)
		bank.set_account_credit_value("1", 200)
		bank.apply_interest_to_account("1")
		self.assertEqual(bank.get_account_balance("1"), 80)

	def test_apply_interest_to_debit(self):
		bank = Bank("myBank")
		bank.create_account("1", "debit", 100, 20)
		bank.apply_interest_to_account("1")
		self.assertEqual(bank.get_account_balance("1"), 120)

	def test_apply_interest_to_nonexistent_account(self):
		bank = Bank("myBank")
		with self.assertRaises(IndexError):
			bank.apply_interest_to_account("1")

	def test_apply_interest_to_all_accounts(self):
		bank = Bank("myBank")
		bank.create_account("1", "debit", 100, 20)

		bank.create_account("2", "credit", 100, 10)
		bank.set_account_credit_value("2", 200)

		bank.create_account("3", "credit", 100, 10)
		bank.set_account_credit_value("3", 100)

		bank.create_account("4", "debit", 0, 10)
		bank.apply_interest_to_all_accounts()

		self.assertEqual(bank.get_account_balance("1"), 120)
		self.assertEqual(bank.get_account_balance("2"), 90)
		self.assertEqual(bank.get_account_balance("3"), 100)
		self.assertEqual(bank.get_account_balance("1"), 120)

	def test_set_account_interest_rate(self):
		bank = Bank("myBank")
		bank.create_account("1", "debit", 100, 20)
		bank.set_account_interest_rate("1", 123)
		self.assertEqual(bank.get_account_interest_rate("1"), 123)

	def test_set_account_interest_rate_to_nonexistent_account(self):
		bank = Bank("myBank")
		with self.assertRaises(IndexError):
			bank.set_account_interest_rate("1", 123)

	def test_delete_account(self):
		bank = Bank("myBank")
		bank.create_account("1", "debit", 100, 20)
		bank.delete_account("1")
		self.assertTrue("1" not in bank.get_accounts_names())

	def test_delete_nonexistent_account(self):
		bank = Bank("myBank")
		with self.assertRaises(IndexError):
			bank.delete_account("1")

	def test_get_accounts_names(self):
		bank = Bank("myBank")
		bank.create_account("1", "debit", 100, 20)
		bank.create_account("2", "debit", 100, 20)
		bank.create_account("3", "debit", 100, 20)
		self.assertEqual(bank.get_accounts_names(), ["1", "2", "3"])

	def test_get_nonexistent_account_credit_value(self):
		bank = Bank("myBank")
		bank.create_account("1", "debit", 100, 20)
		with self.assertRaises(IndexError):
			bank.get_account_credit_value("12")
