import os


heroku_uri = os.environ.get('MONGODB_URI')
if heroku_uri:
	# Get Heroku DB config from environment variable
	MONGO_URI = heroku_uri
else:
	#This assumes that there is a database called 'test_courses'
	#and that db has a table 'courses'

	#Mongodb settings
	MONGO_HOST = 'localhost'
	MONGO_PORT = 27017

	MONGO_DBNAME = 'test_courses'
	RENDERERS = ['eve.render.JSONRenderer']

#definition of the API
schema = {
	'name': {
		'type':'string',
	},
	'description': {
		'type':'string',
	}
}

courses = {
	'item_title': 'course',
	'additional_lookup': {
		'url': 'regex("[\w+]")',
        'field': 'name'
    },
	'schema' : schema
}

DOMAIN = {'courses': courses}
