import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read from the json and make it into a list
df = pd.read_json("iql_5_result.json", lines=True)
json_hist = df["hist_stats"]
normalize_hist_stats = pd.json_normalize(json_hist)
reward_list_iql = []
for index, rows in df.iterrows():
  val = rows["episodes_this_iter"]
  statistic = rows["hist_stats"]
  episode_reward = statistic["episode_reward"]
  reward_list_iql.extend(episode_reward[-5:])

#read from the json for mappo
df = pd.read_json("mappo_5_result.json", lines=True)
json_hist = df["hist_stats"]
normalize_hist_stats = pd.json_normalize(json_hist)
reward_list_mappo = []
for index, rows in df.iterrows():
  val = rows["episodes_this_iter"]
  statistic = rows["hist_stats"]
  episode_reward = statistic["episode_reward"]
  reward_list_mappo.extend(episode_reward[-5:])

#plotting graph
x = list(range(1, 501))
fig, ax = plt.subplots()
ax.plot(x, reward_list_mappo, color = 'royalblue', label = 'MAPPO')
ax.plot(x, reward_list_iql, color = 'orange', label = 'IQL')
plt.title('Reward Graph for 5 Agents')
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.legend(loc='lower right')
plt.grid(True)
plt.savefig("5_Agents.svg", format="svg")
plt.show()