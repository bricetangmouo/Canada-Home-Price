from flask import Flask, request, jsonify
app = Flask(__name__)
import utils

@app.route('/get_name_element', methods = ['GET'])
def get_all_columns():
    reponse = jsonify({
        'province':utils.get_province(),
        'city': utils.get_city(),
        'home_type': utils.get_type_home(),
        'smoking_permission': utils.get_smoking_type()
    })
    reponse.headers.add('Access-Control-Allow-Origin', '*')
    return reponse

@app.route('/predict_home_price', methods = ['POST'])
def predict_home_price():
    province = request.form(['province'])
    city= request.form(['city'])
    home_type = request.form(['home_type'])
    smoking_permission = request.form(['smoking_permission'])


if __name__ == '__main__':
    app.run()