import nekos

from ..utils import admin_cmd, edit_or_reply


@bot.on(admin_cmd(pattern="tcat$"))
async def hmm(cat):
    if cat.fwd_from:
        return
    reactcat = nekos.textcat()
    await edit_or_reply(cat, reactcat)


@bot.on(admin_cmd(pattern="why$"))
async def hmm(cat):
    if cat.fwd_from:
        return
    whycat = nekos.why()
    await edit_or_reply(cat, whycat)


@bot.on(admin_cmd(pattern="fact$"))
async def hmm(cat):
    if cat.fwd_from:
        return
    factcat = nekos.fact()
    await edit_or_reply(cat, factcat)
