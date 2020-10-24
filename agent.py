import random
import util


class Node:

    def __init__(self, state, parent):
        self.state = state
        self.parent = parent


class Agent:

    def random_walk(self, state, n):
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

    def _search(self, state, pop_i, heuristic=None):
        '''This function encapsulates the common base algorithm among Bread-
        First search, Depth-First search, and A* search.'''
        closed = []
        node = Node(state, None)

        # Test if current node is solution state.
        if node.state.is_goal():
            return node

        fringe = [node]
        while fringe:
            # Remove node from fringe.
            node = fringe.pop(pop_i)

            # For each possible action on this state.
            for action in node.state.actions():
                # Clone the current state and execute this action on it.
                clone = node.state.clone()
                clone.execute(action)

                # Test if state is new and has not already been found.
                if self.is_new(clone, closed, fringe):
                    # Append child node to fringe.
                    child = Node(clone, node)
                    fringe.append(child)
                    
                    # Display new state.
                    self.print_path(clone)

                    # Test if clone is solution state.
                    if clone.state.is_goal():
                        return child

            # Append current node to closed list.
            closed.append(node)

        # If no solution state was foundreturn None to indicate failure.
        return None

    def is_new(self, state, closed=[], fringe=[]):
        for c in closed:
            if state.__eq__(c.state):
                return False
        
        for c in fringe:
            if state.__eq__(c.state):
                return False

        return True

    def print_path(self, node):
        path = []
        n = node

        # Generate list of states in path.
        while n is not None:
            path.append(n.state)
            n = n.parent
            
        # Print path starting at initial state.
        for state in reversed(path):
            util.pprint(state)

        print(len(path))

    def bfs(self, state):
        return self._search(state, 0)

    def dfs(self, state):
        return self._search(state, -1)

    def a_star(self, state, heuristic):
        return self._search(state, 0, heuristic)
