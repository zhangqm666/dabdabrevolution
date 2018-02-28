from flask import Flask, Response, send_from_directory
import random, time
app = Flask(__name__, static_folder='www')

@app.route('/')
def index():
	return ''

@app.route('/stream')
def stream():
	def event():
		while True:
			yield "data: " + random.choice(['a', 'b', 'c', 'd']) + "nn"
			with app.app_context():
				time.sleep(1)
	return Response(event(), mimetype="text/event-stream")

@app.route('/static/<path:path>')
def static_f(path):
	return app.send_static_file(path)

if __name__ == '__main__':
	app.run(debug=True)