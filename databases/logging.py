from aiogram import Dispatcher, types
from create_bot import dp
import sqlite3
from typing import final

# Логирование 
def recording_log(message : types.Message):
    try:
        conn = sqlite3.connect("dbTelegram_bot.db")
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO messages_from_users ('user_id', 'message') VALUES (?, ?)""",
        (message.from_user.id, message.text)
        )
        conn.commit()
    except sqlite3.Error as error:
        print("Error", error)
    finally:
        if(conn):
            conn.close()
