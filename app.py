from flask import Flask, render_template, request, redirect, url_for, flash
from prisma import Prisma

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for flash messages

db = Prisma()
db.connect()

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        if not name or not email:
            flash('Please fill out all fields', 'error')
        else:
            try:
                user = db.user.create({
                    'name': name,
                    'email': email
                })
                return render_template('thank_you.html', name=name)
            except Exception as e:
                flash(f'Error: {str(e)}', 'error')

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)