import random

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

    def _search(self, fringe, heuristic=None):
        '''This function encapsulates the common base algorithm among Bread-
        First search, Depth-First search, and A* search.'''


    def bfs(self, state):
        closed_nodes = []

        # Store initial node in open node list.
        open_nodes = [Node(state, None)]

        # For each open node.
        while len(open_nodes) > 0:
            current_node = open_nodes[0]

            # Test if current node is solution state.
            if current_node.state.is_goal():
                break

            # Generate all possible next states from this node.
            actions = current_node.state.actions()

            # For each possible action on this state.
            for a in actions:
                # Clone the current state.
                clone_state = current_node.state.clone()

                # Execute this action on clone.
                clone_state.execute(a)

                #TODO: should it check here if this is also goal before pushing to back of open?

                # Create child node and append to open node list.
                child_node = Node(clone_state, current_node)
                open_nodes.append(child_node)

            # Remove closed node from open node list and append to closed list.
            closed = open_nodes.pop(0)
            closed_nodes.append(closed)

        return current_node
    

    def dfs(self, state):
        return ''

    

    def a_star(self, state, heuristic):
        return ''

    