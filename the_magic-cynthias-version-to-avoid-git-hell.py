
import matplotlib.pyplot as plt
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
house_data_for_results = pd.read_csv("combination_data/housing_complete_data.csv")
X = housing_training_data[['price', "beds", 'baths', "square_feet", "lot_size", 'hoa_permonth', "Summer Temp", "Winter Temp", "population"]]
data = X.copy()
from sklearn.model_selection import train_test_split
X_train, X_test= train_test_split(X, random_state=42)
from sklearn.preprocessing import StandardScaler
X_scaler = StandardScaler().fit(X)
X_train_scaled = X_scaler.transform(X)
kmeans = KMeans(n_clusters=200)
kmeans.fit(X)
predicted_clusters = kmeans.predict(X)
Xlist = X.to_numpy()


# ### HERE BEGINS THE MAGIC unsupervised cluster 
kmeans.fit(Xlist)
predicted_clusters = kmeans.predict(Xlist)

# Print the cluster centers and cluster labels
centers = kmeans.cluster_centers_
labels = kmeans.labels_

cat = kmeans.predict(Xlist[0].reshape(1, -1))

house_list = []

for i in range(4000):
    if kmeans.predict(Xlist[i].reshape(1, -1)) == cat:
#         print (housing_training_data.iloc[i])
#         print (housing_training_data.house_id[i])
        house_list.append(housing_training_data.house_id[i])
#         print (Xlist[i])
#         print (kmeans.predict(Xlist[i].reshape(1, -1)))
        
    
results_df = house_data_for_results[house_data_for_results["house_id"].isin(house_list)]
print(results_df)

results_df.to_html(classes="results")



