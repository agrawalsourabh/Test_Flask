from flask import Flask, render_template,session
from forms import RegistrationForms

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

@app.route('/')
def index():
    sum = 2 + 4
    return render_template('index.html', sum=sum)


@app.route('/registration', methods=('GET', 'POST'))
def registration():
    form = RegistrationForms()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data

        data = {
            "first_name": first_name,
            "last_name" : last_name,
            "email":    email
        }

        return render_template('display.html', data=data)

    return render_template('form.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)