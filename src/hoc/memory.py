class Memory:
    def __init__(self) -> None:
        self.array = []
        self.color = ""

    def check_memory(self) -> None:
        self.array = (lambda array: array[2:] if len(array) > 4 else array)(self.array)

    def check_price(self) -> str:
        if len(self.array) > 1:
            if self.array[-1] > self.array[-2]:
                self.color = "bold white on green"
            elif self.array[-1] < self.array[-2]:
                self.color = "bold white on red"
        elif len(self.array) == 1:
            self.color = "bold white on green"

        return self.color
        