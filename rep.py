"""
rep.py - willie/sopel-compatible clone of a mIRC script
Copyright 2015 dgw
"""

from willie import module


@module.commands('rep')
@module.example(".rep johnnytwothumbs")
def rep(bot, trigger):
    if not trigger.group(3):
        bot.reply("No user specified.")
        return
    target = trigger.group(3)
    rep = bot.db.get_nick_value(target, 'rep_score')
    if not rep:
        bot.say("%s has no reputation score yet." % target)
        return
    bot.say("%s's current reputation score is %d." % (target, rep))
