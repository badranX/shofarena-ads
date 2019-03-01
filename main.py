import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'development')

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    pass
    #app.run()