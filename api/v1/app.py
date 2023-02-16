from flask import Flask
from models import storage
from api.v1.views import app_views
from flaskCORS import CORS
import os

app = Flask(__name__)
app.register__blueprint(app_views)

def teardown_appcontext(self):
    """ a method to handle teardown to close """
    storage.close()


if __name__ == "__main__":
    app_host = os.getenv("HBNB_API_HOST", '0.0.0.0')
    app_port = int(os.getenv("HBNB_API_PORT", '5000'))
    app.run(host = app_host, port=app_port, threaded = True)