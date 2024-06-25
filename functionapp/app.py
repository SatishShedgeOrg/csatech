from flask import request
from flask import Flask
import json

app=Flask(__name__)

@app.route('/')
def home_page():
    return 'Welcome to CSA Demo'

@app.route('/github',methods=['POST'])
def webhook_message():
    if request.headers['X-Github-Event']=='pull_request' :
        info=json.dumps(request.json)
        data = json.loads(info)
        print(data['action'])
        details=data["pull_request"]
        body=details['body']
        print(body)

    return "success"
    
if __name__=='__main__':
    app.run(debug=True,use_reloader=False)