# by BlogChik
# https://github.com/blogchik

from pyrogram import Client, filters
from time import sleep

api_id = 1234       # API ID-ni kiriting
api_hash = "ABCD"   # API HASH-ni kiriting

app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.command("magic", prefixes=".") & filters.me)
def hack(_, msg):
    hearts = [
        "🤍",
        "🤍🤍",
        "🤍🤍🤍",
        "🤍🤍🤍🤍",
        "🤍🤍🤍🤍🤍",
        "🤍🤍🤍🤍🤍🤍",
        "🤍🤍🤍🤍🤍🤍🤍",
        "🤍🤍🤍🤍🤍🤍🤍🤍",
        "🤍🤍🤍🤍🤍🤍🤍🤍🤍",
        "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍",
        "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍",
        "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍",
        "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍",
        "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍",
        "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍",
        "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍",
        "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍",
        "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍",
        "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍",
        "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍",
        "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍",
        "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍",
        "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💖💖🤍💖💖🤍🤍\n🤍💖💖💖💖💖💖💖🤍\n🤍💖💖💖💖💖💖💖🤍\n🤍💖💖💖💖💖💖💖🤍\n🤍🤍💖💖💖💖💖🤍🤍\n🤍🤍🤍💖💖💖🤍🤍🤍\n🤍🤍🤍🤍💖🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍",
        "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡💛🤍💙💜🤍🤍\n🤍❤️❤️🖤💖🤎💚💛🤍\n🤍💙💜💛💚❤️🤎💙🤍\n🤍💖🤎🖤💖💙💛💖🤍\n🤍🤍💚❤️💜🖤💖🤍🤍\n🤍🤍🤍💖🤎💚🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍",
        "<b>I ❤️</b>",
        "<b>I L ❤️</b>",
        "<b>I LO ❤️</b>",
        "<b>I LOV ❤️</b>",
        "<b>I LOVE ❤️</b>",
        "<b>I LOVE Y ❤️</b>",
        "<b>I LOVE YO ❤️</b>",
        "<b>I LOVE YOU❤️</b>",
        "<b>I LOVE YOU ❤️</b>",
        "<b>I LOVE YO ❤️</b>",
        "<b>I LOVE Y ❤️</b>",
        "<b>I LOVE ❤️</b>",
        "<b>I LOV ❤️</b>",
        "<b>I LO ❤️</b>",
        "<b>I L ❤️</b>",
        "<b>I ❤️</b>",
        "<b>I ❤️ U</b>",
        "<b>I ❤️ U!</b>"
    ]
    
    for heart in hearts:
        msg.edit(heart)
        sleep(0.1)

app.run()

# by BlogChik
# https://github.com/blogchik
