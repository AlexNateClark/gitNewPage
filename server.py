from flask_app import app   
from flask import render_template, Flask
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True, port=5001)