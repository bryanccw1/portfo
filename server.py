from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

import csv

@ app.route('/index.html')
def my_home():
	return render_template('index.html') #this looks for folder named "templates" for the parameter file
# 1. Used "set FLASK_APP=server.py" command to tie server with flask
# 2. Used "set FLASK_ENV=development" command to turn on debug mode
# 3. All changes are saved and server is automatically updated without running server again


@ app.route('/about.html')
def about():
	return render_template('about.html')

# can have different routes

# Usually the CSS and JS files are static files. 
# We have to create a "static" folder for them

# @ app.route('/works.html')
# def work():
# 	return render_template('works.html')

# @ app.route('/contact.html')
# def contact():
# 	return render_template('contact.html')

# @ app.route('/components.html')
# def components():
# 	return render_template('components.html')

# Can set up the routes to change dynamically instead of setting up individual ones like above
@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)


def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv',mode='a',newline='') as database2:

		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		#according to csv module #values will be separated by a delimiter
		#newline - this way we always add a new line when we append
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	try:
	    	data = request.form.to_dict() #return the form as dictionary
	    	print(data) #print it in the cmd to make sure it's working
	    	write_to_csv(data) # I can write to file or to csv now
	    	return redirect('/thankyou.html')
	    except:
	    	return 'Did not save to database'
    else:
    	return 'Something went wrong. Try again.'



# # Variable Rules

# @ app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None): #None as default
# 	return render_template('server.html',name=username, post_id=post_id)

# this reads the URL and pass info into the web