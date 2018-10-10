from flask import Flask, request, render_template
from sentiment import sentiment_analysis

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sentiment', methods=['POST'])
def sentiment():
    text = ''
    try:
        data = request.get_json(force=True)
        text = data['text']
    except:
        text = str(request.data)
    result = sentiment_analysis(text)
    return result


if __name__ == '__main__':
    app.run(debug=True)

