import praw
import re
import requests

def run_bot():
    bot_message_disclaimer = "\n\n &nbsp; \n *** \n ^(*Beep boop. I am a bot, and this action was performed automatically.*)"
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit("kjfacts")
    replied_comments = []


    with open("replied_comments.txt", "r") as f:
        replied_comments = f.read()
        replied_comments = replied_comments.split("\n")
        replied_comments = list(filter(None, replied_comments))

    for comment in subreddit.stream.comments():
        if comment.id not in replied_comments:
            if re.search("u/kaj-bot", comment.body, re.IGNORECASE):
                response = requests.get("https://kjfacts.herokuapp.com/api/1")
                comment.reply(response.json()[0] + bot_message_disclaimer)
                replied_comments.append(comment.id)

                with open("replied_comments.txt", "w") as f:
                    for comment_id in replied_comments:
                        f.write(comment_id + "\n")

def main():
    run_bot()


if __name__ == "__main__":
    main()