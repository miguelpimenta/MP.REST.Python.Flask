import os

# Collections Name on MongoDB
usersCollName = "users"
logsCollName = "logs"

# Detect if is running in Heroku
if 'DYNO' in os.environ:
    debug = False
    mongoConn = {
        "username": os.environ.get('MONGO_USERNAME'),
        "password": os.environ.get('MONGO_PASSWORD'),
        "host": os.environ.get('MONGO_HOST'),
        "port": os.environ.get('MONGO_PORT'),
        "db_name": os.environ.get('MONGO_DB_NAME')
    }
    print("\t -> Running on Heroku.")
# Else use Windows User Enviroment Vars
else:
    debug = True
    mongoConn = {
        "username": os.environ.get('MONGO_USERNAME_MLAB_DEV'),
        "password": os.environ.get('MONGO_PASSWORD_MLAB_DEV'),
        "host": os.environ.get('MONGO_HOST_MLAB_DEV'),
        "port": os.environ.get('MONGO_PORT_MLAB_DEV'),
        "db_name": os.environ.get('MONGO_DB_NAME_MLAB_DEV')
    }
    print("\t -> Running Locally.")