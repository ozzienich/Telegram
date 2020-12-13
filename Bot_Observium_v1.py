'''
=======================================================================================
    sent Observium Graph to Telegram 
    (c)2020 - OZZIE <ozzie@optimasidata.com>
    
=======================================================================================
'''

from telegram import Update, ParseMode 
from telegram.ext import Updater, CommandHandler, CallbackContext,  MessageHandler, Filters
import re
from datetime import datetime, timedelta
import time
import os
import pycurl


def start (update: Update, context: CallbackContext) -> None:
    update.message.reply_text('BOT started!')

    
    
def disk_command(update: Update, context: CallbackContext) -> None:
    last_date_time = datetime.now() - timedelta(hours = 3)
    timestamp = datetime.timestamp(last_date_time)
    jam_now = int(time.time())
    jam_lalu  = int(timestamp)
    jam_now = str(jam_now)
    jam_lalu = str(jam_lalu) 
    uurl = 'http://xxx.xxx.xxx.xxx/graph.php?type=device_storage&device=15&to='+jam_now+'&from='+jam_lalu+'&height=300&width=800'
    print (uurl)
    c = pycurl.Curl()
    c.setopt(c.URL,uurl)
    with open('/tmp/disk.png', 'wb') as f:
        c.setopt(c.WRITEFUNCTION, f.write)
        c.perform()
    
    context.bot.send_photo(chat_id=update.message.chat.id,photo=open('/tmp/disk.png','rb'),caption="sdadadsadsa")

    
'''
DISK EXT DB DC
'''    
def disk_dbext_dc(update: Update, context: CallbackContext) -> None:
    last_date_time = datetime.now() - timedelta(hours = 3)
    timestamp = datetime.timestamp(last_date_time)
    jam_now = int(time.time())
    jam_lalu  = int(timestamp)
    jam_now = str(jam_now)
    jam_lalu = str(jam_lalu) 
    uurl = 'http://xxx.xxx.xxx.xxx/graph.php?type=device_storage&device=7&to='+jam_now+'&from='+jam_lalu+'&height=300&width=800'
    print (uurl)
    c = pycurl.Curl()
    c.setopt(c.URL,uurl)
    with open('/tmp/disk.png', 'wb') as f:
        c.setopt(c.WRITEFUNCTION, f.write)
        c.perform()
    context.bot.send_photo(chat_id=update.message.chat.id,photo=open('/tmp/disk.png','rb'), parse_mode=ParseMode.HTML, caption="XXXXX - 3 Jam Terakhir")

    
'''
DISK EXT DB DRC
'''    
def disk_dbext_drc(update: Update, context: CallbackContext) -> None:
    last_date_time = datetime.now() - timedelta(hours = 3)
    timestamp = datetime.timestamp(last_date_time)
    jam_now = int(time.time())
    jam_lalu  = int(timestamp)
    jam_now = str(jam_now)
    jam_lalu = str(jam_lalu) 
    uurl = 'http://xxx.xxx.xxx.xxx/graph.php?type=device_storage&device=35&to='+jam_now+'&from='+jam_lalu+'&height=300&width=800'
    print (uurl)
    c = pycurl.Curl()
    c.setopt(c.URL,uurl)
    with open('/tmp/disk.png', 'wb') as f:
        c.setopt(c.WRITEFUNCTION, f.write)
        c.perform()
    context.bot.send_photo(chat_id=update.message.chat.id,photo=open('/tmp/disk.png','rb'),parse_mode=ParseMode.HTML, caption="<b>XXXXX </b> - 3 Jam Terakhir")

    
'''
DISK DB PUBLIC DC
'''    
def disk_dbpublic_dc(update: Update, context: CallbackContext) -> None:
    last_date_time = datetime.now() - timedelta(hours = 3)
    timestamp = datetime.timestamp(last_date_time)
    jam_now = int(time.time())
    jam_lalu  = int(timestamp)
    jam_now = str(jam_now)
    jam_lalu = str(jam_lalu) 
    uurl = 'http://xxx.xxx.xxx.xxx/graph.php?type=device_storage&device=15&to='+jam_now+'&from='+jam_lalu+'&height=300&width=800'
    print (uurl)
    c = pycurl.Curl()
    c.setopt(c.URL,uurl)
    with open('/tmp/disk.png', 'wb') as f:
        c.setopt(c.WRITEFUNCTION, f.write)
        c.perform()
    context.bot.send_photo(chat_id=update.message.chat.id,photo=open('/tmp/disk.png','rb'),parse_mode=ParseMode.HTML,caption="<b>XXXXX </b> - 3 Jam Terakhir")

'''
DISK DB PUBLIC DRC
'''    
def disk_dbpublic_drc(update: Update, context: CallbackContext) -> None:
    last_date_time = datetime.now() - timedelta(hours = 3)
    timestamp = datetime.timestamp(last_date_time)
    jam_now = int(time.time())
    jam_lalu  = int(timestamp)
    jam_now = str(jam_now)
    jam_lalu = str(jam_lalu) 
    uurl = 'http://xxx.xxx.xxx.xxx/graph.php?type=device_storage&device=22&to='+jam_now+'&from='+jam_lalu+'&height=300&width=800'
    print (uurl)
    c = pycurl.Curl()
    c.setopt(c.URL,uurl)
    with open('/tmp/disk.png', 'wb') as f:
        c.setopt(c.WRITEFUNCTION, f.write)
        c.perform()
    context.bot.send_photo(chat_id=update.message.chat.id,photo=open('/tmp/disk.png','rb'),parse_mode=ParseMode.HTML,caption="<b>XXXXX </b> - 3 Jam Terakhir")

    
'''
DISK DB REPORTING DC
'''    
def disk_dbreport_dc(update: Update, context: CallbackContext) -> None:
    last_date_time = datetime.now() - timedelta(hours = 3)
    timestamp = datetime.timestamp(last_date_time)
    jam_now = int(time.time())
    jam_lalu  = int(timestamp)
    jam_now = str(jam_now)
    jam_lalu = str(jam_lalu) 
    uurl = 'http://xxx.xxx.xxx.xxx/graph.php?type=device_storage&device=14&to='+jam_now+'&from='+jam_lalu+'&height=300&width=800'
    print (uurl)
    c = pycurl.Curl()
    c.setopt(c.URL,uurl)
    with open('/tmp/disk.png', 'wb') as f:
        c.setopt(c.WRITEFUNCTION, f.write)
        c.perform()
    context.bot.send_photo(chat_id=update.message.chat.id,photo=open('/tmp/disk.png','rb'),parse_mode=ParseMode.HTML,caption="<b>XXXXX </b> - 3 Jam Terakhir")

    
    
''' DRC
DISK DB REPORTING DRC
'''    
def disk_dbreport_drc(update: Update, context: CallbackContext) -> None:
    last_date_time = datetime.now() - timedelta(hours = 3)
    timestamp = datetime.timestamp(last_date_time)
    jam_now = int(time.time())
    jam_lalu  = int(timestamp)
    jam_now = str(jam_now)
    jam_lalu = str(jam_lalu) 
    uurl = 'http://xxx.xxx.xxx.xxx/graph.php?type=device_storage&device=19&to='+jam_now+'&from='+jam_lalu+'&height=300&width=800'
    print (uurl)
    c = pycurl.Curl()
    c.setopt(c.URL,uurl)
    with open('/tmp/disk.png', 'wb') as f:
        c.setopt(c.WRITEFUNCTION, f.write)
        c.perform()
    context.bot.send_photo(chat_id=update.message.chat.id,photo=open('/tmp/disk.png','rb'),parse_mode=ParseMode.HTML,caption="<b>XXXXX </b> - 3 Jam Terakhir")

    
''' DWH DC
DISK DB DWH DC
'''    
def disk_dbdwh_dc(update: Update, context: CallbackContext) -> None:
    last_date_time = datetime.now() - timedelta(hours = 3)
    timestamp = datetime.timestamp(last_date_time)
    jam_now = int(time.time())
    jam_lalu  = int(timestamp)
    jam_now = str(jam_now)
    jam_lalu = str(jam_lalu) 
    uurl = 'http://xxx.xxx.xxx.xxx/graph.php?type=device_storage&device=1&to='+jam_now+'&from='+jam_lalu+'&height=300&width=800'
    print (uurl)
    c = pycurl.Curl()
    c.setopt(c.URL,uurl)
    with open('/tmp/disk.png', 'wb') as f:
        c.setopt(c.WRITEFUNCTION, f.write)
        c.perform()
    context.bot.send_photo(chat_id=update.message.chat.id,photo=open('/tmp/disk.png','rb'),parse_mode=ParseMode.HTML,caption="<b>XXXXX </b> - 3 Jam Terakhir")
    
    
''' DWH DRC
DISK DB DWH DC
'''    
def disk_dbdwh_drc(update: Update, context: CallbackContext) -> None:
    last_date_time = datetime.now() - timedelta(hours = 3)
    timestamp = datetime.timestamp(last_date_time)
    jam_now = int(time.time())
    jam_lalu  = int(timestamp)
    jam_now = str(jam_now)
    jam_lalu = str(jam_lalu) 
    uurl = 'http://xxx.xxx.xxx.xxx/graph.php?type=device_storage&device=36&to='+jam_now+'&from='+jam_lalu+'&height=300&width=800'
    print (uurl)
    c = pycurl.Curl()
    c.setopt(c.URL,uurl)
    with open('/tmp/disk.png', 'wb') as f:
        c.setopt(c.WRITEFUNCTION, f.write)
        c.perform()
    context.bot.send_photo(chat_id=update.message.chat.id,photo=open('/tmp/disk.png','rb'),parse_mode=ParseMode.HTML,caption="<b>XXXXX </b> - 3 Jam Terakhir")
    

    
def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,parse_mode=ParseMode.HTML,text='sorry. unknown command \U0001F61C')


REQUEST_KWARGS={ 'proxy_url': 'http://xxx.xxx.xxx.xxx:8080/',}

updater = Updater("XXXXXXXXXXX_API_TOKEN_XXXXXXXXXXXXX", use_context=True, request_kwargs=REQUEST_KWARGS)

unknown_handler = MessageHandler(Filters.command, unknown)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(CommandHandler('disk',disk_command))
updater.dispatcher.add_handler(CommandHandler('disk_dbpublic_dc',disk_dbpublic_dc))
updater.dispatcher.add_handler(CommandHandler('disk_dbpublic_drc',disk_dbpublic_drc))
updater.dispatcher.add_handler(CommandHandler('disk_dbext_dc',disk_dbext_dc))
updater.dispatcher.add_handler(CommandHandler('disk_dbext_drc',disk_dbext_drc))
updater.dispatcher.add_handler(CommandHandler('disk_dbreport_dc',disk_dbreport_dc))
updater.dispatcher.add_handler(CommandHandler('disk_dbdwh_dc',disk_dbdwh_dc))
updater.dispatcher.add_handler(CommandHandler('disk_dbdwh_drc',disk_dbdwh_drc))

updater.dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()

