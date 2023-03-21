from flask import Flask
 
app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'Welcome To Kubernet Deployment for FLASK Application'
 
# main driver function
if __name__ == '__main__':
    app.run()