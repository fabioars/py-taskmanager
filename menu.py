
class Menu:
    def __init__(self):
        self.items = []
        self.add(MenuItem("Exit", lambda l: exit(0)))

    def add(self, item):
        self.items.append(item)

    def call(self, pos):
        self.items[pos].call()

    def __str__(self):
        subtotal = ""

        for i, item in enumerate(self.items):
            subtotal += "[%i] %s\n" % (i, item)

        return subtotal


class MenuItem:
    def __init__(self, label, callback):
        self.label = label
        self.callback = callback

    def call(self):
        self.callback(self.label)

    def __str__(self):
        return self.label

