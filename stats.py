class Stats():
    """tracking statistics (lifes, mistakes)"""

    def __init__(self):
        """inicialization statistics"""

        self.reset_stats()
        self.run_game = True
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.readline())


    def reset_stats(self):
        """stats changes in real-time"""

        self.persons_life = 2
        self.score = 0

