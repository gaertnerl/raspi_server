from .__init__ import app
from flask import jsonify, request, make_response

@app.route('/api')
def api_information():
    return 'welcome to esketch_api'

@app.route('/api/login')
def login():
    auth = request.authorization

    if auth and auth.password == '':
        pass

    return make_response('Could not verfiy', 401,
                         {})