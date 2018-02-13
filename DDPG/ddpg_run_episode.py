from __future__ import division
import gym
import numpy as np 
import pandas as pd 
import collections
import torch
import psutil
import replay_memory
import policy_neural_networks
import train_networks



no_of_episodes = 6000
no_of_steps = 2000

if __name__ == '__main__':
	env = gym.make('Walker2d-v1')

	mem = replay_memory.ReplayMemory(10000000)
	trainer = train_networks.Training(env.observation_space.shape[0], env.action_space.shape[0], env.action_space.high[0], mem)

	
	avg_reward = 0.0
	sum_reward = 0
	for i in range(no_of_episodes):
		obs = env.reset()
		
		print "Episode No - "+str(i)+"" 
		for j in range(no_of_steps):
			#if i%100 == 0:
			env.render()	
			
			state = np.float32(obs)
			action = trainer.next_action(state)

			next_obs, reward, done, ext = env.step(action)
			sum_reward += reward
			
			if done==False:
				next_state = np.float32(next_obs)
				mem.add_transition(state, action, reward, np.float32(next_state))
			
			trainer.learn()
			obs = next_obs
			if done:
				break
		avg_reward = sum_reward/no_of_steps
		print avg_reward		
