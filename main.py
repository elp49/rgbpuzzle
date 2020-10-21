import rgb
import agent
import util

if __name__ == '__main__':
    cmd = util.get_arg(1)
    if cmd:
        state = rgb.State(util.get_arg(2))
        if cmd == 'random':
            # Generate list of N states
            states = agent.Agent.random_walk(state, 8)

            # Print resulting sequence of states.
            util.pprint(states)