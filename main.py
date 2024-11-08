from bank import Bank
from bank_account import BankAccount


def main():
	bank = Bank("Name")
	bank.create_account("1","debit", 0, 0)
	bank.deposit_to_account("1", 100)
	bank.get_account_balance("1")
	# print(bank.__accounts)

	account = BankAccount("1", "credit", 100, 10)
	print(account.__balance)



if __name__ == "__main__":
	main()