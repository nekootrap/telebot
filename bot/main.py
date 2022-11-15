from starters.add_bot import bot
from starters.register_handlers import register_all_handlers


bot = register_all_handlers(bot)

#я тебя люблю

bot.infinity_polling(skip_pending=True)