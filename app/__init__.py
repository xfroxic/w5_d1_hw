from flask import Flask
from config import Config

# __name__ is a predefined variable in Python, which is set to the name of the module in which it's used
# passing __name__ almost always configures Flask in the correct way
app = Flask(__name__)
app.config.from_object(Config)

# importing routes at the bottom of the script helps avoid circular imports
from app import routes