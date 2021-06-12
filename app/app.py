from flask import Flask, request, json
import requests
import logging
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/info')
def info():
    """Info endpoint returning a status or info 
    This is using docstrings for specifications.
    ---
    responses:
      200:
        description: Receiver info static JSON will be returned
        examples:
          /info
    """

    response = app.response_class(
            response=json.dumps({"Receiver": "Cisco is the best!"}),
            status=200,
            mimetype='application/json'
    )

    app.logger.info('Info request successfull')
    return response

@app.route('/ping', methods=['POST'])
def ping():    
    """Ping endpoint returning the payload it will get from url passed 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: body
        in: body
        type: json
        default: {'url' : 'https://google.com'}
        description: Url for the specific website someone wants to get payload
        schema:
          url: Product
          required:
            - url
          properties:
            url :
              type: string
              description: WebSite Url
              default: "https://google.com"
    definitions:
      Url:
        type: string
        description: WebSite Url
        default: "https://google.com"

    responses:
      200:
        description: Returns payload for the specific url passed 
        examples:
          {'url' : 'https://google.com' }
    """

    if request.method == "POST":        
        req = requests.get(str(request.json['url']).replace("https", "http"))
        app.logger.info('Ping request successfull')
        return app.response_class(
            response=req.text,
            status=req.status_code,
            content_type=req.headers['content-type']
        )

@app.route("/")
def hello():
    app.logger.info('Root request successfull')
    return "Project Running"

if __name__ == "__main__":
    ## stream logs to a file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)    
    app.run(host='0.0.0.0', debug=True)
