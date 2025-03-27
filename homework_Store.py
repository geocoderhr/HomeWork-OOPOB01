# Класс Store для управления магазинами
class Store:
    def __init__(self, name: str, address: str):
        """
        Конструктор. Инициализирует название, адрес и пустой словарь для товаров.
        """
        self.name = name
        self.address = address
        self.items = {}  # Словарь товаров, например: {'apples': 0.5, 'bananas': 0.75}

    def add_item(self, item_name: str, price: float):
        """
        Добавляет товар в ассортимент.
        :param item_name: название товара
        :param price: цена товара
        """
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name: str):
        """
        Удаляет товар из ассортимента.
        :param item_name: название товара для удаления
        """
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удалён.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def get_price(self, item_name: str):
        """
        Возвращает цену товара по его названию.
        :param item_name: название товара
        :return: цена товара или None, если товар не найден
        """
        return self.items.get(item_name)

    def update_price(self, item_name: str, new_price: float):
        """
        Обновляет цену товара.
        :param item_name: название товара
        :param new_price: новая цена товара
        """
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден для обновления цены.")

# Создаём несколько объектов класса Store

# Магазин свежих продуктов
store1 = Store("Fresh Mart", "ул. Ленина, 10")
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

# Магазин техники
store2 = Store("Tech Hub", "пр. Мира, 25")
store2.add_item("laptops", 999.99)
store2.add_item("smartphones", 499.99)

# Книжный магазин
store3 = Store("Book Nook", "ул. Пушкина, 5")
store3.add_item("novels", 15.0)
store3.add_item("magazines", 5.0)

# Тестирование методов на магазине Fresh Mart
print("Цена яблок:", store1.get_price("apples"))  # Должно вывести 0.5
store1.update_price("apples", 0.6)  # Обновляем цену яблок
print("Обновлённая цена яблок:", store1.get_price("apples"))  # Должно вывести 0.6
store1.remove_item("bananas")  # Удаляем товар "bananas"
print("Товары в Fresh Mart:", store1.items)
