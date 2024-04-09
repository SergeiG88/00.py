class EvenNumbers:
    def __init__(self, start=0, end=1, step=0):
        self.start = start
        self.end = end
        self.step = step


    def __iter__(self):
        self.value = self.start - self.step
        return self


    def __next__(self):
        if self.value + self.step < self.end:
            self.value += self.step

            return self.value
        else:
            raise StopIteration()


en = EvenNumbers(10, 25, 2)
for i in en:
    print(i)