from textblob import TextBlob


def sentiment_analysis(text):
        blob = TextBlob(text)
        pol = blob.sentiment.polarity
        if pol > 0:
            return 'Positive'
        elif pol < 0:
            return 'Negative'
        else:
            return 'Zero'


if __name__ == '__main__':
    print(sentiment_analysis('You are not bad'))
