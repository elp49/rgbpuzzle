import rgb
import agent
import util

def heuristic():
    return 0

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
            heuristic = heuristic()
            my_agent.a_star(state, heuristic)