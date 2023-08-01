class Pizza:
    def __init__(self, name, price, toppings=[]):
        self.name = name
        self.price = price
        self.toppings = toppings

    def add_topping(self, topping):
        self.toppings.append(topping)

    def remove_topping(self, topping):
        self.toppings.remove(topping)

    def get_price(self):
        return self.price + sum([topping.price for topping in self.toppings])


class Topping:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Menu:
    def __init__(self, pizzas=[]):
        self.pizzas = pizzas

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)


class Order:
    def __init__(self, pizzas=[], payment_method='наличные'):
        self.pizzas = pizzas
        self.payment_method = payment_method

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def get_total_price(self):
        return sum([pizza.get_price() for pizza in self.pizzas])


class Sales:
    def __init__(self, sales=[], profit=0):
        self.sales = sales
        self.profit = profit

    def add_sale(self, sale):
        self.sales.append(sale)
        self.profit += sale.get_total_price()

    def get_profit(self):
        return self.profit


def run_pizzeria():
    menu = Menu([
        Pizza('Маргарита', 100),
        Pizza('Пепперони', 120),
        Pizza('Веганская', 120),
        Pizza('Гавайская', 130),
        Pizza('Мясная', 150)
    ])

    order = Order()

    sales = Sales()

    while True:
        print('1 - Показать пицы')
        print('2 - Заказать пиццу')
        print('3 - Показать отчет о продажах')
        print('4 - Выйти')
        choice = input('Ваш выбор: ')

        if choice == '1':
            print('Меню:')
            for pizza in menu.pizzas:
                print(f'{pizza.name} - ${pizza.price}')

        elif choice == '2':
            print('Доступные пиццы:')
            for i, pizza in enumerate(menu.pizzas):
                print(f'{i + 1}. {pizza.name} - ${pizza.price}')

                pizza_choice = input('Введите номер пиццы или название: ')

                if pizza_choice.isnumeric():
                    pizza_index = int(pizza_choice) - 1
                    if pizza_index in range(len(menu.pizzas)):
                        pizza = menu.pizzas[pizza_index]
                    else:
                        print('Некорректный номер.')
                        continue
                else:
                    pizza_name = pizza_choice
                    pizza_price = input('Введите цену пиццы: ')
                    toppings_choice = input('Введите топпинг, через запятую: ')
                    toppings = []
                    for topping_name in toppings_choice.split(','):
                        topping_price = input(f'Введите цену для {topping_name}: ')
                        topping = Topping(topping_name.strip(), float(topping_price))
                        toppings.append(topping)
                    pizza = Pizza(pizza_name, float(pizza_price), toppings)

                order.add_pizza(pizza)

                print('Топпинг:')
                for i, topping in enumerate(pizza.toppings):
                    print(f'{i + 1}. {topping.name} - ${topping.price}')

                payment_choice = input('Введите способ оплаты (наличные или карта): ')
                order.payment_method = payment_choice

                sales.add_sale(order)

                print('Заказ:')
                for pizza in order.pizzas:
                    print(f'{pizza.name} - ${pizza.get_price()}')

                print(f'Цена: ${order.get_total_price()}')

                order = Order()

        elif choice == '3':
            print(f'Общий объем продаж: ${sales.get_profit()}')
            print('Отчет о продажах:')
            for sale in sales.sales:
                print(f'Итоговая цена: ${sale.get_total_price()}')
                for pizza in sale.pizzas:
                    print(f'{pizza.name} - ${pizza.get_price()}')
            with open('order.txt', 'w') as f:
                f.write(f'Отчет о продажах: \n'
                        f'Итог: {sale.get_total_price()}')
        elif choice == '4':
            break
        else:
            print('Некорректный выбор.')

if __name__ == '__main__':
    run_pizzeria()
