class Stats:
    """tracking statistics (lifes, mistakes)"""

    def __init__(self):
        """inicialization statistics"""
        self.score = 0
        high_score = 0
        self.persons_life = 2

        self.reset_stats()
        self.run_game = True

        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """stats changes in real-time"""
        self.persons_life = 2
        self.score = 0

    def update_tick(self, value):
        self.score = value
