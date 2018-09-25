from menu import Menu, MenuItem
from task import Task, TaskList
from console_input import ConsoleInput
class App:
    def __init__(self):
        self.menu = Menu()
        self.tasks = TaskList()
        self.bootstrap()

    def bootstrap(self):
        self.menu.add(MenuItem('New Task', ConsoleInput.new_task(self.tasks)))
        self.menu.add(MenuItem('List Task', ConsoleInput.list_task(self.tasks)))
        self.menu.add(MenuItem('Check Task', ConsoleInput.check_task(self.tasks)))

        print(self.menu)

    def start(self):
        option = -1

        while True:
            option = int(input("Type an option: "))
            self.menu.call(option)
            print(self.menu)
