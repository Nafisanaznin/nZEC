import pandas as pd
import matplotlib.pyplot as plt

#read from the json and make it into a list
df = pd.read_json("result.json", lines=True)
json_hist = df["hist_stats"]
normalize_hist_stats = pd.json_normalize(json_hist)
reward_list = []
for index, rows in df.iterrows():
  val = rows["episodes_this_iter"]
  statistic = rows["hist_stats"]
  episode_reward = statistic["episode_reward"]
  reward_list.extend(episode_reward[-20:])
#plotting graph
print(len(reward_list))
plt.plot(reward_list)
plt.show()
