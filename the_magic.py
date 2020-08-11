# import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import os
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.cluster import KMeans
# get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.preprocessing import StandardScaler
import warnings
warnings.simplefilter('ignore')
import numpy as np

# importing data
housing_training_data = pd.read_csv("housing_training_data.csv")
# housing_training_data.head()


X = housing_training_data[["temp_range", "population", "square_feet", 'price', "beds", 'baths', "lot_size", 'hoa_permonth',]]
# print(X.shape)


data = X.copy()

# scaling the data
from sklearn.preprocessing import StandardScaler
X_scaler = StandardScaler().fit(X)
X_train_scaled = X_scaler.transform(X)

# run the ML model w/ clusters
kmeans = KMeans(n_clusters=16)
kmeans.fit(X)
predicted_clusters = kmeans.predict(X)

# turn dataframe into an array of arrays for ML Model
Xlist = X.to_numpy()
Xlist

kmeans.fit(Xlist)

# need to change Xlist to the user input variable
predicted_clusters = kmeans.predict(Xlist)

predicted_clusters
# Print the cluster centers and cluster labels
centers = kmeans.cluster_centers_
labels = kmeans.labels_
# centers


cat = kmeans.predict(Xlist[0].reshape(1, -1))

# checking the results of the models
# Xlist[0]
# Xlist[1]

# X

# putting the results into a list to push to the front end
house_list = []

for i in range(4000):
    if kmeans.predict(Xlist[i].reshape(1, -1)) == cat:
        results_objects = housing_training_data.iloc[i]
        # print (housing_training_data.house_id[i])
        house_list.append(housing_training_data.house_id[i])
        # print (Xlist[i])
        # print (kmeans.predict(Xlist[i].reshape(1, -1)))
        # print(results_objects)

print(house_list)
print(results_objects[0])

# send house list to front end...
house_data_for_results = pd.read_csv("combination_data/housing_complete_data.csv")
results_df = house_data_for_results[house_data_for_results["house_id"].isin(house_list)]
results_df