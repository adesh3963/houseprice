from flask import Flask, jsonify, request, render_template

import util
app= Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('app.html')

@app.route('/get_location_names')
def get_location_names():

    print('here is here')
    response= jsonify({
        "locations": util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', "*")
    print(response)

    return response


@app.route('/predict', methods=["POST"])
def predict():
    if request.method == 'POST':
        total_sqft=float(request.form["TOTAL_SQFT"])
        location= request.form["LOCATION"]
        bhk= int(request.form["BHK"])
        balcony=int(request.form["BALCONY"])
        bath= int(request.form["BATH"])

        
        estimated_price= util.get_estimated_price(total_sqft,bath,balcony,bhk,location)
        print(estimated_price)
        
        return render_template('result.html', prediction=estimated_price)
    else:
        return render_template('app.html')

if __name__== "__main__":
    util.load_save_artifacts()
    app.run(debug=True)