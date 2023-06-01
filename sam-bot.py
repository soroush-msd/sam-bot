import praw


sam_bot = praw.Reddit('sam-bot')

ds = sam_bot.subreddit("DeathStranding")

with open("replied.txt", "a+") as f:
    f.seek(0)
    replied = (f.read()).split("\n")
    # add for body as well
    # add object detection
    for news in ds.new(limit=25):
        if news.id not in replied:
            if ("my" and "birthday") in (news.title).lower():
                f.write(news.id + "\n")
                #print(news.title)
                news.reply("Happy Birthday " + str(news.author) + "!" + "\n\n" + "Keep on keepin' on!")    

