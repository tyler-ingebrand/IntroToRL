import gym

from stable_baselines3 import DDPG

# choose the mdp
env = gym.make("Pendulum-v1") # continuous state, continuous action
# This alg can only handle continuous action spaces!

# Creates a algorithm to solve your game. The algorithm has to be tailored to your env because it
# needs to know how many states and actions their are.
# It also needs to use a Multi-Layer Perceptron as the actor and critic, AKA a normal neural network.
# DDPG is the alg we talked about for continuous state, continuous action spaces
model = DDPG("MlpPolicy", env, verbose=1)

# runs 100,000 steps (not episodes) of the game in simulation
# Learns using the bellman equation we talked about
model.learn(total_timesteps=10_000)

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