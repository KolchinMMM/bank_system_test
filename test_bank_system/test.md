# Перечень тестов
## Блочное тестирование
### Модуль bank_account.py

#### Б1. test_init_account_with_balance_and_rate (позитивный)
* Цель: Проверка инициализации счета с верно заполненными полями initial_balance и interest_rate
* Входные данные: 
  1. ("1", "debit", 100, 5);
  2. ("1", "debit", initial_balance=100); 
  3. ("1", "credit", interest_rate=10)
* Ожидаемый результат: к каждому счету применится метод get_balance() и get_interest_rate() и они вернут:
  1. 100, 5
  2. 100, 0
  3. 0, 10
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### Б2. test_init_wrong_type (негативный)
* Цель: Инициализировать счет с неверным значением account_type.
* Входные данные: 1. ("12345", "abc");
* Ожидаемый результат: вызывается ValueError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### Б3. test_deposit (позитивный)
* Цель: Проверить, что метод deposit() увеличивает значение суммы на счету верно.
* Входные данные: 
  1. ("1", "debit"), deposit(500)
  2. ("1", "credit", 100), deposit(200.5)
* Ожидаемый результат: метод get_balance возвращает следующие значения:
  1. 500
  2. 300.5
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### Б4. test_deposit_negative (позитивный)
* Цель: Проверить, что нельзя вносить отрицательную сумму.
* Входные данные: 1. ("1", "debit"), deposit(-500);
* Ожидаемый результат: вызывается ValueError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### Б5. test_debit_withdraw (позитивный)
* Цель: Проверить, что с дебетового счета можно снять деньги.
* Входные данные: 
  1. ("1", "debit", 100), withdraw(92.5);
  2. ("1", "debit", 100), withdraw(100)
* Ожидаемый результат: метод get_balance возвращает следующие суммы:
  1. 7.5
  2. 0
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### Б6. test_debit_withdraw_more_than_balance (негативный)
* Цель: Проверить, что нельзя снять с дебетового счета больше, чем текущий баланс
* Входные данные: 1. ("1", "debit", 100), withdraw(101);
* Ожидаемый результат: вызывается ValueError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### Б7. test_credit_withdraw (позитивный)
* Цель:
* Входные данные:
  1. ("1", "credit", 100), withdraw(100);
  2. ("1", "credit", 100), withdraw(195)
* Ожидаемый результат: метод get_balance возвращает следующие суммы:
  1. 0
  2. -95
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### Б. test_apply_interest_debit (позитивный)
* Цель: Проверить работу процентных начислений на накопительный счет
* Входные данные: 
  1. ("1", "debit", 100, 10), apply_interest();
  2. ("1", "debit", 100), apply_interest()
* Ожидаемый результат: метод get_balance возвращает следующие суммы:
  1. 110
  2. 100
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### Б. test_set_credit_value_to_credit (позитивный)
* Цель: проверить возможность установки значения кредита.
* Входные данные: ("1", "credit", 100, 10), set_credit_value(200)
* Ожидаемый результат: метод get_credit_value  возвращает 200
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### Б. test_set_negative_credit_value_to_credit (негативный)
* Цель: проверить невозможность установки отрицательного значения кредита.
* Входные данные: ("1", "credit", 100, 10), set_credit_value(-200)
* Ожидаемый результат: метод get_credit_value  вызывает ValueError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### Б. test_set_negative_credit_value_to_credit (негативный)
* Цель: проверить невозможность установки не числового значения кредита.
* Входные данные: ("1", "credit", 100, 10), set_credit_value("abc")
* Ожидаемый результат: метод get_credit_value  вызывает ValueError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### Б. test_set_credit_value_to_debit (позитивный)
* Цель: проверить невозможность установки значения кредита для накопительного счета.
* Входные данные: ("1", "debit", 100, 10), set_credit_value(-200)
* Ожидаемый результат: метод get_credit_value  вызывает TypeError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.


#### Б. test_apply_interest_credit (позитивный)
* Цель: Проверить работу процентных начислений для кредитного счета
* Входные данные:
  1. ("1", "credit", 100, 10), apply_interest(200);
  2. ("1", "credit", 200, 10), apply_interest(200);
  3. ("1", "credit", -800, 10), apply_interest(200)
  ("1", "credit", 100), apply_interest(200)
* Ожидаемый результат: метод get_balance возвращает следующие суммы:
  1. 90
  2. 200
  3. -900
  4. 100
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.



#### Б. test_get_interest (позитивный)
* Цель: проверить возможность получения процентной ставки.
* Входные данные:
  1. ("1", "credit", 100, 10);
  2. ("1", "debit", 100); 
* Ожидаемый результат: метод get_interest_rate возвращает следующие суммы:
  1. 10
  2. 0
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### Б. test_change_interest (позитивный)
* Цель: проверить возможность изменения ставки.
* Входные данные:
  1. ("1", "credit", 100, 10), set_interest_rate(5);
* Ожидаемый результат: get_interest_rate(): 5
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### Б. test_change_interest_negative (негативный)
* Цель: проверить невозможность изменения ставки на отрицательную
* Входные данные: ("1", "credit", 100, 10), set_interest_rate(-5);
* Ожидаемый результат: вызывается ValueError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### Б. test_cannot_get_private_fields (негативный)
* Цель: проверить, что нельзя получить значения приватных полей
* Входные данные: ("MyBank")
* Ожидаемый результат: вызывается AttributeError при попытке доступа к __balance, __account_number, __initial_balance, __interest_rate
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.


### Модуль bank.py

#### Б. test_create_bank_no_accounts (позитивный)
* Цель: проверить, что создается банк без счетов
* Входные данные: ("MyBank")
* Ожидаемый результат:get_accounts_names() = []
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### Б. test_create_bank_correct_name (позитивный)
* Цель: 
* Входные данные: ("MyBank")
* Ожидаемый результат:
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### Б. test_create_bank_no_accounts (позитивный)
* Цель: проверить, что создается банк с верным названием
* Входные данные: ("MyBank")
* Ожидаемый результат: name = "MyBank"
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### Б. test_create_bank_wrong_name (негативный)
* Цель: проверить, что нельзя создать аккаунт с неверным названием
* Входные данные: (True)
* Ожидаемый результат: вызывается ValueError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.


#### Б. test_cannot_access_accounts (негативный)
* Цель: проверить, что нельзя получить доступ к приватному полю __accounts.
* Входные данные: ("MyBank")
* Ожидаемый результат: вызывается AttributeError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

## Интеграционное тестирование
#### И. test_duplicate_accounts(негативный)
* Цель: проверить, что нельзя создавать несколько счетов с одинаковым именем.
* Входные данные: Bank("MyBank"), create_account("1", "credit")
* Ожидаемый результат: при повторной попытке создания счета create_account("1", "credit") вызывается IndexError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### И. test_create_several_accounts (позитивный)
* Цель: проверить, что можно создать несколько счетов.
* Входные данные: Bank("MyBank"),create_account("1", "debit", 10, 20), create_account("2", "credit", 10), create_account("3", "debit", interest_rate=20), create_account("4", "credit")
* Ожидаемый результат: создано 4 аккаунта
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### И. test_can_get_balance(позитивный)
* Цель: проверить, что можно получить баланс счета через класс банка
* Входные данные: Bank("MyBank"), create_account("1", "debit", 10, 20)
* Ожидаемый результат: get_account_balance("1"): 10
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### И. test_cannot_get_balance_from_nonexistent_account (негативный)
* Цель: проверить, что нельзя получить баланс несуществующего банка
* Входные данные: Bank("MyBank")
* Ожидаемый результат: get_account_balance("1"): вызывает IndexError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.


#### И. test_deposit_to_existent_account (позитивный)
* Цель: проверить, что можно внести деньги на счет
* Входные данные: Bank("MyBank"), create_account("1", "credit", 10, 20), create_account("2", "credit", 10)
* Ожидаемый результат: deposit_to_account("1", 100): 110, deposit_to_account("2", 200): 210
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.


#### И. test_deposit_negative (негативный)
* Цель: проверить, что нельзя внести отрицательное число на счет
* Входные данные: Bank("MyBank"), create_account("1", "debit", 10, 20)
* Ожидаемый результат: deposit_to_account("1", -1) вызывает ValueError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.


#### И. test_withdraw_from_credit (позитивный)
* Цель: проверить, что можно списать деньги с кредитного счета
* Входные данные: Bank("MyBank"), create_account("1", "credit", 10, 20)
* Ожидаемый результат: withdraw_from_account("1", 100) вернет -90
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.


#### И. test_withdraw_from_debit (позитивный)
* Цель: проверить, что можно списать деньги с накопительного счета
* Входные данные: Bank("MyBank"), create_account("1", "debit", 100, 20), withdraw_from_account("1", 100)
* Ожидаемый результат: get_account_balance("1"): 0
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### И. test_withdraw_negative (позитивный)
* Цель: проверить, что нельзя снять отрицательную сумму
* Входные данные: Bank("MyBank"), create_account("1", "credit", 100, 20)
* Ожидаемый результат: withdraw_from_account("1", -100): вызывает valueError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### И. test_withdraw_from_debit_not_enough_money (позитивный)
* Цель: проверить, что нельзя списать больше, чем есть на накопительном счету
* Входные данные: Bank("MyBank"), create_account("1", "debit", 100, 20)
* Ожидаемый результат: withdraw_from_account("1", 101) вызывает ValueError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### И. test_withdraw_from_nonexistent_account (негативный)
* Цель: проверить, что 
* Входные данные: Bank("MyBank")
* Ожидаемый результат: withdraw_from_account("1", 101) вызывает IndexError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### И. test_set_account_credit_value (позитивный)
* Цель: проверить, что можно установить значение кредита для кредитного счета
* Входные данные: Bank("MyBank"), create_account("1", "credit", 100, 20), set_account_credit_value("1", 1000)
* Ожидаемый результат: get_account_credit_value("1"): 1000
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.


#### И. test_set_credit_value_to_nonexistent_account (негативный)
* Цель: проверить, что нельзя поставить значение кредита для накопительного счета
* Входные данные: Bank("MyBank")
* Ожидаемый результат: set_account_balance("1", 1000) вызывает IndexError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### И. test_apply_interest_to_credit (позитивный)
* Цель: проверить, что можно применить начисление процентов для кредитного счета
* Входные данные: Bank("MyBank"), create_account("1", "credit", 100, 20), set_account_credit_value("1", 200), apply_interest_to_account("1")
* Ожидаемый результат: get_account_balance("1"): 80
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.

#### И. test_apply_interest_to_debit (позитивный)
* Цель: проверить, что можно применить начисление процентов для накопительного счета
* Входные данные: Bank("MyBank"), create_account("1", "debit", 100, 20), apply_interest_to_account("1")
* Ожидаемый результат: get_account_credit_value("1"): 120
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.


#### И. test_apply_interest_to_nonexistent_account (негативный)
* Цель: проверить, что нельзя применить начисление процентов для несуществующего счета
* Входные данные: Bank("MyBank")
* Ожидаемый результат: set_account_credit_value("1", 1000) вызывает IndexError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.



#### И. test_apply_interest_to_all_accounts (позитивный)
* Цель: проверить, что можно начислить проценты по всем аккаунтам 
* Входные данные:
  1. Bank("MyBank"), create_account("1", "debit", 100, 20)
  2. Bank("MyBank"), create_account("2", "credit", 100, 10), set_account_credit_value("2", 200)
  3. Bank("MyBank"), create_account("3", "credit", 100, 10), set_account_credit_value("3", 100)
  4. Bank("MyBank"), create_account("4", "debit", 0, 10)
После чего вызывается apply_interest_to_all_accounts()
* Ожидаемый результат: 
  1. get_account_balance("1"): 120
  2. get_account_balance("2"): 90
  3. get_account_balance("3"): 100
  4. get_account_balance("4"): 120
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.


#### И. test_set_account_interest_rate (позитивный)
* Цель: проверить, что можно поменять значение процента
* Входные данные: Bank("MyBank"), create_account("1", "debit", 100, 20)
* Ожидаемый результат: get_account_interest_rate("1"): 123
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.


#### И. test_set_account_interest_rate_to_nonexistent_account (негативный)
* Цель: проверить, что нельзя поменять значение процента несуществующего аккаунта
* Входные данные: Bank("MyBank")
* Ожидаемый результат: set_account_interest_rate("1", 123) вызывает IndexError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.


#### И. test_delete_account (негативный)
* Цель: проверить, что можно удалить аккаунт.
* Входные данные: Bank("MyBank"), create_account("1", "debit", 100, 20)
* Ожидаемый результат: get_accounts_names() не содержит ключа-имени "1"
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.


#### И. test_delete_nonexistent_account (негативный)
* Цель: проверить, что нельзя удалить несуществующий аккаунт.
* Входные данные: Bank("MyBank")
* Ожидаемый результат: delete_account("1") вызывает IndexError
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.


#### И. test_get_accounts_names (негативный)
* Цель: проверить, что правильно выводится список имен всех счетов
* Входные данные: Bank("MyBank"), create_account("1", "debit", 100, 20), create_account("2", "debit", 100, 20), 
  create_account("3", "debit", 100, 20)
* Ожидаемый результат: get_accounts_names() вернет список \["1", "2", "3"\]
* Описание процесса: используется стандартный вызов функции с контролем возвращаемого значения.


## Аттестационное тестирование

#### А. test_apply_interest_several_times
* Цель: применить функцию начисления процентов к разным счетам в разные моменты времени. 
* Входные данные: bank = Bank("MyBank")
  1. create_account("1", "debit", 100, 20), apply_interest_to_all_accounts(), apply_interest_to_all_accounts()
  2. create_account("2", "credit", 100, 20), set_account_credit_value("2", 200), apply_interest_to_all_accounts(), 
     set_account_interest_rate("2", 100), apply_interest_to_all_accounts()
  3. create_account("3", "debit", 100, 20), apply_interest_to_all_accounts()
* Ожидаемый результат: get_account_balance:
  1. 144
  2. -40
  3. 120
* Описание процесса: вызывается последовательность функций.

#### А. test_delete_then_create_again_account
* Цель: создать счет с номером "1", удалить его, затем создать снова, при этом начисляя проценты в процессе, чтобы 
  проверить возможность создание аккаунта с тем же именем, что до удаления.
* Входные данные: create_account("1", "debit", 100, 20), create_account("2", "credit", 100, 20), 
  apply_interest_to_all_accounts(), delete_account("1"), create_account("1", "credit", 10, 10)
* Ожидаемый результат: 
1. get_account_balance("1"): 10
2. get_accounts_names(): \["2", "1"\]
* Описание процесса: вызывается последовательность функций.


#### А. test_poor_account
* Цель: начислить на счет проценты 10 раз подряд, чтобы проверить возможность работы с вещественными числами
* Входные данные: create_account("1", "debit", 100, 20), apply_interest_to_account("1") 20 раз
* * Ожидаемый результат: get_account_balance("1"): 3833.75999 
* Описание процесса: вызывается последовательность функций.