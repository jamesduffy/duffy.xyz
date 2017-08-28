"""Create the core duffyxyz website."""
import os
from datetime import datetime

from flask import Flask, render_template, url_for

from duffyxyz.views.pages import pages
from duffyxyz.views.writings import writings
# from duffyxyz.views.photos import photos


CONFIG_MODULE = os.getenv('CONFIG_MODULE', 'duffyxyz.config.local')


# Create the app and load the configuration
app = Flask(__name__)
app.config.from_object(CONFIG_MODULE)

# Register the different parts of the app
app.register_blueprint(pages)
app.register_blueprint(writings, url_prefix='/writings')
# app.register_blueprint(photos, url_prefix='/photos')


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.errorhandler(404)
def error_not_found(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def error_server(error):
    if error.description:
        message = error.description
    else:
        message = 'The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.'
    return render_template('errors/500.html', message=message), 500


@app.context_processor
def override_url_for():
    """Date url for cache busting."""
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    """Decide if we need to add modified time to file."""
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
