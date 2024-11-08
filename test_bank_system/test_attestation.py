import unittest
from bank import Bank


class TestAttestation(unittest.TestCase):
	def test_apply_interest_several_times(self):
		bank = Bank("MyBank")
		bank.create_account("1", "debit", 100, 20)
		bank.create_account("2", "credit", 100, 20)
		bank.set_account_credit_value("2", 200)

		bank.apply_interest_to_all_accounts()

		bank.create_account("3", "debit", 100, 20)
		bank.set_account_interest_rate("2", 100)

		bank.apply_interest_to_all_accounts()

		self.assertEqual(bank.get_account_balance("1"), 144)
		self.assertEqual(bank.get_account_balance("2"), -40)
		self.assertEqual(bank.get_account_balance("3"), 120)

	def test_delete_then_create_again_account(self):
		bank = Bank("MyBank")

		bank.create_account("1", "debit", 100, 20)
		bank.create_account("2", "credit", 100, 20)

		bank.apply_interest_to_all_accounts()

		bank.delete_account("1")

		bank.create_account("1", "credit", 10, 10)

		self.assertEqual(bank.get_account_balance("1"), 10)
		self.assertEqual(bank.get_accounts_names(), ["2", "1"])

	def test_poor_account(self):
		bank = Bank("MyBank")
		bank.create_account("1", "debit", 100, 20)

		for i in range(20):
			bank.apply_interest_to_account("1")
		print(bank.get_account_balance("1"))
		self.assertAlmostEqual(bank.get_account_balance("1"), 100 * (1.2**20))
