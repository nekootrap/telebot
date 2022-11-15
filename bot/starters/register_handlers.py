from handlers.default import send_help, exo


def register_all_handlers(bot):
    bot.register_message_handler(
        send_help,
        commands = ['start', 'help']
    )

    bot.register_message_handler(
        exo,
        func=lambda m: True
    )

    return bot