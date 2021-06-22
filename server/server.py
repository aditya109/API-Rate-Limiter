import logging

from flask import Flask

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
# creating a logger instance
FORMAT = '%(asctime)s - %(levelname)s : %(message)s'
logging.basicConfig(filemode='w',
                    format=FORMAT)


# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'


@app.route('/result')
# '/result' URL is bound with get_result() function.
def get_result():
    return 'Received result'


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    host = "0.0.0.0"
    port = 5000
    logging.info('Starting server on {0} on PORT: {1}'.format(host, port))
    app.run(host=host, port=port, debug=False)
