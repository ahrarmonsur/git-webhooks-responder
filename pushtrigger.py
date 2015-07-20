from flask import Flask, request
import subprocess, os, datetime

app = Flask(__name__)

branch = 'ContInt'
directory = os.path.dirname(os.path.realpath(__file__))

def log_and_respond(message):
    message = str(datetime.datetime.now()) + "\t" + message
    print message
    return message

@app.route('/push_trigger', methods=['GET', 'POST'])
def do_POST():
    if request.method == 'POST':
	print request.form

	error = subprocess.call(['./git-updater.sh', directory, branch])
	if not error:
	    return log_and_respond('Git updating script ran successfully')
	else:
	    return log_and_respond('Error: git updating script did not run successfully')
    else:
	return log_and_respond('Error: Webhook was not a POST request')

if __name__ == '__main__':
    app.run(port=8080)
