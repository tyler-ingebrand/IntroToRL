import gym

# Recall MDPs are basically games
# All of the following are games you can try. Comment out all but 1.
# Try any of the following
env = gym.make("Acrobot-v1") # continuous state, discrete action
env = gym.make("MountainCar-v0") # continuous state, discrete action
env = gym.make("CartPole-v1")  # continuous state, discrete action
env = gym.make("Pendulum-v1")  # continuous state, continuous action
# If you want to get robotics examples or Atari games, let me know. It takes more effort but is possible

# sets the environment to a new episode
observation = env.reset()

# Iterates through the episode
for _ in range(1000):
    # Sets a random action
    action = env.action_space.sample()

    # Applies that action to env. Gets the new state, reward, termination (bool) as a result
    observation, reward, terminated, info = env.step(action)

    # resets environment if it has reached a termination condition
    if terminated:
        observation = env.reset()

    # display env for fun. Dont do this while training FYI, it is slow
    env.render()
    # Try printing different things to see what it looks like
    # print("State = ", observation)
    # print("Action = ", action)
    # print("Reward = ", reward)

# closes render window
env.close()