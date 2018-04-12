import os

heroku_uri = os.environ.get('MONGODB_URI')
if heroku_uri:
    # Get Heroku DB config from environment variable
    MONGO_URI = heroku_uri
else:
    # This assumes that there is a database called 'test_courses'
    # and that db has a table 'courses' and a table 'periods'

    # Mongodb settings
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017

    MONGO_DBNAME = 'test_courses'

X_DOMAINS = '*'
RENDERERS = ['eve.render.JSONRenderer']

# definition of the API
course_schema = {
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
                    'type': 'datetime'
                },
                'end': {
                    'type': 'datetime'
                }
            },
            'tue': {
                'start': {
                    'type': 'datetime'
                },
                'end': {
                    'type': 'datetime'
                }
            },
            'wed': {
                'start': {
                    'type': 'datetime'
                },
                'end': {
                    'type': 'datetime'
                }
            },
            'thu': {
                'start': {
                    'type': 'datetime'
                },
                'end': {
                    'type': 'datetime'
                }
            },
            'fri': {
                'start': {
                    'type': 'datetime'
                },
                'end': {
                    'type': 'datetime'
                }
            }
        }
    }
}

period_schema = {
    'name' : {
        'type' : 'string'
    },
    'mon': {
        'start': {
            'type': 'datetime'
        },
        'end': {
            'type': 'datetime'
        }
    }, 
    'tue': {
        'start': {
            'type': 'datetime'
        },
        'end': {
            'type': 'datetime'
        }
    }, 
    'wed': {
        'start': {
            'type': 'datetime'
        },
        'end': {
            'type': 'datetime'
        }
    }, 
    'thu': {
        'start': {
            'type': 'datetime'
        },
        'end': {
            'type': 'datetime'
        }
    }, 
    'fri': {
        'start': {
            'type': 'datetime'
        },
        'end': {
            'type': 'datetime'
        }
    }
}

courses = {
    'item_title': 'course',
    'additional_lookup': {
        'url': 'regex("[\w+]")',
        'field': 'name'
    },
    'schema': course_schema
}

periods = {
    'schema': period_schema
}

DOMAIN = {
    'courses': courses,
    'periods': periods
}
