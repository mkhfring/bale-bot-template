import os


class BotConfig:

    token = os.environ.get(
        'BOT_TOKEN',
        '1520084492:4e0a8824f7fc9e06fa953d57a23f9a59d1c509e8'
    )

    database_url = os.environ.get('database', 'sqlite:////home/mohamad/workspace/bot_template/bot_template/vip_practicedb.db')
    report_mode = os.environ.get('REPORT_MODE', 'database')
    database_string=os.environ.get(
        'DB_STRING',
        'ACCOFFDB, localhost, 50000, db2inst1, db2inst1-pwd'
    )
    database_string = database_string.split(', ')
