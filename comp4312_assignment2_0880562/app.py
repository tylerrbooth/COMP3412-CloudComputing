# -*- coding: utf-8 -*-
"""
@author duytinvo
"""
import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
import signal
import datetime
import sys
from storage_list_files import return_blobs
from storage_create_bucket import create_bucket
from storage_delete_bucket import delete_bucket

# define the app
DebuggingOn = bool(os.getenv('DEBUG', False))  # Whether the Flask app is run in debugging mode, or not.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'comp4312'
CORS(app)  # needed for cross-domain requests, allow everything by default


def sigterm_handler(_signo, _stack_frame):
    print(str(datetime.datetime.now()) + ': Received SIGTERM')


def sigint_handler(_signo, _stack_frame):
    print(str(datetime.datetime.now()) + ': Received SIGINT')
    sys.exit(0)


signal.signal(signal.SIGTERM, sigterm_handler)
signal.signal(signal.SIGINT, sigint_handler)


# HTTP Errors handlers
@app.errorhandler(404)
def url_error(e):
    return """
    Wrong URL!
    <pre>{}</pre>""".format(e), 404


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


@app.route('/health')
def check_health():
    response = app.response_class(
        response="",
        status=200,
        mimetype='application/json')
    return response


@app.route('/')
def index():
    return """<h1 style='color:blue'>Welcome to COMP4312 - Cloud Computing</h1>"""


@app.route('/list_files', methods=['GET'])
def list_files():
    """
        http://127.0.0.1:8080/list_files?bucket_name=comp4312_0880562
    """
    try:
        bucket_name = request.args.get('bucket_name', default='comp4312_0880562', type=str)
        file_names = []
        #####################
        # Your code is here #
        ####################
        # Hint: extract all files in bucket_name and assign to file_names

        #uses return_blobs from storage_list_files and adds to list file_names
        file_names = return_blobs(bucket_name)
        
        #assigns filenames and returns result
        result = jsonify(file_names)
        return result
    except:
        return "Invalid bucket name"


@app.route('/create_bk', methods=['GET'])
def create_bk():
    """
        http://127.0.0.1:8080/create_bk?bucket_name=comp4312_assign2_0880562
    """
    try:
        bucket_name = ""
        #####################
        # Your code is here #
        ####################
        # Hint: obtain bucket_name then call a function to create a bucket named bucket_name

        # gets the bucket name (bucket from storage_upload_files_sln)
        bucket_name = request.args.get('bucket_name', default='comp4312_0880562', type=str)
        # creates the bucket using create_bucket in storage_create_bucket
        create_bucket(bucket_name=bucket_name)
        

        return "Bucket {} created".format(bucket_name)
    except:
        return "Bucket name is either existing or invalid format"


@app.route('/delete_bk', methods=['GET'])
def delete_bk():
    """
        http://127.0.0.1:8080/delete_bk?bucket_name=comp4312_assign2_0880562
    """
    try:
        bucket_name = ""
        #####################
        # Your code is here #
        ####################
        # Hint: obtain bucket_name then call a function to delete a bucket named bucket_name
        
        #gets the bucket name
        bucket_name = request.args.get('bucket_name', default='comp4312_assign2_0880562', type=str)
        
        #deletes the bucket using delete_bucket from storage_delete_bucket
        delete_bucket(bucket_name=bucket_name, force=True)
        return "Bucket deleted successfully"

    except:
        return "Invalid bucket name"


if __name__ == '__main__':
    """
    kill -9 $(lsof -i:5000 -t) 2> /dev/null
    """
    # app.run(debug=True)
    app.run(host='127.0.0.1', port=8080, debug=True)
