from flask import Flask, render_template,redirect, request
import pandas as pd
import pickle


app = Flask(__name__)


def text_splitter(text): #without this function vectorizer.pkl can't be loaded
  return text.split()

def vect_to_lable(v):
    global y_list
    l = []
    for i in range(len(v)):
        if v[i] == 1:
            l.append(y_list[i])
    return l

def pred(user_input):
    user_input_vect = vectorizer_saved.transform(user_input)
    pred_result = model_saved.predict(user_input_vect)
    pred_result = pred_result.toarray()
    pred_result= pred_result.tolist()
    pred_result = vect_to_lable(pred_result[0])
    return pred_result

f = open("vectorizer1.pkl","rb")
vectorizer_saved = pickle.load(f)

f = open("tag_predictor_model.pkl",'rb')
model_saved = pickle.load(f)

y_list = pd.read_csv("All_tags.csv")
y_list = y_list['Tags'].tolist()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    features = [x for x in request.form.values()]
    features = [features[0] + " " + features [1]]
    output = pred(features)

    return render_template('index.html', prediction_text='The Predicted Tag For the given Question : {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)