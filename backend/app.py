# Import flask and datetime module for showing date and time
from flask import Flask, render_template , request,jsonify,json
import datetime
# pip install flask_cors
from flask_cors import CORS
from model import model
x = datetime.datetime.now()
# Initializing flask app
app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config["SECRET_KEY"]
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def starting():
    return render_template("", response=True)
@app.route('/getDataFromReact',methods=["POST"])
def setTime():
    if request.method == 'POST':
        m = model(app.config["DB_IP"], app.config["DB_USER"],
              app.config["DB_PASSWORD"], app.config["DATABASE"],app.config["DB_PORT"])
        FileName=request.form['fileName']
        dataOfFile=request.form['ArrayList']
        DictionaryOfdata=json.loads(dataOfFile)
        
        for e in DictionaryOfdata:
            m.insertRoadmap(json.dumps(e))
        DictionaryOfdata[0]
        # print(f'Posting....{FileName}{DictionaryOfdata[0]}{DictionaryOfdata[0]["rd_crs_code"]}')
        return "Hello"
    print('Wrong')
    return "Hello"
@app.route('/set_data',methods = ["GET"])
def set_data():
    m = model(app.config["DB_IP"], app.config["DB_USER"],
              app.config["DB_PASSWORD"], app.config["DATABASE"],app.config["DB_PORT"])
    List = m.getRoadMapList()
    print("posting......")
    print(List)
    if List != None:
        return jsonify(List)
    return "'key': 'empty'"

@app.route('/send-data', methods=['POST','GET'])
def send_data():
    course = None
    data = request.get_json()
    m = model(app.config["DB_IP"], app.config["DB_USER"],
            app.config["DB_PASSWORD"], app.config["DATABASE"],app.config["DB_PORT"])
    course = m.getcourse(data)
    if request.method == "POST":
        return "Success"
    else:
        return jsonify(course)

# @app.route('/getDataFromReact',methods=["GET"])
# def setTime():
#     if request.method == 'GET':
#         # dataFile=request.formData
#         print('Posting....') 
#         return jsonify()
#     print('Wrong')
#     return 'hello'

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/data',methods=["GET"])
# def get_time():
#     return {
#         'Name':"geek",
#         "Age":"22",
#         "Date":x,
#         "programming":"python"
#     }
#     # Running app