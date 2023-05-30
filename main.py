import time
import serial
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext



BOT_TOKEN = "6078239183:AAG0-PrtzITsWncvhzd86MvZm7inIXdbjBs"
# set up serial connection
ser = serial.Serial('COM3', 9600)  # replace 'COM_PORT' with your M5Stack's COM port

# define command handlers
def takeoff(update: Update, context: CallbackContext):
    print("Received command: /takeoff from Telegram")
    ser.write(b'takeoff')
    print("Sent command: takeoff to M5Stack")

def land(update: Update, context: CallbackContext):
    print("Received command: /land from Telegram")
    ser.write(b'land')
    print("Sent command: land to M5Stack")

def move(update: Update, context: CallbackContext, direction: str):
    distance = context.args[0] if context.args else '20'  # default to 20 if no argument is given
    print(f"Received command: /{direction} {distance} from Telegram")
    ser.write((direction + ' ' + distance).encode())
    print(f"Sent command: {direction} {distance} to M5Stack")

def battery(update: Update, context: CallbackContext):
    print("Received command: /battery from Telegram")
    ser.write(b'battery')
    print("Sent command: battery to M5Stack")

def shutdown(update: Update, context: CallbackContext):
    print("Received command: /shutdown from Telegram")
    ser.write(b'shutdown')
    print("Sent command: shutdown to M5Stack")

def status(update: Update, context: CallbackContext):
    print("Received command: /status from Telegram")
    ser.write(b'status')
    print("Sent command: status to M5Stack")

def rotate(update: Update, context: CallbackContext, direction: str):
    degree = context.args[0] if context.args else '90'  # default to 90 if no argument is given
    print(f"Received command: /{direction} {degree} from Telegram")
    ser.write((direction + ' ' + degree).encode())
    print(f"Sent command: {direction} {degree} to M5Stack")

def flip(update: Update, context: CallbackContext, direction: str):
    print(f"Received command: /flip_{direction} from Telegram")
    ser.write(('flip ' + direction).encode())
    print(f"Sent command: flip {direction} to M5Stack")


# set up telegram bot
updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

# add command handlers to bot
dp.add_handler(CommandHandler('cw', lambda update, context: rotate(update, context, 'cw'), pass_args=True))
dp.add_handler(CommandHandler('ccw', lambda update, context: rotate(update, context, 'ccw'), pass_args=True))
dp.add_handler(CommandHandler('flip_f', lambda update, context: flip(update, context, 'f')))
dp.add_handler(CommandHandler('flip_b', lambda update, context: flip(update, context, 'b')))
dp.add_handler(CommandHandler('flip_l', lambda update, context: flip(update, context, 'l')))
dp.add_handler(CommandHandler('flip_r', lambda update, context: flip(update, context, 'r')))
dp.add_handler(CommandHandler('takeoff', takeoff))
dp.add_handler(CommandHandler('land', land))
dp.add_handler(CommandHandler('forward', lambda update, context: move(update, context, 'forward'), pass_args=True))
dp.add_handler(CommandHandler('back', lambda update, context: move(update, context, 'back'), pass_args=True))
dp.add_handler(CommandHandler('up', lambda update, context: move(update, context, 'up'), pass_args=True))
dp.add_handler(CommandHandler('down', lambda update, context: move(update, context, 'down'), pass_args=True))
dp.add_handler(CommandHandler('left', lambda update, context: move(update, context, 'left'), pass_args=True))
dp.add_handler(CommandHandler('right', lambda update, context: move(update, context, 'right'), pass_args=True))
dp.add_handler(CommandHandler('battery', battery))
dp.add_handler(CommandHandler('shutdown', shutdown))
dp.add_handler(CommandHandler('status', status))


# start bot
updater.start_polling()

# keep the script running
while True:
    time.sleep(10)
