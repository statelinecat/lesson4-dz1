# Менеджер задач
#
# Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты:
# описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.





class Task:
    def __init__(self, description, due_date, status):
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_done(self):
        """Отмечает задачу как выполненную."""
        self.status = "выполнена"

    # @classmethod
    # def add_task(self, description, due_date):
    #
    #     self.description = input('Введите описание задачи: ')
    #     self.due_date = input('Введите срок выполнения задачи: ')




def task_manage(tasks):
    doit = ''
    current_tasks = [task for task in tasks if task.status == "не выполнена"]
    # print("Текущие задачи:")
    # if len(current_tasks) < 1:
    #     print('Текущих задач нет')
    # else:
    #     for task in current_tasks:
    #         print(f"- Описание: {task.description}, Срок: {task.due_date}, Статус: {task.status}")
    while doit != '0':
        current_tasks = [task for task in tasks if task.status == "не выполнена"]
        doit = input(f"Для добавления новой задачи введите 1 \nДля отметки о выполнении задачи введите 2 \n"
                 f"Для вывода списка задач на экран введите 3 \nДля выхода введите 0: ")
        match doit:
            case '1':
                description = input('Введите описание задачи: ')
                due_date = input('Введите срок выполнения задачи: ')
                status = "не выполнена"
                new_task = Task(description, due_date, status)
                current_tasks.append(new_task)
            case '2':
                completed_task = input('Введите описание выполненной задачи: ')
                for task in current_tasks:
                    if task.description == completed_task:
                        task.status = 'выполнена'
            case '3':
                print("Текущие задачи:")
                if len(current_tasks) < 1:
                    print('Текущих задач нет')
                else:
                    for task in current_tasks:
                        print(f"- Описание: {task.description}, Срок: {task.due_date}, Статус: {task.status}")






tasks = []

task_manage(tasks=tasks)
