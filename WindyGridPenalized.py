# the grid gets windy, meaning actions are not deterministic but stochastic
ACTIONS = ['U', 'D', 'R', 'L']
class WindyGrid:
    def __init__(self, rows, cols, start):
        self.rows = rows
        self.cols = cols
        self.pos = start

    def initialize(self, rewards, actions, probs):
        # rewards are a dict of (row, col): reward
        # actions should be a dict of (row, col): list of possible actions
        # probs should be a dictionary within dictionary ((1, 2): 'U'): {(0, 2): 0.5, (1, 3): 0.5}
        self.rewards = rewards
        self.actions = actions
        self.probs = probs

    def set_position(self, p):
        self.pos = p

    def get_position(self):
        return self.pos

    def is_terminal(self, p):
        return p not in self.actions
    
    def move(self, action):
        pos = self.pos

        next_state_probs = self.probs[(pos, action)]
        next_states = list(next_state_probs.keys())
        next_probs = list(next_state_probs.values())
        s2 = np.random.choice(next_states, p=next_probs)

        self.pos = s2
        return self.rewards.get(s2, 0)

    def game_over(self):
        return self.pos not in self.actions

    def all_states(self):
        return set(self.actions.keys()) | set(self.rewards.keys())

def get_windy_grid_penalized(step_cost=-.1):
    g = WindyGrid(3, 4, (2, 0))
    rewards = {
        (0, 0): step_cost,
        (0, 1): step_cost,
        (0, 2): step_cost,
        (1, 0): step_cost,
        (1, 2): step_cost,
        (2, 0): step_cost,
        (2, 1): step_cost,
        (2, 2): step_cost,
        (2, 3): step_cost,
        (0, 3): 1.0,
        (1, 3): -1.0
    }

    actions = {
        (0, 0): ('D', 'R'),
        (0, 1): ('L', 'R'),
        (0, 2): ('L', 'D', 'R'),
        (1, 0): ('U', 'D'),
        (1, 2): ('U', 'D', 'R'),
        (2, 0): ('U', 'R'),
        (2, 1): ('L', 'R'),
        (2, 2): ('L', 'R', 'U'),
        (2, 3): ('L', 'U')
    }

    probs = {
        ((2, 0), 'U'): {(1, 0): 1.0},
        ((2, 0), 'D'): {(2, 0): 1.0},
        ((2, 0), 'L'): {(2, 0): 1.0},
        ((2, 0), 'R'): {(2, 1): 1.0},
        ((1, 0), 'U'): {(0, 0): 1.0},
        ((1, 0), 'D'): {(2, 0): 1.0},
        ((1, 0), 'L'): {(1, 0): 1.0},
        ((1, 0), 'R'): {(1, 0): 1.0},
        ((0, 0), 'U'): {(0, 0): 1.0},
        ((0, 0), 'D'): {(1, 0): 1.0},
        ((0, 0), 'L'): {(0, 0): 1.0},
        ((0, 0), 'R'): {(0, 1): 1.0},
        ((0, 1), 'U'): {(0, 1): 1.0},
        ((0, 1), 'D'): {(0, 1): 1.0},
        ((0, 1), 'L'): {(0, 0): 1.0},
        ((0, 1), 'R'): {(0, 2): 1.0},
        ((0, 2), 'U'): {(0, 2): 1.0},
        ((0, 2), 'D'): {(1, 2): 1.0},
        ((0, 2), 'L'): {(0, 1): 1.0},
        ((0, 2), 'R'): {(0, 3): 1.0},
        ((2, 1), 'U'): {(2, 1): 1.0},
        ((2, 1), 'D'): {(2, 1): 1.0},
        ((2, 1), 'L'): {(2, 0): 1.0},
        ((2, 1), 'R'): {(2, 2): 1.0},
        ((2, 2), 'U'): {(1, 2): 1.0},
        ((2, 2), 'D'): {(2, 2): 1.0},
        ((2, 2), 'L'): {(2, 1): 1.0},
        ((2, 2), 'R'): {(2, 3): 1.0},
        ((2, 3), 'U'): {(1, 3): 1.0},
        ((2, 3), 'D'): {(2, 3): 1.0},
        ((2, 3), 'L'): {(2, 2): 1.0},
        ((2, 3), 'R'): {(2, 3): 1.0},
        ((1, 2), 'U'): {(0, 2): 0.5, (1, 3): 0.5},
        ((1, 2), 'D'): {(2, 2): 1.0},
        ((1, 2), 'L'): {(1, 2): 1.0},
        ((1, 2), 'R'): {(1, 3): 1.0}
    }
    g.initialize(rewards, actions, probs)
    return g