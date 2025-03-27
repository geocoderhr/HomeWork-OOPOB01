class Store:
    def __init__(self, name,address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self,item_name,price):
        self.items[item_name] = price
        print(f"Товар {item_name} - был добавлен в {self.name}")

    def remove_item(self,item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} - удален из {self.name}")

    def get_price(self,item_name):
        return self.items.get(item_name)


    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

            print(f"Цена на товар {item_name}  была обновлена в {self.name}")
        else:
            print(f"Товар не найден в {self.name}")

    def info(self):
        print(f"Доступные товары в магазине {self.name}:")
        # Проходим по ключам словаря items и выводим название товара и его цену
        for item_name, price in self.items.items():
            print(f"{item_name} - {price}")


store1 = Store("Bikes", "Limido dele Roje 16")
store2 = Store("Bicycle parts", "Goranska 35")
store3 = Store("Bicycle tours", "Goranska 35/A")

store1.add_item("<Bike EL IStra>", 1000)
store1.add_item("<Bike EL Endurance>", 1350)
store1.add_item("<Bike EL Sport>", 1600)

store1.remove_item("<Bike EL IStra>")

store1.add_item("<Bike EL IStra>", 1450)
store1.update_price("<Bike EL Endurance>", 1500)

print(store1.get_price("<Bike EL Endurance>"))

store1.info()





