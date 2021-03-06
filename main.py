from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import nltk
nltk.download('punkt')
app = Flask(__name__)
@app.route('/') # default route
def new():
  return render_template('index.html') # 
@app.route('/predict', methods = ['POST']) # /result route
def predict():
  name = request.form['name']
  blob = TextBlob(name)
  for sentence in blob.sentences:
    result = sentence.sentiment.polarity
  if result>0:
    result=str(int(result*100))+"% Positive"
  elif result<0:
    result=str(int(abs(result)*100))+"% Negative"
  else:
    result="Neutral" # result = polarity value
  return jsonify(result = result)
if __name__ == '__main__':
  app.debug = True
  app.run()