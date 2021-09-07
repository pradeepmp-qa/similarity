from flask import Flask, render_template, request
# from textblob import TextBlob
import spacy
nlp = spacy.load('en_core_web_md')

# initialse the application
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('form.html')

@app.route('/submit' , methods = ["POST"])
def form_data():
   first_word = request.form.get('first_word')
   second_word = request.form.get('second_word')
   doc1 = nlp(first_word)
   doc2 = nlp(second_word)
   score = doc1.similarity(doc2)
   if score >= 0.7:
       out = 'Similar'
   elif score < 0.7:
       out = 'Dissimilar'
   
   
   return render_template('predict.html' , corrected_data = f' {out}')
#    return render_template('predict.html' , sentence_data = f'Number of sentences are {sentence_length}')
if __name__ == '__main__':
    app.run(debug = True)
    # app.run(host = '0.0.0.0',port = 8080)

