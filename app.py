from flask import Flask, render_template, request
import pickle

app= Flask(__name__)
model= pickle.load(open("model/Email_Spam_Detection_Model.pkl", 'rb'))
tf= pickle.load(open("model/tf.pkl", 'rb'))

@app.route("/")
def home():
    return render_template("index.html")

# Initialize predictions to a neutral value
predictions= -1

@app.route("/predict", methods= ["POST"])
def predict():
    email= request.form.get('content')
    tokenized_email= tf.transform([email])
    predictions= model.predict(tokenized_email)

    # ham mail=1, spam=0
    predictions = 1 if predictions == 1 else -1
    return render_template("index.html", predictions= predictions, email= email)

if __name__== "__main__":
    app.run(host= "0.0.0.0", port=8080, debug=True)
