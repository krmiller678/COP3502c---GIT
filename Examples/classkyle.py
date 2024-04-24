class Kyle:

    def __init__(self):
        Kyle.height = 1
        self.number = 7


if __name__ == '__main__':
    kyle = Kyle()
    print(kyle.height)
    print(Kyle.height)
    kyle.height = 9
    Kyle.height = 10
    print(kyle.height)
    print(Kyle.height)