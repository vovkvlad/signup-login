from flask import send_from_directory, send_file
from server.db.user import create_user, authenticate_user

def register_routes(app):
    @app.route('/')
    def index():
        return 'Hello world'

    @app.route('/login')
    def login():
        return 'Login'

    @app.route('/signup')
    def signup():
        return send_file('../../front-end/pages/signup.html')

    @app.route('/public/<path:path>')
    def host_static(path):
        return send_from_directory('../../front-end/public', path)

    #this is demo routes - should be deleted later
    @app.route('/user/create')
    def create_user_request():
        create_user('testemailAAAAA@gamil.com', 'password123')
        return 'User should have been created'

    @app.route('/user/auth')
    def authenticate_user_request():
        try:
            user = authenticate_user('testemailAAAAA@gamil.com', 'password12344')
            return user['email']

        except LookupError as err:
            print(err)
            return err.args[0]
