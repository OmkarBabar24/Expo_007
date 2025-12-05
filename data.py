import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ****** Histogram ******
# data=pd.Series([1,1,3,3,4,4,4,2,2,2,5,5])
# sns.histplot(data)
# plt.show()

# # ******  Scatter plot ******
# # data=pd.DataFrame({'x':[1,2,3,4,5],'y':[2,4,1,5,3]})
# # sns.scatterplot(x='x',y='y',data=data)
# # plt.show()A
#
# # ****** Bar Plot ******
# # data=pd.DataFrame({'category':['A','B','C'],'Value':[10,15,7]})
# # sns.barplot(x='category',y='Value',data=data)
# # plt.show()
#
# # # ****** Box Plot ******
# # data=pd.DataFrame({'Category':['A','A','B','B','C','C'],'Value':[5,7,10,12,3,8]})
# # sns.boxplot(x='Category',y='Value',data=data)
# # plt.show()
#
# # sns.set_style("whitegrid")
# # sns.histplot()
# # plt.show()
#
# # ****** Distrubution plot ******
# # data=pd.DataFrame({'Category':['A','A','B','B','C','C'],'Value':[5,7,10,12,3,8]})
# # sns.displot(data,kind="hist")
# # plt.show()
# #
# # sns.displot(data,kind='kid')
# # plt.show()
#
# aa = sns.load_dataset('tips')
# print(aa.head())
#
#
df = sns.load_dataset("tips")  # Contains data about restaurant bills and tips
print(df.head())

#
# # 2)Scatter Plots = visualize the relationship between two numerical variables
#
# sns.scatterplot(x="total_bill", y="tip", data=df)
# plt.show()

#
#  3) Line Plot
#
# sns.lineplot(x="size", y="tip", data=df)
# plt.show()

#
# 4)Histogram / Distribution Plot =  To understand the distribution of a single numerical variable
#
# sns.histplot(df["total_bill"], kde=True)
# plt.show()

#5) Box Plot
#
# sns.boxplot(x="day", y="total_bill", data=df)
# plt.show()

#
 # 6)Violin Plot

# sns.violinplot(x="day", y="total_bill", data=df)
# plt.show()


# 3. Intermediate Concepts
#
# 3.1. Categorical Plot (catplot)
#
# sns.catplot(x="day", y="total_bill", hue="sex", kind="bar", data=df)
# plt.show()


# 3.2. Pairplot
#
# Shows relationships between all numerical columns:
#
# sns.pairplot(df, hue="sex")
# plt.show()
#
#
# ---
#
# 3.3. Heatmap (correlation)
#
# corr = df.corr()
# sns.heatmap(corr, annot=True, cmap="coolwarm")
# plt.show()
#
#
# ---
#
# 4. Advanced Seaborn Features
#
# 4.1. FacetGrid (multi-plot layout)
#
# g = sns.FacetGrid(df, col="sex", row="time")
# g.map(sns.scatterplot, "total_bill", "tip")
# plt.show()
#
#
# ---
#
# 4.2. Custom Styling
#
# sns.set_style("whitegrid")
# sns.boxplot(x="day", y="total_bill", data=df)
# plt.title("Boxplot with whitegrid style")
# plt.show()
#
#
# ---
#
# 4.3. Regression Plot
#
# sns.lmplot(x="total_bill", y="tip", hue="sex", data=df)
# plt.show()
#
#
# ---
#
# 4.4. Swarm Plot
#
# sns.swarmplot(x="day", y="total_bill", data=df)
# plt.show()
#
#
# ---
#
# 4.5. Combining Plots
#
# fig, axes = plt.subplots(1, 2, figsize=(12, 6))
# sns.boxplot(x="day", y="tip", data=df, ax=axes[0])
# sns.violinplot(x="day", y="tip", data=df, ax=axes[1])
# plt.show()
#
#
# ---
#
# Would you like this as a downloadable notebook or a PDF?