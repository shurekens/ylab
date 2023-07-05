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

#Task №2
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple

@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        list = []
        for element in self.dates:
            date = element[0]
            while date <= element[1]:
                yield(date)
                date += timedelta(1)

m = Movie('sw', [
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule():
    print(d)
