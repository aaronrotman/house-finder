
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
import time

housing_training_data = pd.read_csv("housing_training_data.csv")
house_data_for_results = pd.read_csv("combination_data/housing_complete_data.csv")
X = housing_training_data[["Summer Temp", "Winter Temp", "pop_cat_hot", "square_feet", 'price', "beds", 'baths', "lot_size_hot"]]


def train_and_save_model():

    from sklearn.model_selection import train_test_split
    kmeans = KMeans(n_clusters=400)
    kmeans.fit(X)
    
    with open('kmeans.pickle', 'wb') as f:
        pickle.dump(kmeans, f)

#train_and_save_model()    

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
    
    Xlist = X.to_numpy()
    # ### HERE BEGINS THE MAGIC unsupervised cluster 
    opening_pickle_start = time.perf_counter()
    with open('kmeans.pickle', 'rb') as f:
        kmeans = pickle.load(f)
    opening_pickle_end = time.perf_counter()
    print("Spent " + str(opening_pickle_end-opening_pickle_start) +" seconds in that load pickle block.")

    fit_start = time.perf_counter()
    kmeans.fit(Xlist)
    fit_end = time.perf_counter()
    print("Spent " + str(fit_end-fit_start) +" seconds in that fitting block.")

    cat_start_time = time.perf_counter()
    cat = kmeans.predict(np.array(input_array).reshape(1, -1))
    cat_end_time = time.perf_counter()
    print("Spent " + str(cat_end_time-cat_start_time) + " seconds in that cat block.")
    house_list = []

    houselist_timer_start = time.perf_counter()
    for i in range(len(housing_training_data)):
        if kmeans.predict(Xlist[i].reshape(1, -1)) == cat:
            house_list.append(housing_training_data.house_id[i])
        
    results_df = house_data_for_results[house_data_for_results["House ID"].isin(house_list)]
    houselist_timer_end = time.perf_counter()
    print("Spent " + str(houselist_timer_end-houselist_timer_start) + " seconds in that housinglist block.")

    return results_df
    