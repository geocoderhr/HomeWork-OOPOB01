class Task:
    def __init__(self, description, due_date, completed=False):

        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_completed(self):
        """Помечает задачу как выполненную."""
        self.completed = True

    def __str__(self):
        """Возвращает строковое представление задачи."""
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"


# Создаём список задач
tasks = []

# Прямой вызов конструктора для создания задач
task1 = Task("Приготовить ужин", "2025-03-25")
task2 = Task("Сходить в магазин", "2025-03-24")
task3 = Task("Позвонить маме", "2025-03-23")

# Добавляем задачи в список
tasks.append(task1)
tasks.append(task2)
tasks.append(task3)

# Отмечаем задачу task2 как выполненную
task2.mark_completed()


# Функция для вывода всех не выполненных задач
def list_current_tasks(task_list):
    print("Текущие задачи (не выполненные):")
    for task in task_list:
        if not task.completed:
            print(task)


# Выводим список текущих задач
list_current_tasks(tasks)
