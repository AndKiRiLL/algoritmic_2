#Объявляем класс BankAccount
class BankAccount:

    # Инициализируем переменные
    def __init__(self, full_name, balance):
        self.full_name = full_name
        self.balance = balance
        self.account_transactions = []

    # Метод получения информации
    def get_info(self):
        print('Информация о клиенте:')
        print(f'Полное имя: {self.full_name}')
        print(f'Баланс: {self.balance} руб.')

    # Метод получения истории операций со счётом
    def get_account_transactions(self):
        print('История операций со счётом:')
        for i in range(0, len(self.account_transactions)):
            print(f'{i+1}. {self.account_transactions[i]}')

    # Метод Пополнения баланса
    def replenish_balance(self, quantity):
        print(f'На ваш баланс поступило {quantity} руб.')
        self.account_transactions.append(f'На ваш баланс поступило {quantity} руб.')
        print(f'Ваш баланс после операции: {self.balance} + {quantity} = {self.balance + quantity}')
        self.balance += quantity

    # Метод Снятия баланса
    def withdrawal_balance(self, quantity):
        print(f'С вашего баланса снято {quantity} руб.')
        self.account_transactions.append(f'С вашего баланса снято {quantity} руб.')
        print(f'Ваш баланс после операции: {self.balance} - {quantity} = {self.balance - quantity}')
        self.balance -= quantity


# Задаём класс BankAccount в переменную ba
ba = BankAccount('Andriyanov Kirill', 15000)

# получаем информацию
ba.get_info()
print()

# пополняем счёт на 5000 руб
ba.replenish_balance(5000)
print()

# снимаем со счёта 2500
ba.withdrawal_balance(2500)
print()

# Получаем историю операций со счётом
ba.get_account_transactions()