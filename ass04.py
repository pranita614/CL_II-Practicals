# Agglomerative Hierarchical Clustering

import pandas as pd  # Imports Pandas library for data handling and analysis
import matplotlib.pyplot as plt  # Imports Matplotlib for creating graphs and visualizations

from sklearn.datasets import load_iris  # Imports the built-in Iris dataset
from sklearn.cluster import AgglomerativeClustering  # Imports Agglomerative Hierarchical Clustering algorithm
from scipy.cluster.hierarchy import dendrogram, linkage  # Imports functions to create linkage matrix and dendrogram

iris = load_iris()  # Loads the Iris flower dataset

data = pd.DataFrame(  # Converts the Iris dataset into a Pandas DataFrame
    iris.data,  # Contains the flower measurements
    columns=iris.feature_names  # Assigns column names to the measurements
)

print("First 5 records:")
print(data.head())

Z = linkage(data, method="ward")  # Creates a linkage matrix using Ward's method to combine similar clusters

plt.figure(figsize=(10, 6))  # Creates a figure with width 10 and height 6

dendrogram(  # Draws a hierarchical clustering dendrogram
    Z,  # Uses the linkage matrix
    truncate_mode="level",  # Displays only the specified number of hierarchy levels
    p=5  # Displays the last 5 levels of the hierarchy
)

plt.title("Dendrogram - Agglomerative Hierarchical Clustering")  # Sets the graph title
plt.xlabel("Data Points")  # Sets the X-axis label
plt.ylabel("Distance")  # Sets the Y-axis label

plt.show()  # Displays the dendrogram


model = AgglomerativeClustering(  # Creates an Agglomerative Clustering model
    n_clusters=3,  # Divides the dataset into 3 clusters
    linkage="ward"  # Uses Ward's method to minimize within-cluster variance
)

clusters = model.fit_predict(data)  # Fits the model and assigns a cluster label to each data point

data["Cluster"] = clusters  # Adds the assigned cluster labels as a new column in the dataset

print("\nClustered Data:")
print(data.head(10))

print("\nNumber of data points in each cluster:")

print(data["Cluster"].value_counts().sort_index())  # Counts data points in each cluster and sorts by cluster number

plt.figure(figsize=(8, 6))  # Creates a figure with width 8 and height 6

plt.scatter(  # Creates a scatter plot to visualize the clusters
    data.iloc[:, 0],  # Selects the first column (Sepal Length) for the X-axis
    data.iloc[:, 1],  # Selects the second column (Sepal Width) for the Y-axis
    c=data["Cluster"],  # Assigns different colors based on cluster labels
    cmap="rainbow",  # Uses rainbow colors to distinguish clusters
    s=50  # Sets the size of each plotted point
)

plt.xlabel("Sepal Length")  # Sets the X-axis label
plt.ylabel("Sepal Width")  # Sets the Y-axis label
plt.title("Agglomerative Hierarchical Clustering")  # Sets the graph title

plt.show()  # Displays the final cluster visualization