"""Senior Work App API"""
import flask as fl
import json

app = fl.Flask(__name__, template_folder='jinja_templates/')

with open('user-data/student_trackers.json') as f:
	student_profiles = json.load(f)

if __name__ == "__main__":
	app.run(debug=True)
