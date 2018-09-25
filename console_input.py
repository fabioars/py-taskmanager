from task import Task


class ConsoleInput:

    @staticmethod
    def new_task(tasks):
        return lambda t: tasks.add(Task(input('Type your task: ')))

    @staticmethod
    def list_task(tasks):
        return lambda t: print(tasks)

    @staticmethod
    def check_task(tasks):
        return lambda t: tasks.toggle_state(int(input('Number of the task to check: ')))
