import gym
import universe
import random

env = gym.make('flashgames.CoasterRacer-v0')

# Instead of connecting to created docker remote
# Prefering to use always-on docker cont. to reduce
# time taken between each code prototype due to 
# redownloading of flash files
env.configure(remotes='vnc://localhost:5900+15900')

# Reset docker env
observation_n = env.reset()

# Vars for moving the car

left = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', True),
        ('KeyEvent', 'ArrowRight', False)]
right = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False),
         ('KeyEvent', 'ArrowRight', True)]

# Forward with greedy nitros boost
fwd = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowRight', False),
       ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'n', True)]

# Initiate vars
# TODO: Create class instead of this thing below :(
sum_reward = 0
turn = 0
rewards = []
buffer_size = 100
action = fwd

while True:
    
    turn -= 1
    if turn <= 0:
        action = fwd
        turn = 0
    # choose action based on speed
    action_n = [action for ob in observation_n]
    
    # perform action
    observation_n, reward_n, done_n, info = env.step(action_n)

    sum_reward += reward_n[0]
    
    rewards += [reward_n[0]]
    #if stuck, try going one side for some time
    if len(rewards) >= buffer_size:
        mean = sum(rewards)/len(rewards)
        print "mean:", mean

        if mean == 0:
            turn = 25 
            if random.random() < 0.5:
                action = left
            else:
                action = right
        
        rewards = []


    # debug values
    print reward_n[0], sum_reward

    # render
    env.render()
