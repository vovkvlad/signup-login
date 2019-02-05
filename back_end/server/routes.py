from flask import send_from_directory, send_file

def register_routes(app):
    @app.route('/')
    def index():
        return 'Hello world'

    @app.route('/login')
    def login():
        return 'Login'

    @app.route('/signup')
    def signup():
        return send_file('../../front-end/sign_up.html')

    @app.route('/public/<path:path>')
    def host_static(path):
        return send_from_directory('../../front-end/public', path)
