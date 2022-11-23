# Create a GridWorld for the agent to move in
class Grid:
    # 0, 0 top left
    def __init__(self, rows, cols, start):
        self.rows = rows
        self.cols = cols
        self.start= start
    
    def set(self, rewards, actions):
        # rewards: dictionary of type (i, j) - reward
        # actions = dictionary of type (m, n) - action list
        self.rewards = rewards
        self.actions = actions

    def set_state(self, s):
        self.i = s[0]
        self.j = s[1]

    def is_terminal(self, s):
        return s not in self.actions

    def get_next_state(self, a, s):
        i, j = s[0], s[1]
        if a in self.actions[(i, j)]:
            if a == 'U':
                i -= 1
            elif a == 'D':
                i += 1
            elif a == 'R':
                j += 1
            elif a == 'L':
                j -= 1
        return i, j

    def current_state(self):
        return (self.i, self.j)

    def move(self, action):
        if action in self.actions[(self.i, self.j)]:
            newI, newJ = self.get_next_state(action, (self.i, self.j))
            self.i = newI
            self.j = newJ
        return self.rewards.get((self.i, self.j), 0)
    
    def game_over(self):
        return (self.i, self.j) not in self.actions

    def all_states(self):
        return set(self.actions.keys()) | set(self.rewards.keys())

    def reset(self):
        # put agent back in start position
        self.i = 2
        self.j = 0
        return (self.i, self.j)

ACTIONS = ['U', 'D', 'L', 'R']

def get_standard_grid():
    g = Grid(3, 4, (2, 0))
    rewards = {(0, 3): 1.0, (1, 3): -1.0}
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

    g.set(rewards, actions)
    return g

def get_negative_grid(step_cost=-0.1):
    g = get_standard_grid()
    g.rewards.update({
        (0, 0): step_cost,
        (0, 1): step_cost,
        (0, 2): step_cost,
        (1, 0): step_cost,
        (1, 2): step_cost,
        (2, 0): step_cost,
        (2, 1): step_cost,
        (2, 2): step_cost,
        (2, 3): step_cost,
    })
    return g
    