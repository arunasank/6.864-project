import os
import requests
import pandas as pd
from datetime import datetime
from tqdm import tqdm
import numpy as np
import time


def post_tweets(tweet_ids, bearer_token, tweet_fields=None):
    joined_ids = ','.join([str(t) for t in tweet_ids])
    if tweet_fields is None:
        tweet_fields = ['id', 'text']
    headers = {'Authorization': 'Bearer ' + bearer_token}
    url = 'https://api.twitter.com/2/tweets?ids=' + joined_ids + '&tweet.fields=' + ','.join(tweet_fields)
    payload={}
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


if __name__ == '__main__':
    bearer_token = os.getenv('BEARER_TOKEN')
    birdwatch_notes = pd.read_table('https://ton.twimg.com/birdwatch-public-data/notes/G1OLUMSOO3MEDURGVDURV6IKQ2Q1YBSOA4O03ETC2DFTM767AAVCVQE7JNMG/notes-00000.tsv')
    birdwatch_tweets = birdwatch_notes['tweetId'].unique()
    max_n_tweets = 100  # rate limit
    n_groups = np.ceil(len(birdwatch_tweets)/max_n_tweets)
    tweet_df_list = []
    for tweet_ids in tqdm(np.array_split(birdwatch_tweets, n_groups)):
        tweet_dict = post_tweets(tweet_ids, bearer_token,
                                 tweet_fields=['author_id', 'id', 'text', 'created_at', 'lang', 'public_metrics',
                                               'possibly_sensitive'])
        tweet_df = pd.json_normalize(tweet_dict['data'])
        tweet_df_list.append(tweet_df)
        time.sleep(1)
    all_tweet_df = pd.concat(tweet_df_list).reset_index(drop=True)
    all_tweet_df.to_csv(path_or_buf='../data/raw/' + 'tweet_text' +
                                    datetime.today().strftime('%Y-%m-%d') + '.csv',
                        index=False)
