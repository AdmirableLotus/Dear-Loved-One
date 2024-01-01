from flask import Flask, render_template
app = Flask(__name__)
# Route for the home page (index.html)
@app.route('/')
def index():
    return render_template('index.html')
# Route for the login/signup page
@app.route('/login_signup')
def login_signup():
    return render_template('login_signup.html')
# Route for the "Dear Loved One" page
@app.route('/dear_loved_one')
def dear_loved_one():
    return render_template('dear_loved_one.html')
# Add more routes as needed
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080, debug = True)