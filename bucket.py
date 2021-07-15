class Bucket:
    def __init__(self, maximum=10 ** 5) -> None:
        self.maximum = maximum
        self.origin = []
        self.bucket = [0] * maximum

    def append(self, value: int) -> None:
        self.origin.append(value)
        self.bucket[value] += 1

    def append_list(self, list: list) -> None:
        for value in list:
            self.origin.append(value)
            self.bucket[value] += 1

    def sorted(self) -> list:
        cum = []

        for i in range(self.maximum):
            if i == 0:
                cum.append(self.bucket[0])
            else:
                cum.append(self.bucket[i] + cum[i-1])

        result = [None] * len(self.origin)

        for value in self.origin:
            index = cum[value] - 1
            result[index] = value

            if self.bucket[value] > 1:
                cum[value] -= 1

        return result
