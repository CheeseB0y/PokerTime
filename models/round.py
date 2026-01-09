class Round:
    """
    Round object

    Games will be stored as an array of round objects
    """

    def __init__(self, num, time=0, s_blind=0, b_blind=0):
        self.num = num
        self.time = time
        self.s_blind = s_blind
        self.b_blind = b_blind

    def __str__(self):
        return f"Round: {self.num}\nTime: {self.time}\nSmall Blind: {self.s_blind}\nBig Blind: {self.b_blind}"
