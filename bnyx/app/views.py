from flask import Flask , render_template , request


app = Flask(__name__)


@app.route("/")
def Definition():
    return render_template("index.html")



@app.route('/tahmin', methods=['GET', 'POST'])
def predict():
    yas = float(request.form.get('yaş', False))

    cinsiyet = float(request.form.get('cinsiyet', False))

    kolestrol = float(request.form.get('kolestrol', False))

    thalach = float(request.form.get('thalachh', False))

    kanBasinci = float(request.form.get('kanBasinci', False))

    kanSekeri = float(request.form.get('kanSekeri', False))

    agriTipi = float(request.form.get('agriTipi', False))

    arr = np.array([[yas, cinsiyet, kolestrol, thalach, kanBasinci, kanSekeri, agriTipi]])
    pred = model.predict(arr)
    if pred == 0:
        res_Val = "No heart problem,Your Doing Good"
    else:
        res_Val = "Heart Problem,You may have to give extra care towards your health"

    return render_template('index.html', prediction_text='Patient has {}'.format(res_Val))
