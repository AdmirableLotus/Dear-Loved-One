from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page (home.html)
@app.route('/')
def home():
    return render_template('home.html')

# Route for the login/signup page (login_signup.html)
@app.route('/login_signup')
def login_signup():
    return render_template('login_signup.html')

# Route for the "Dear Loved One" page (journal.html)
@app.route('/journal')
def journal():
    return render_template('journal.html')

# Add more routes as needed

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
