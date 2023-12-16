# import gym
# import ma_gym
# gym.envs.register(
#     id='PowerGrid-v1',
#     entry_point='ma_gym.envs.power_grid:PowerGrid',
# )
# env = gym.make('PowerGrid-v1')
# env.reset()
# for i in range(100):
#   obs,r,d,info = env.step(env.action_space.sample())
#-----------------------------------------------------
# import pandas as pd
# from matplotlib import pyplot as plt
# from iteration_utilities import flatten
# import json
# data = [json.loads(line) for line in open('MARLlib/exp_results/mappo_mlp_PowerGrid/MAPPOTrainer_magym_PowerGrid_206d3_00000_0_2023-12-16_13-24-19/result.json', 'r')]
# data_frame = pd.json_normalize(data, max_level=1)
# listed = list(data_frame["hist_stats.episode_reward"])
# flattend_reward_list = list(flatten(listed))
# lst = list(range(0,len(flattend_reward_list)))
# plt.figure(figsize=(20,10))
# plt.plot(lst, flattend_reward_list)
# plt.show()
# from matplotlib import pyplot as plt
# h = open('MARLlib/exp_results/mappo_mlp_PowerGrid/MAPPOTrainer_magym_PowerGrid_206d3_00000_0_2023-12-16_13-24-19/microgrid.txt', 'r')
# # Reading from the file
# content = h.readlines()
# lst = []
# for c in content:
#   lst.append(float(c))
# index = list(range(0, len(lst)))
# plt.plot(index, lst)
# plt.show()
#-----------------------load 
from matplotlib import pyplot as plt
h = open('MARLlib/exp_results/mappo_mlp_PowerGrid/MAPPOTrainer_magym_PowerGrid_206d3_00000_0_2023-12-16_13-24-19/loads.txt', 'r')
content = h.read().splitlines()
lst = []
for c in content:
  c = c.strip('][').split(', ')
  num_list = []
  for list_value in c:
    num_list.append(float(list_value))
  lst.append(sum(num_list))
print(lst[1])
index = list(range(0, len(lst)))
plt.plot(index, lst)
plt.show()

