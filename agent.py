import random

class Node:

    def __init__(self, state, parent):
        self.state = state
        self.parent = parent


class Agent:

    @staticmethod
    def random_walk(state, n):
        '''Does a random walk through the state space.'''
        # Initialize node.
        node = Node(state, None)

        # Repeat random walk until N states have been visited.
        for i in range(n):
            # Generate all the possible next states from current state.
            actions = node.state.actions()

            # Select a random possible state.
            rand_i = random.randrange(0, len(actions))

            # Clone state and execute action.
            next_state = node.state.clone()
            next_state.execute(actions[rand_i])

            # Build node.
            node = Node(next_state, node)

        # Use final node to generate list of N states visited on random walk.
        visited = []
        while node is not None:
            visited.append(node.state)
            node = node.parent

        # Return list of N states visited.
        return visited