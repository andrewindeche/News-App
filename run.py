from app import app
from .config import DevConfig

# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)

if __name__ == '__main__':
    app.run(debug = True)
