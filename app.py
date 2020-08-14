# Dependencies
from flask import Flask, render_template, request, redirect
import pandas as pd
import the_magic
import time

# Create instance of Flask app
app = Flask(__name__)

# Route that renders the welcome page and receives user inputs
@app.route("/", methods=["GET", "POST"])
def user_inputs():
    app.logger.debug('user_inputs() called.')

    if request.method == "POST":
        post_start_time = time.perf_counter()
        app.logger.debug('POST request received.')

        req = request.form

        summer_temp = req["summer-temp"]
        winter_temp = req["winter-temp"]
        city_size = req["city-size"]
        house_size = req["house-size"]
        budget = req["budget"]
        bedrooms = req["bedrooms"]
        bathrooms = req["bathrooms"]
        yard = req["yard"]
        # Array of user inputs
        input_array = [summer_temp, winter_temp, city_size, house_size, budget, bedrooms, bathrooms, yard]
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
        
        get_table_data = the_magic.make_prediction(input_array)
        mytable = get_table_data.to_html(classes="results table table-striped")
        post_end_time = time.perf_counter()
        time_spent_processing_post_request = post_end_time - post_start_time
        app.logger.debug("Spent " + str(time_spent_processing_post_request) + " seconds processing POST.")
        return render_template('display_results.html',  table=mytable , titles=get_table_data.columns.values)
        
       
    return render_template("index.html")


    
    
#     return render_template('simple.html',  tables=[results_df.to_html(classes="results")], titles=results_df.columns.values)

if __name__ == "__main__":
    app.run(debug=True)