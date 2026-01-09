class GameState:
    """
    Keeps track of what round it is and the blinds
    Use for reference in other classes so there is no mixup
    """

    def __init__(self, rounds):
        self.rounds = rounds
        self.round_index = 0
        self.round_num = self.rounds[self.round_index].num
        self.time = self.rounds[self.round_index].time
        self.s_blind = self.rounds[self.round_index].s_blind
        self.b_blind = self.rounds[self.round_index].b_blind

    def next_round(self):
        """
        Increment round counter and update values

        Args:
            None

        Returns:
            None
        """
        if len(self.rounds) > self.round_index + 1:
            self.round_index += 1
        self.round_num = self.rounds[self.round_index].num
        self.time = self.rounds[self.round_index].time
        self.s_blind = self.rounds[self.round_index].s_blind
        self.b_blind = self.rounds[self.round_index].b_blind

    def restart_game(self):
        """
        Set round counter to zero and update values

        Args:
            None

        Returns:
            None
        """
        self.round_index = 0
        self.round_num = self.rounds[self.round_index].num
        self.time = self.rounds[self.round_index].time
        self.s_blind = self.rounds[self.round_index].s_blind
        self.b_blind = self.rounds[self.round_index].b_blind

    def update_rounds(self, rounds):
        """
        Update round values when a change is made in the game editor

        Args:
            rounds (arr[Round]): New rounds to be applied to the GameState instance

        Returns:
            None
        """
        self.rounds = rounds
        self.round_index = min(self.round_index, len(rounds) - 1)
        self.round_num = self.rounds[self.round_index].num
        self.time = self.rounds[self.round_index].time
        self.s_blind = self.rounds[self.round_index].s_blind
        self.b_blind = self.rounds[self.round_index].b_blind
