import random
import util


class Node:

    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.value = None


class Agent:

    def __init__(self):
        self.node = None
        self.fringe = []
        self.closed = []

    def random_walk(self, state, n):
        '''Perfroms a random walk through the state space.'''
        self.node = Node(state, None)

        # Repeat random walk until N states have been visited.
        for i in range(n):
            # Generate all the possible next states from current state.
            actions = self.node.state.actions()

            # Select a random possible state.
            rand_i = random.randrange(0, len(actions))

            # Clone state and execute action.
            next_state = self.node.state.clone()
            next_state.execute(actions[rand_i])

            self.node = Node(next_state, self.node)

        # Use final node to generate list of N states visited on random walk.
        visited = []
        while self.node is not None:
            visited.append(self.node.state)
            self.node = self.node.parent

        # Return list of N states visited.
        return visited

    def bfs(self, state):
        '''Performs a Breadth-First search starting at the given state.'''
        return self._search(state)

    def dfs(self, state):
        '''Performs a Depth-First search starting at the given state.'''
        return self._search(state, -1)

    def a_star(self, state, heuristic):
        '''Performs an A* search starting at the given state and uses a 
        evaluation function.'''
        return self._search(state, heuristic=heuristic)

    def _search(self, state, pop_i=0, heuristic=None):
        '''This function encapsulates the common base algorithm among Bread-
        First, Depth-First, and A* search.'''
        if state is None:
            raise ValueError('Initial state cannot be None.')

        self.node = Node(state, None)
        self.fringe = [self.node]

        # Test if initial state is solution.
        if state.is_goal():
            self.print_path()
            self.print_num_paths_explored()
            return self.node

        while self.fringe:
            # Set current node and print its path.
            self.node = self.fringe[pop_i]
            self.print_path()
            
            # Expand current node.
            for action in self.node.state.actions():
                # Get result state of action.
                child = self.child(action)
                if child is not None:
                    self.fringe.append(child)

                    # Test if child has solution state.
                    if child.state.is_goal():
                        self.node = child
                        self.print_path()
                        self.print_num_paths_explored()
                        return child

                    # Test if heuristic is given.
                    if heuristic is not None:
                        self.fringe[-1].value = heuristic(self.fringe[-1].state)

            # Move current node from fringe to closed.
            self.fringe.remove(self.node)
            self.closed.append(self.node)
            
            # Test if heuristic is given.
            if heuristic is not None:
                self.sort_fringe_by_value(pop_i)

        # If no solution state was found, return None to indicate failure.
        print('Failure, no solution found.')
        return None

    def child(self, action):
        '''Executes action on current state and returns child node of resulting
        state or None if it has already been visited.'''
        # Clone the current state and execute this action on it.
        clone = self.node.state.clone()
        clone.execute(action)

        # Test if state has already been visited.
        for n in self.closed:
            if clone.__eq__(n.state):
                return None
        
        for n in self.fringe:
            if clone.__eq__(n.state):
                return None

        return Node(clone, self.node)

    def sort_fringe_by_value(self, pop_i):
        '''Finds the node with the lowest value and moves it to the location in
        fringe that the _search function expects the next node to expand to be.'''
        min_index = 0
        min_value = self.fringe[0].value

        # Find node with lowest value.
        for i in range(1, len(self.fringe)):
            # Test if node has lower value than min.
            if self.fringe[i].value < min_value:
                min_index = i
                min_value = self.fringe[i].value

        # Swap node with lowest value and node at index pop_i.
        if self.fringe[pop_i].value > min_value:
            self.swap(self.fringe, pop_i, min_index)

    def swap(self, mylist, i1, i2):
        '''Swap two items in a list.'''
        size = len(mylist)
        if size <=1 or i1 < 0 or i1 >= size or i2 < 0 or i2 >= size:
            return

        temp = mylist[i1]
        mylist[i1] = mylist[i2]
        mylist[i2] = temp

    def print_path(self):
        '''Pretty print the path to current node.'''
        path = []
        n = self.node

        # Generate list of states in path.
        while n is not None:
            path.append(n.state)
            n = n.parent
            
        # Print path starting at initial state.
        path.reverse()
        util.pprint(path)

    def print_num_paths_explored(self):
        print(len(self.closed) + len(self.fringe))
