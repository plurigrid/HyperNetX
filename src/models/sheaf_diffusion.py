class SheafDiffusion:
    def __init__(self, initial_condition):
        self.state = initial_condition

    def update_state(self, delta_F):
        self.state = self.state - delta_F * self.state