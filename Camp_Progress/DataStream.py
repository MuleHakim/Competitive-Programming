class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.countOfNumEqualValue = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.countOfNumEqualValue += 1
        else:
            self.countOfNumEqualValue = 0
        if self.countOfNumEqualValue >= self.k:
            return True
        return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)