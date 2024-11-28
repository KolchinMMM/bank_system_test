from bank import Bank
from bank_account import BankAccount


def main():
	bank = Bank("Name")
	bank.create_account("1","credit", 100, 10)
	bank.set_account_credit_value("1",50)
	bank.apply_interest_to_all_accounts()
	print(bank.get_account_balance("1"))



if __name__ == "__main__":
	main()