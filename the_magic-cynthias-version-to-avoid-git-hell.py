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
import pickle

housing_training_data = pd.read_csv("housing_training_data.csv")
house_data_for_results = pd.read_csv("combination_data/housing_complete_data.csv")
X = housing_training_data[["Summer Temp", "Winter Temp", "pop_cat_hot", "square_feet", 'price', "beds", 'baths', "lot_size_hot"]]
# results_df.to_html(classes="results")
def train_and_save_model(input_array):
    # Change this to load saved model
    # importing data
    # housing_training_data = pd.read_csv("housing_training_data.csv")
    # house_data_for_results = pd.read_csv("combination_data/housing_complete_data.csv")
    # X = housing_training_data[["Summer Temp", "Winter Temp", "pop_cat_hot", "square_feet", 'price', "beds", 'baths', "lot_size_hot"]]
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    # X_scaler = StandardScaler().fit(X)
    kmeans = KMeans(n_clusters=400)
    kmeans.fit(X)
    # need and array of arrays 
    
    # Convert string input to number
    if input_array[2] == "Small Town":
        input_array[2] = 0
    elif input_array[2] == "Medium City":
        input_array[2] = 1
    else:
        input_array[2] = 2

    # Yard Size
    if input_array[7] == "Yes":
        input_array[7] = 1
    else:
        input_array[7] = 0

    with open('kmeans.pickle', 'wb') as f:
        pickle.dump(kmeans, f)

    return 'kmeans.pickle'

def make_prediction(input_array):    
    # Convert string input to number
    if input_array[2] == "Small Town":
        input_array[2] = 0
    elif input_array[2] == "Medium City":
        input_array[2] = 1
    else:
        input_array[2] = 2

    # Yard Size
    if input_array[7] == "Yes":
        input_array[7] = 1
    else:
        input_array[7] = 0
    with open('kmeans.pickle', 'rb') as f:
        kmeans = pickle.load(f)
    Xlist = X.to_numpy()
    # ### HERE BEGINS THE MAGIC unsupervised cluster 
    kmeans.fit(Xlist)
    cat = kmeans.predict(np.array(input_array).reshape(1, -1))
    house_list = []

    for i in range(len(housing_training_data)):
        if kmeans.predict(Xlist[i].reshape(1, -1)) == cat:
            house_list.append(housing_training_data.house_id[i])
        
    results_df = house_data_for_results[house_data_for_results["House ID"].isin(house_list)]

    return results_df
    