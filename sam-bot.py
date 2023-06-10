import praw


sam_bot = praw.Reddit('sam-bot')

ds = sam_bot.subreddit("DeathStranding")

with open("replied.txt", "a+") as f:
    f.seek(0)
    replied = (f.read()).split("\n")
    # add for body
    # add object detection - check url for img clues
    for news in ds.new(limit=25):
        if news.id not in replied:
            key = (news.title).lower()
            if (("my" in key or "me" in key) and ("birthday" in key or "birth day" in key)):
                f.write(news.id + "\n")
                news.reply("Happy Birthday " + str(news.author) + "!" + "\n\n" + "Keep on keepin' on!")    

