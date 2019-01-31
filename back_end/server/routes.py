def register_routes(app):
    @app.route('/')
    def index():
        return 'Hello world'

    @app.route('/login')
    def login():
        return 'Login'

    @app.route('/signup')
    def signup():
        return 'signup'
