import rgb
import agent
import util

def heuristic(state):
    '''The evalutation function for A* search - '''
    h = 0
    for x in range(state.size):
        for y in range(state.size):
            c = state.get(x, y)
            if c != rgb.Cell.EMPTY:
                deltas = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
                for dx, dy in deltas:
                    x2, y2 = x+dx, y+dy
                    c2 = state.get(x2, y2)
                    if c == c2:
                        h += 1
    return h

if __name__ == '__main__':
    cmd = util.get_arg(1)
    if cmd:
        state = rgb.State(util.get_arg(2))
        my_agent = agent.Agent()

        if cmd == 'random':
            # Generate and print list of N visited states.
            visited_states = my_agent.random_walk(state, 8)
            util.pprint(visited_states)

        elif cmd == 'bfs':
            my_agent.bfs(state)

        elif cmd == 'dfs':
            my_agent.dfs(state)

        elif cmd == 'a_star':
            my_agent.a_star(state, heuristic)