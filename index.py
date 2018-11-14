from firebase import firebase
from flask import Flask
from .forms import FirePut

app = Flask(__name__)
firebase = firebase.FirebaseApplication(‘<path tofirebase app>’, None)

@app.route('/')
def index():
    return "Hello world!"

@app.route('/testing')
def testing():
    return "testing"

count = 0

@app.route('/api/put', methods=['GET', 'POST'])
def fireput():
    frm = FirePut()
    if form.validate_on_submit():
        count += 1
        putData = {'Title': form.title.data, 'Year' : form.year.data, 'Rating' : form.rating.data}
        firebase.put('/films', 'film' +str(count), putData)
        return render_template('api-put-resulthtml', form=form, putData=putData)
    return render_template('My-form.html')

if __name__ 00 '__main__':
    app.run(debug=True)
