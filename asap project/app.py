import random

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    s = ['''Astronomy compels the soul to look upward, and leads us from this world to another.''',
         '''True, we love life, not because we are used to living, but because we are used to loving. There is always s\
         ome madness in love, but there is also always some reason in madness.''',
         '''Life is full of beauty. Notice it. Notice the bumble bee, the small child, and the smiling faces. Smell the\
         rain, and feel the wind. Live your life to the fullest potential, and fight for your dreams.''',
         '''Too often we underestimate the power of a touch,a smile, a kind word,a listening ear, an honest compliment,\
         the smallest act of caring, all of which have the potential to turn a life around.''',
         '''Sing like no one’s listening, love like you’ve never been hurt, dance like nobody’s watching, and live like\
          it’s heaven on earth.''',
         '''Anyone who has never made a mistake has never tried anything new.''']
    string = list(s)[random.randint(0, len(s) - 1)]
    return render_template("index.html", text=string)


@app.route('/check_text', methods=['POST'])
def check_text():
    error = []
    matching = []
    place = []
    string = request.form.get("init_text")
    text = request.form.get("text")
    time_taken = int(request.form.get("time_taken"))
    wordcount = len(string.split())
    wordcount2 = len(text.split())
    print(wordcount2)
    wpm = wordcount / time_taken

    if len(string) != len(text) and len(string) > len(text) or len(string) == len(text):
        for i in range(len(text)):
            if string[i] == text[i]:
                matching.append(text[i])
            elif string[i] != text[i]:
                error.append(text[i])
                place.append(i)
    return {
        "wordcount": wordcount,
        "wordcount2": wordcount2,
        "wpm": wpm,
        "error": error,
        "non": matching,
        "place": place,
        "typed_length": len(text),
        "checked_length": len(string)
    }


if __name__ == "__main__":
    app.run(debug=True)
