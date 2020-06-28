from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World from Call'

if __name__=='__main__':
    # app.run('localhost', port=5000, debug=True)  default values
     app.run(debug=True) # to run the app. via your local
    # app.run('0.0.0.0', port=80)  to run the app. via EC2, activate this line

