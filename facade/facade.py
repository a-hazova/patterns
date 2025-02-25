class Balance:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        print(f'Сумма {amount} успешно зачислена на счет. Новый баланс {self.balance}')
    
    def withdraw(self, amount):
        if amount > self.balance:
            print('Запрашиваемая сумма меньше баланса счета')
        else:
            self.balance -= amount
            print(f'Сумма {amount} успешно снята со счета. Остаток на счете {self.balance}')

    def check_balance(self):
        print(f'Текущий баланс счета: {self.balance}')

class Pizza:
    price = {
        'cheese': 50,
        'pepperoni': 60,
        'ham': 70,
        'onion': 30,
        'mushrooms': 40,
        'tomatoes': 20,
        'cheese': 50,
    }

    def __init__(self, ingredients: list):
        self.ingredients = ingredients
    
    def get_total_price(self):
        return sum(self.price[ingredient] for ingredient in self.ingredients)

class Customer:
    def __init__(self, name: str):
        self.name = name
        self.balance = Balance()
        self.total_price = 0
    
    def order_pizza(self, ingredients: list):
        pizza = Pizza(ingredients)
        self.total_price += pizza.get_total_price()
        print (f'Заказ на сумму {pizza.get_total_price()} оформлен на имя {self.name}. Общая сумма: {self.total_price}')
    
    def deposit(self, amount):
        self.balance.deposit(amount)
    def buy(self):
        if self.balance.balance >= self.total_price:
            self.balance.withdraw(self.total_price)
            print(f'Заказ оплачен. Общая сумма заказа: {self.total_price}')
        else:
            print(f'{self.name} не хватает {self.balance.balance - self.total_price} для оплаты заказа. Пополните счет')

if __name__ == "__main__":
    customer = Customer('John Doe')
    customer.deposit(1000)
    customer.order_pizza(['cheese', 'pepperoni', 'ham'])
    customer.order_pizza(['cheese', 'pepperoni', 'ham', 'onion', 'mushrooms', 'tomatoes'])
    customer.buy()
    