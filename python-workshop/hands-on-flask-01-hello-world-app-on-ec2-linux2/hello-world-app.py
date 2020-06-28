from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World from Vincenzo"

print('name of this app..:', __name__)

if __name__ == '__main__':
	#app.run('localhost', port=5000, debug=True)>>default values
	app.run(debug=True)
	
	