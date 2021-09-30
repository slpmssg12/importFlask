from flask import Flask
app = Flask(_name_) # "_main_"


@app.route('/hello', methods=['GET'])
def hello_world():
 return "Hello world."

if _name_ == "_main_":
 app.run(host='0.0.0.0', port=8080
