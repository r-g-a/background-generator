from flask import Flask
from gevent.pywsgi import WSGIServer
from flask import Flask, render_template, url_for, request, redirect 

app = Flask(__name__)

if __name__=='__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()    

print(__name__)  # name is __main__ here


@app.route('/')  
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')  
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
     with open('database.txt',mode='a') as database:
         email = data["email"]
         subject = data["subject"]
         message = data["message"]
         file = database.write(f'\n{email},{subject},{message}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    #content = request.get_json()
    #request.setHeader("Content-Type","application/json")
    if request.method == 'POST':
        #data = request.form.to_dict()
        data = request.get_json(force=True)
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong try again!!'