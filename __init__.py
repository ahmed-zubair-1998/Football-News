import os, requests, praw

from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        r = requests.get('https://newsapi.org/v2/everything?sources=bbc-sport&from=2018-10-3&sortBy=popularity&q=football&apiKey=69f140fb78274a1e9a63c50aa8ccf82e')
        res = r.json()
        arr = []
        for article in res['articles']:
            if 'football' in article['url']:
                arr.append(article)

        return render_template('index.html', arr = arr)

    @app.route('/community')
    def community():
        reddit = praw.Reddit(client_id='miObOoT6nCtceA',
                     client_secret='oz7762iyqTS7bYp-8ZXZQmIyCPc',
                     user_agent='AhmedZubairGCU/0.1')
        res = reddit.subreddit('soccer').hot(limit=50)

        

        return render_template('community.html', results = res)
        
        

    return app
