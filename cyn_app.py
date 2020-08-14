# Dependencies
from flask import Flask, render_template, request, redirect
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors
import os
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import warnings
warnings.simplefilter('ignore')
import numpy as np


# Create instance of Flask app
app = Flask(__name__)

# Route that renders the welcome page and receives user inputs
@app.route("/", methods=["GET", "POST"])
def user_inputs():

    if request.method == "POST":

        req = request.form

        summer_temp = req["summer-temp"]
        winter_temp = req["winter-temp"]
        city_size = req["city-size"]
        house_size = req["house-size"]
        budget = req["budget"]
        bedrooms = req["bedrooms"]
        bathrooms = req["bathrooms"]
        yard = req["yard"]
    

        print(
            f"""
            Form submitted:\n
            Summer Temp: {summer_temp}\n
            Winter Temp: {winter_temp}\n
            City Size: {city_size}\n
            House Size: {house_size}\n
            Budget: {budget}\n
            Bedrooms: {bedrooms}\n
            Bathrooms: {bathrooms}\n
            Yard: {yard}\n 
            """)


        return redirect(request.url)

    return render_template("index.html")

# Route that renders the ML Results
@app.route("/results", methods=("POST", "GET"))

def run_ml():
    housing_training_data = pd.read_csv("housing_training_data.csv")
    house_data_for_results = pd.read_csv("combination_data/housing_complete_data.csv")
    X = housing_training_data[['price', "beds", 'baths', "square_feet", "lot_size", 'hoa_permonth', "Summer Temp", "Winter Temp", "population"]]
    # data = X.copy()
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

    mytable = results_df.to_html(classes="results")
    return render_template('display_results.html',  table=mytable , titles=results_df.columns.values)
       
        
    

if __name__ == "__main__":
    app.run(debug=True)