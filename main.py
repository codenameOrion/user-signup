from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 



@app.route("/validator", methods=['POST'])
def validator():
    
    
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    #welcome_page = render_template('welcome.html', username=username)
    is_error = False
    
    error_user = ''
    error_pass = ''
    error_pass_val = ''
    error_email = ''

    #if request.method == 'POST':
      
    
    if len(username) < 3 or len(username) > 20 or ' ' in username:
        error_user = "That's not a valid username"
        is_error = True
    if len(password) < 3 or len(password) > 20 or ' ' in username:
        error_pass = "That's not a valid password"
        is_error = True
    if verify != password:
        error_pass_val = "Password does not match"
        is_error = True
    #elif email == '':
        #return welcome_page
    if email != '' and ('@' not in email or len(email) < 3 or len(email) > 20 or ' ' in email):
        error_email = "Not a valid email"
        is_error = True
    if is_error == False:
        #return render_template('form.html', error_user=error_user, error_pass=error_pass, error_pass_val=error_pass_val)
        return render_template('welcome.html', username=username)
    else:
        
        return render_template('form.html', username=username, password=password, email=email, error_user=error_user, error_pass=error_pass, error_pass_val=error_pass_val, error_email=error_email )


    return render_template('form.html', username=username, password=password)
       

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)



@app.route("/")
def index():
    encoded_user = request.args.get("username")
    encoded_password = request.args.get("password")
    encoded_error_user = request.args.get("error_user")
    encoded_error_pass = request.args.get("error_pass")
    encoded_error_pass_val = request.args.get("error_pass_val")
    encoded_error_email = request.args.get("error_email")
    
    return render_template('form.html', error_user=encoded_error_user, error_pass=encoded_error_pass, error_pass_val=encoded_error_pass_val, error_email=encoded_error_email)


if __name__ == "__main__":

    app.run()