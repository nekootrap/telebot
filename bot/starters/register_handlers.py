from handlers.default import send_help, exo, bread, season, weather, guess_the_number


def register_all_handlers(bot):
    bot.register_message_handler(
        send_help,
        commands=['start', 'help']
    )
    
    bot.register_message_handler(
        season,
        commands=['сезон']
    )

    bot.register_message_handler(
        weather,
        commands=['w', 'погода', 'п']
    )

    bot.register_message_handler(
        bread,
        func=lambda m: m.text in ('да', 'Да')
    )
    
    bot.register_message_handler(
        guess_the_number,
        func=lambda x: True
    )
    # bot.register_message_handler(
    #     exo,
    #     func=lambda m: True
        
    # )

    return bot