import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("matches_cleaned.csv")
deliveries = pd.read_csv("deliveries_cleaned.csv")
print("Both table loaded.............")
print("BOX PLOT")
plt.figure(figsize=(7,5))
plt.boxplot(matches["target_runs"].dropna())
plt.title("Box Plot of Target Runs")
plt.xlabel("Target Runs")
plt.ylabel("Runs")
plt.show()

print("HISTOGRAM")
plt.hist("batsman_runs", bins = 100, edgecolor = 'Orange', color = 'cyan')
plt.ylabel("Frequency")
plt.show()

print("BAR CHART")
plt.bar("winner","target_runs", width = 0.5, align = 'center', edgecolor = 'Orange', color = 'cyan')
plt.title("Bar Chart for winner")
plt.show()

print("plotting scatter chart")
plt.scatter("target_overs", "target_runs", alpha = 0.7, s= 50)
plt.show()

print("Line Chart")
plt.plot(matches["target_runs"], matches["result_margin"], linestyle='dotted')
#Labelling Axes
plt.xlabel("Target Run", fontdict = {'fontsize' : 12, 'fontweight' : 5, 'color' : "Brown"})
plt.ylabel("Result Margin", fontdict = {'fontsize' : 12, 'fontweight' : 5, 'color' : 'Brown'})
plt.show()

print("Group BY Line Chart")
season_matches = matches.groupby("season")["id"].count()
plt.figure(figsize=(10,5))
season_matches.plot(kind="line", marker="o")
plt.title("Number of Matches Played per Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.grid(True)
plt.show()