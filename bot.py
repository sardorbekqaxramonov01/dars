# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


# app = ApplicationBuilder().token("6079032773:AAGwOad6VfDMOqvMxsyIXJ0ac9z5j-SSktk").build()

# app.add_handler(CommandHandler("hello", hello))

# app.run_polling()










# import os

# os.remove("main.html")















#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

# import logging

# from telegram import __version__ as TG_VER

# try:
#     from telegram import __version_info__
# except ImportError:
#     __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

# if __version_info__ < (20, 0, 0, "alpha", 1):
#     raise RuntimeError(
#         f"This example is not compatible with your current PTB version {TG_VER}. To view the "
#         f"{TG_VER} version of this example, "
#         f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
#     )
# from telegram import ForceReply, Update
# from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# # Enable logging
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
# )
# logger = logging.getLogger(__name__)


# # Define a few command handlers. These usually take the two arguments update and
# # context.
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Send a message when the command /start is issued."""
#     user = update.effective_user
#     await update.message.reply_html(
#         rf"Hi {user.mention_html()}!",
#         reply_markup=ForceReply(selective=True),
#     )


# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Send a message when the command /help is issued."""
#     await update.message.reply_text("Help!")


# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Echo the user message."""
#     await update.message.reply_text(update.message.text)


# def main() -> None:
#     """Start the bot."""
#     # Create the Application and pass it your bot's token.
#     application = Application.builder().token("6079032773:AAGwOad6VfDMOqvMxsyIXJ0ac9z5j-SSktk").build()

#     # on different commands - answer in Telegram
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CommandHandler("help", help_command))

#     # on non command i.e message - echo the message on Telegram
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

#     # Run the bot until the user presses Ctrl-C
#     application.run_polling()


# if __name__ == "__main__":
#     main()








# import telegram

# print(telegram.__bot_api_version__) # 6.7
# print(telegram.__bot_api_version_info__) # 6.7

# print(telegram.__version__) # 20.3
# print(telegram.__version_info__) # 20.3








# text = "10"
# a = "Salom"
# print(text.isnumeric()) # True
# print(a.isnumeric()) # False










# import logging
# from telegram import ForceReply, Update
# from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# # Enable logging
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
# )
# logger = logging.getLogger(__name__)


# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Send a message when the command /start is issued."""
#     user = update.effective_user
#     await update.message.reply_html(
#         rf"Assalomu alaykum {user.mention_html()}!",
#         reply_markup=ForceReply(selective=True),
#     )


# async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Echo the user message."""
#     if update.message.text.isnumeric():
#        input_value = float(update.message.text) * 10
#     else:
#        input_value = "Son kiriting!"
    

#     await update.message.reply_text(str(input_value))


# def main() -> None:
#     """Start the bot."""
#     # Create the Application and pass it your bot's token.
#     application = Application.builder().token("6079032773:AAGwOad6VfDMOqvMxsyIXJ0ac9z5j-SSktk").build()

#     # on different commands - answer in Telegram
#     application.add_handler(CommandHandler("start", start))

#     # on non command i.e message - echo the message on Telegram
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calc))

#     # Run the bot until the user presses Ctrl-C
#     application.run_polling()


# if __name__ == "__main__":
#     main()









# try:
#     son = 10
#     print(son / 0)

# except ZeroDivisionError as err:
#     print(err)

# except TypeError:
#     print("Qiymatda xato bor!")

# except NameError:
#     print("Nomida xato bor!")









# a = 10
# b = 0

# try:
#     c = a / b
#     print(c)
# except ZeroDivisionError as error:
#     print(error)
# else:
#     print('Finishing up.')









# import asyncio


# async def square(number: int) -> int:
#     return number*number


# async def main() -> None:
#     try:
#        x = await square("10")
#        print(f'x={x}')
#        y = await square(5)
#        print(f'y={y}')
#        print(f'total={x+y}')

#     except:
#         print("Xato bor!")

# asyncio.run(main())









# from http import HTTPStatus

# print(HTTPStatus.OK) # 200
# print(HTTPStatus.NOT_FOUND) # 404
# print(HTTPStatus.INTERNAL_SERVER_ERROR) # 500

# print(list(HTTPStatus))








# from http import HTTPMethod

# print(HTTPMethod.GET) # GET

# print(list(HTTPMethod))










# import http.client

# from http import HTTPStatus

# # print(HTTPStatus.OK)

# print(list(HTTPStatus))


# data = http.client.HTTPConnection("www.askpython.com")

# data.request("get","/")
# response = data.getresponse()
# print(response.reason)
# print(response.status)
# data.close










# import http.client
 
# data = http.client.HTTPSConnection("www.youtube.com")
# data.request("GET", "/")
# response = data.getresponse()
# header = response.getheaders()
 
# print(header)
# print(header[0])

# print(response.reason)
# print(response.status)
# data.close()









# import requests

# r = requests.get('https://core.telegram.org/api')

# print(r.status_code)








import json

# data = {
#     "data_name": "Data Name",
#     "data_info": "Data Info",
#     "data_date": 2023,
#     "is_active": True,
#     "data_types": ["data_1", ("data_2","data_3")]
# }

# json_data = """
# {
#     "data_name": "Data Name",
#     "data_info": "Data Info",
#     "data_date": 2023,
#     "is_active": true,
#     "data_types": [
#         "data_1",
#         [
#             "data_2",
#             "data_3"
#         ]
#     ]
# }
# """

# print(type(data))
# data_json_format = json.dumps(data, indent=4)

# print(type(json_data))
# data_dict_format = json.loads(json_data)

# with open("data.json", "w") as f:
#     f.write(data_json_format)

# with open("data.json", "r") as f:
#     data_dict_format = json.load(f)
#     print(data_dict_format)








# import requests

# r = requests.get("https://jsonplaceholder.typicode.com/users")

# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.json())

# data = r.json()

# website = input(f"Sayt linkini kiriting: ")

# for name in data:
#     if name["website"] == website:
#         print(name["name"])

# print(f"Qaytadan urinib ko'ring!!!")









import requests

r = requests.get("https://jsonplaceholder.typicode.com/users")

import json

search = input("Search in here: ")

with open("data.json", "r") as f:
    data = json.load(f)


def search_result(search):
    for user in data:
        if search == user["ishchi_nomi"]:
         print(f'Delete {user["ishchi_nomi"]}?')  

         is_delete = str(input("Yes/no: ") or "yes").lower()
         
         if is_delete == "yes":
            data.remove(user)
            with open("data.json", "w") as f:
               json.dump(data, f, indent=4)
               print(f"{user['ishchi_nomi']} deleted!")
        else:
          print(f'{search} not found!')
          break 

search_result(search)