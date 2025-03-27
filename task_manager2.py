class Task:
    def __init__(self):
        self.tasks = []  # Список задач

    def add_task(self, deadline, description):
        # Добавляем задачу с заданным сроком, описанием и статусом "не выполнено"
        self.tasks.append({
            "deadline": deadline,
            "description": description,
            "status": "не выполнено"
        })

    def complete_task(self, description):
        # Находим задачу по описанию и отмечаем её как выполненную
        found = False
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = "выполнено"
                print(f"Задача '{description}' выполнена.")
                found = True
                break
        if not found:
            print(f"Задача '{description}' не найдена.")

    def show_tasks(self):
        # Выводим только задачи со статусом "не выполнено"
        print("Текущие задачи:")
        for task in self.tasks:
            if task["status"].lower() == "не выполнено":
                print(f"{task['description']} - {task['deadline']}")

# Создаем объект класса Task (вызов конструктора)
t = Task()

# Добавляем задачи
t.add_task("27.03.2025", "Приготовить обед.")
t.add_task("28.03.2025", "Съездить на природу.")
t.add_task("01.04.2025", "Смазать велосипед.")

# Выводим текущие задачи
t.show_tasks()

# Отмечаем задачу как выполненную
t.complete_task("Приготовить обед.")


t.show_tasks()


t.complete_task("Съездить на природу.")
t.show_tasks()
