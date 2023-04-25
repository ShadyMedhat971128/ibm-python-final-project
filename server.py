import machinetranslation
import machinetranslation.translator
from machinetranslation.translator import english_to_french,french_to_english
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return english_to_french(textToTranslate)
    

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return french_to_english(textToTranslate)

@app.route("/")
def renderIndexPage():
    """
    implement a method that renders the mywebscript.js from static folder
    """
    # render index.html from templates folder
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
