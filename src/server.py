# pip install flask
import legofy
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return legofy.main("../assets/images/주먹밥.jpeg", size= 100, palette_mode= 'px-master')

if __name__ == '__main__':
    app.run(debug=False,host="127.0.0.1", port=5000)