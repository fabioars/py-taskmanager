
class Task:
    def __init__(self, name, is_done=False):
        self.name = name
        self.is_done = is_done

    def __str__(self):
        return "[%s] %s\n" % (self.is_done, self.name)


class TaskList:
    def __init__(self):
        self.list = []

    def add(self, task):
        self.list.append(task)

    def remove(self, pos):
        self.list.remove(self.list[pos])

    def toggle_state(self, pos):
        item = self.list[pos]
        state = item.is_done
        self.list[pos].is_done = not state

    def __str__(self):
        size = len(self.list)
        subtotal = "%s items: \n\n" % size

        for task in self.list:
            subtotal += "%s\n" % task

        return subtotal
