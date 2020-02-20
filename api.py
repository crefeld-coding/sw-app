"""Senior Work App API"""
import flask as fl
import json

app = fl.Flask(__name__)

with open('user-data/student_trackers.json') as f:
	student_profiles = json.load(f)
