# IntroToRL

## Setup
Download Pycharm - https://www.jetbrains.com/pycharm/download/#section=windows
Create new project
Go to settings (top right) > Project > Python Interpreter > Add package "stable-baselines3" (Use the plus sign, this will take some time to download)
Do the same thing for package "pyglet"

## Starting point. Play with the provided scripts. 
Run show_MDPs.py to see MDPs in action. They are basically games.
Run train_DQN.py to solve a MDP using DQN, the continuous state space discrete action space algorithm.
Run train_DDPG.py to solve a MDP using DDPG, the continuous state space continuous action space algorithm.

## Where to go:
- Create your own MDP: See google or https://towardsdatascience.com/creating-a-custom-openai-gym-environment-for-stock-trading-be532be3910e for examples. 
- Try to solve Atari games or Robotics using one of these reinforcement learning algs. You would have to install a few packages (from the command line this time) but LMK, I can help. 
- To get a good understanding of the algorithms, read the papers (Simply google the algorithm names and you will find the paper). Then compare to the source code at https://github.com/DLR-RM/stable-baselines3/tree/master/stable_baselines3. If you can understand how the algorithm becomes code you can do research in the field. Most of the algorithms are only 1 trick more complicated than the last. 
