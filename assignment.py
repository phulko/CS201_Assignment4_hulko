import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("random_walk.csv")
df["distance"] = np.sqrt(df["x"]**2 + df["y"]**2)

max_dist = df["distance"].max()
mean_dist = df["distance"].mean()

print("max distance = ", max_dist)
print("mean distance = ", mean_dist)

filtered_df = df[df["distance"] > mean_dist]
print(filtered_df)

filtered_df.to_json("filtered_walk.json")

plt.plot(df["x"], df["y"])
plt.scatter(0, 0, label="Starting point")
plt.scatter(df["x"].iloc[-1], df["y"].iloc[-1], label="End point")
plt.title("Random Walk Distance")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

#але в Rstudio працювати з даними простіше в рази:)