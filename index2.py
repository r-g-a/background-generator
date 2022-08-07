from flask import Flask, render_template, url_for, request, redirect 
app = Flask(__name__) # name of the app
print(__name__)  # name is __main__ here

# @app.route('/')  # gives extra tools to build a server like a decorator
# def hello_world():
#     return 'Hello, MasterData!'

@app.route('/')  
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')  
def html_page(page_name):
    return render_template(page_name)

# @app.route('/index.html')  
# def Home():
#     return render_template('index.html')

# @app.route('/about.html')  
# def about():
#      return render_template('about.html')

# @app.route('/contact.html')  
# def contact():
#      return render_template('contact.html')

# @app.route('/components.html')  
# def components():
#      return render_template('components.html')


# @app.route('/works.html')  
# def works():
#      return render_template('works.html')

def write_to_file(data):
     with open('database.txt',mode='r') as database:
         email = data["email"]
         subject = data["subject"]
         message = data["message"]
         file = database.write(f'\n{email},{subject},{message}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    #request.setHeader("Content-Type","application/json")
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong try again!!'