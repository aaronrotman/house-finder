# Dependencies
from flask import Flask, render_template, request, redirect

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

if __name__ == "__main__":
    app.run(debug=True)