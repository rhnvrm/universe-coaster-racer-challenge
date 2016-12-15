import gym
import universe

env = gym.make('flashgames.CoasterRacer-v0')
env.configure(remotes='vnc://localhost:5900+15900')
observation_n = env.reset()

while True:
    action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n]
    for ob in observation_n:
        print ob
        pass
    observation_n, reward_n, done_n, info = env.step(action_n)
    env.render()
