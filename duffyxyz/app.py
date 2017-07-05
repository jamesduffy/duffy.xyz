"""Create the core duffyxyz website."""
import os
from datetime import datetime

from flask import Flask, render_template

from duffyxyz.views.pages import pages
from duffyxyz.views.writings import writings
from duffyxyz.views.photos import photos


CONFIG_MODULE = os.getenv('CONFIG_MODULE', 'duffyxyz.config.local')


# Create the app and load the configuration
app = Flask(__name__)
app.config.from_object(CONFIG_MODULE)

# Register the different parts of the app
app.register_blueprint(pages)
app.register_blueprint(writings, url_prefix='/writings')
app.register_blueprint(photos, url_prefix='/photos')


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404
