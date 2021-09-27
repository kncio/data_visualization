import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")


# Path of the file to read
ign_filepath = "ign_scores.csv"

# Fill in the line below to read the file into a variable ign_data
ign_data = pd.read_csv(ign_filepath, index_col="Platform")

# print(ign_data)

# Bar chart showing average score for racing games by platform
# plt.figure(figsize=(8,6))
# sns.barplot(x=ign_data['Racing'], y= ign_data.index)
# plt.xlabel("")
# plt.title("Average Score ffor Racing Games, by Platform")
# plt.show()

plt.figure(figsize= (10,10)) # Your code here
sns.heatmap(ign_data, annot=True)
#Add label for horizontal axis
plt.xlabel("Genre")
# Add label for vertical axis
plt.title("Average Game Score, by Platform and Genre")
plt.show()