import os

heroku_uri = os.environ.get('MONGODB_URI')
if heroku_uri:
    # Get Heroku DB config from environment variable
    MONGO_URI = heroku_uri
else:
    # This assumes that there is a database called 'test_courses'
    # and that db has a table 'courses'

    # Mongodb settings
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017

    MONGO_DBNAME = 'test_courses'

X_DOMAINS = '*'
RENDERERS = ['eve.render.JSONRenderer']

# definition of the API
schema = {
    'dept': {
        'type': 'string'
    },
    'course_num': {
        'type': 'string'
    },
    'course_section': {
        'type': 'string'
    },
    'credits': {
        'type': 'string'
    },
    'name': {
        'type': 'string'
    },
    'prof': {
        'type': 'string'
    },
    'building': {
        'type': 'string'
    },
    'room_num': {
        'type': 'string'
    },
    'description': {
        'type': 'string'
    },
    'sched': {
        'type': 'dict',
        'schema': {
            'mon': {
                'start': {
                    'type': 'string'
                },
                'end': {
                    'type': 'string'
                }
            },
            'tue': {
                'start': {
                    'type': 'string'
                },
                'end': {
                    'type': 'string'
                }
            },
            'wed': {
                'start': {
                    'type': 'string'
                },
                'end': {
                    'type': 'string'
                }
            },
            'thu': {
                'start': {
                    'type': 'string'
                },
                'end': {
                    'type': 'string'
                }
            },
            'fri': {
                'start': {
                    'type': 'string'
                },
                'end': {
                    'type': 'string'
                }
            }
        }
    }
}

courses = {
    'item_title': 'course',
    'additional_lookup': {
        'url': 'regex("[\w+]")',
        'field': 'name'
    },
    'schema': schema
}

DOMAIN = {
    'courses': courses
}
