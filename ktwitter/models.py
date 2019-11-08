import json
from pathlib import Path
import twitter
from ktwitter.keys import ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET

class Tracker():
    def __init__(self):
        self.api = twitter.Api(
            CONSUMER_KEY,
            CONSUMER_SECRET,
            ACCESS_TOKEN_KEY,
            ACCESS_TOKEN_SECRET,
        )
        self.download_dir = Path(__file__).parent / 'download'
    def get_images_from_fansite(self, screen_name):
        timeline = self.get_tweets(screen_name=screen_name)
        image_url_list = []
        if timeline:
            for tweet in timeline:
                if tweet.media:
                    for media in tweet.media:
                        image_url_list.append(media.media_url_https)
                else:
                    print('No media from https://twitter.com/{0}/status/{1}'.format(screen_name, tweet.id))
        else:
            print('No tweets from https://twitter.com/{}'.format(screen_name))
        print(image_url_list)
        
        # with open('timeline.json', 'w+') as f:
        #     for tweet in timeline:
        #         f.write(json.dumps(tweet._json))
        #         f.write('\n')

    def get_tweets(self, screen_name=None):
        timeline = self.api.GetUserTimeline(screen_name=screen_name, count=200)
        earliest_tweet = min(timeline, key=lambda x: x.id).id
        while True:
            tweets = self.api.GetUserTimeline(
                screen_name=screen_name,
                max_id=earliest_tweet,
                count=200,
            )
            new_earliest = min(tweets, key=lambda x: x.id).id
            if not tweets or new_earliest == earliest_tweet:
                break
            else:
                earliest_tweet = new_earliest
                timeline += tweets
        return timeline
