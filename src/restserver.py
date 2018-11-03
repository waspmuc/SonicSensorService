from flask import render_template
import connexion
import sensor
import threading
from pymemcache.client import base

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

thr = threading.Thread(target=sensor.read, args=(), kwargs={})
thr.daemon = True
client = base.Client(('localhost', 11211))
print client.set('some_key', 'some value')
print client.get('some_key')

thr.start() # Will run "foo"
print "thread.start() called"

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=False)
