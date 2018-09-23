from flask import Flask

# initialize flask app
app = Flask(__name__)

# route calls to local_ip/ to this function
@app.route("/")
def get_command():
	"""
	returns current command when called on local_ip/
	"""
	with open("command_file.txt", "r") as command_file:
		current_command = command_file.read()
	return current_command

# run the service
if __name__ == '__main__':
    app.run(host='0.0.0.0') # host argument for exposing to to web