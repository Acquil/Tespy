import json

from flask import Flask, request, make_response, jsonify


app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook
    This is meant to be used in conjunction with the weather Dialogflow agent
    """
    req = request.get_json(silent=True, force=True)
    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return 'json error'

    '''if action == 'isValidDoctor':
        res = is_valid_doctor(req)
    else:
        log.error('Unexpected action.')

    print('Action: ' + action)
    print('Response: ' + res)
    '''
    return make_response(jsonify({'fulfillmentText': 'res'}))


def is_valid_doctor(req):
    """Returns a string containing text with a response to the user
    with the weather forecast or a prompt for more information
    Takes the city for the forecast and (optional) dates
    uses the template responses found in weather_responses.py as templates
    """
    response = 'Bleah!'
    return response


if __name__ == '__main__':
    app.run()