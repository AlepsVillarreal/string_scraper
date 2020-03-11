#! usr/bin/env python3
import praw
import pandas as pd
from datetime import datetime
import pprint
from collections import Counter
import re
from credentials import personal_use, secret, reddit_app_name, reddit_user_name, password
import matplotlib.pyplot as plt
import seaborn as sns
import os

class Streamer():
    def __init__():
        pass

    def connect_reddit_api(self, client_id, client_secret, user_agent, username, passwd):
        # Create a praw reddit object
        reddit = praw.Reddit(client_id=self.client_id,
                             client_secret=self.client_secret,
                             user_agent=self.user_agent,
                             username=self.username,
                             password=self.passwd)
        return reddit


    def choose_subreddits(self, subreddit_list, reddit_object):
        subr_list = [reddit_object.subreddit(element) for element in subreddit_list]
        return subr_list


    def get_comment_df(self):

        return pd.DataFrame(comment_skeleton)

    def get_word_count_df(self, word_counter_skeleton):
        return pd.DataFrame(word_counter_skeleton)


    def look_for_word_in_list_of_subreddits(self, word, comment_dict, word_counter_Df, subrList, reddit):
        # Create a regex object to look for any mention of amlo
        pattern = re.compile(word, re.IGNORECASE)

        for comment in subrList[0].stream.comments():
            # print (comment.body)
            if len(comment.body) > 0:
                if re.search(pattern, comment.body):
                    # Eliminate all non alphanumerical characters from the message
                    re.sub(r'\W+', '', comment.body)
                    print(comment.body)
                    parent_id = str(comment.parent())
                    original = reddit.comment(parent_id)
                    comment_dict["parent_id"].append(str(comment.parent()))
                    comment_dict["original"].append(original)
                    comment_dict["body"].append(comment.body)


# Start of the program
if __name__ == '__main__':
    stream = Streamer()
    word_counter_skeleton = {"word": [],
                             "counter": []
                             }
    comment_skeleton = {"parent_id": [],
                        "original": [],
                        "body": [],
                        }

    stream.connect_reddit_api(personal_use, secret, reddit_app_name, reddit_user_name, password)