#Task №1 
class CyclicIterator:
    def __init__(self, container):
        self.container = container
        self.iterator = iter(container)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                print(next(self.iterator))
            except StopIteration:
                self.iterator = iter(self.container)

cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)

