import gym
import numpy as np 
import pandas as pd 
import collections
import torch
import replay_memory
import policy_neural_networks

if __name__ == '__main__':
	env = gym.make("Walker 2d-v1")