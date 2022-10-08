import gym

from stable_baselines3 import DQN # if you want different algorithms, there are many in this package. Try A2C.

# choose the mdp
env = gym.make("Acrobot-v1") # continuous state, discrete action
env = gym.make("MountainCar-v0") # continuous state, discrete action. Something unexpected happens if you run this one, note the reward function is -1 always. This is not sufficient for learning!
env = gym.make("CartPole-v1")  # continuous state, discrete action
# This alg can only handle discrete action spaces!

# Creates a algorithm to solve your game. The algorithm has to be tailored to your env because it
# needs to know how many states and actions their are.
# It also needs to use a Multi-Layer Perceptron as the critic, AKA a normal neural network.
# DQN is the alg we talked about for continuous state, discrete action spaces
model = DQN("MlpPolicy", env, verbose=1)

# runs 100,000 steps (not episodes) of the game in simulation
# Learns using the bellman equation we talked about
model.learn(total_timesteps=100_000)

# Now its done training, lets run a sample episode to see how it does
obs = env.reset()
for i in range(1000):
    # passes the state (observation) into the learned model. Returns the action given by the policy.
    action, _state = model.predict(obs, deterministic=True)

    # apply action to env
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
      obs = env.reset()