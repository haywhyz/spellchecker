from flask import Flask,request,json,jsonify
from spellchecker import SpellChecker
app = Flask(__name__)             # create an app instance
app.secret_key = 'b_5#y2L"F4Q8zxec]/'

def set_default(obj): #convert set to list
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

@app.route('/api/v1/spellchecker/<string:text>', methods=['GET'])
def spell_checker(text):
    split_sen = []
    sentence = [text]
    split_sen = [i for item in sentence for i in item.split()]
    spell = SpellChecker()

    # find those words that may be misspelled
    misspelled = spell.unknown(split_sen)
    suggestions = []
    likely_correct = []
    for word in misspelled:
        # Get the one `most likely` answer
        likely_correct.append(spell.correction(word))

        # Get a list of `likely` options
        suggestions.append(spell.candidates(word))
    a_dict = dict()

    a_dict['suggestions'] = suggestions
    a_dict['misspelled'] = misspelled
    a_dict['likely_correct'] = likely_correct

    return json.dumps(a_dict, default=set_default)
if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)