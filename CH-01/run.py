from flask import Flask , jsonify #jsonify -> browser ngerti dri py ke js 
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welcome to My Page</h1>"

# API GATEWAY

@app.route("/api/weather/tokyo")
def api_currency_latest():
    try:
        with open("data.json") as file:
            data = json.load(file)
    except: 
        return jsonify({
            "status" : False
        })
    else:
        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin','*')
        return response


app.run(debug=True)