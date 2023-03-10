from telegram.ext import(
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from telegram import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
def start(update,context):
    text = 'Hello! š \nThis is a demo version of the Telegram Store bot. You can test out catalog function and checkout process.'
    bot = context.bot
    
    Card = KeyboardButton(text='š³ Card')
    Finance = KeyboardButton(text='š“ Finance')
    Misc = KeyboardButton(text='šāāļø Misc')
    Name = KeyboardButton(text='š“ Name')
    Phone = KeyboardButton(text='š± Phone')
    SNumber = KeyboardButton(text='š Social Number')
    Text = KeyboardButton(text='š Text')

    keyboard = ReplyKeyboardMarkup(
        [   
            [Card,Finance],
            [Misc,Name],
            [Phone,SNumber],
            [Text]
        ],
        resize_keyboard=True
    )
    update.message.reply_text(text=text,reply_markup = keyboard)
def catalog(update,context):
    query = update.callback_query
    catalog = InlineKeyboardButton(
        text='š pizza',
        switch_inline_query_current_chat='š pizza'
    )
    reply_markup = InlineKeyboardMarkup(
        [
            [catalog]
        ]
    )
    update.message.reply_text(text = 'š¬ Catalog',reply_markup = reply_markup)

def order(update,context):
    cancel = InlineKeyboardButton(
        text='ā Cancel',
        callback_data='cancel'
    )
    accept = InlineKeyboardButton(
        text='ā Accept',
        callback_data='accept'
    )
    keyboard = InlineKeyboardMarkup(
        [
            [accept,cancel]
        ]
    )   
    text='š¦ Your order\n\nChili Pizza (14") - $22.99 x1 = $22.99\n\nšµ Amount to pay: $22.99\n\nš¬ Comment to the order: š¦ Orders'
    update.message.reply_text(text,reply_markup = keyboard)

def cart(update,context):
    place_order = InlineKeyboardButton(
        text= 'ā Place order',
        callback_data='placeorder'
    )
    clear = InlineKeyboardButton(
        text='š§¹ Clear',
        callback_data='clear'
    )
    keyboard = InlineKeyboardMarkup(
        [
            [place_order,clear]
        ]
    )
    text = 'š Cart\n\nChili Pizza (14") - $22.99 x1 = $22.99\n\nšµ Total: $22.99'
    update.message.reply_text(text,reply_markup = keyboard)
def userinfo(update,context):
    bot = context.bot
    query = update.callback_query
    chat_id = update.message.chat.id
    first_name = update.message.from_user.first_name
    addresses = InlineKeyboardButton(
        text='š  Addresses',
        callback_data='iplace'
    )
    add_address = InlineKeyboardButton(
        text= 'ā Add address',
        callback_data='add'
    )
    keyboard = InlineKeyboardMarkup(
        [
            [addresses,add_address]
        ],resize_keyboard=True
    )
    text = f'š¤ {first_name}\nš¤ Invited friends: 0\nšø Bonus balance: $0.0\nā¹ļø You can get 5.0% on your bonus balance from the amount of each order of your invited friends.'
    bot.sendMessage(chat_id,text=text,reply_markup = keyboard)
def administration(update,context):
    users = KeyboardButton(text= 'š„ Users')
    orders = KeyboardButton(text= 'š· Orders')
    welcome_text = KeyboardButton(text='š Welcome text')
    bonus = KeyboardButton(text='š¤ Bonus rate')
    add = KeyboardButton(text='ā Add category')
    remove = KeyboardButton(text='š Remove category')
    new = KeyboardButton(text='š¦ New product')
    delete = KeyboardButton(text='š Delete product')
    exit = KeyboardButton(text='šŖ Exit')

    keyboard = ReplyKeyboardMarkup(
        [
            [users,orders],
            [welcome_text,bonus],
            [add,remove],
            [new,delete],
            [exit]
        ],
        resize_keyboard=True
    )
    text = update.message.text
    update.message.reply_text(text,reply_markup=keyboard)
def users(update,context):
    update.message.reply_text(text='No users')
def welcome_text(update,context):
    cancel = KeyboardButton(text='ā Cancel')

    keyboard = ReplyKeyboardMarkup(
        [
            [cancel]
        ],
        resize_keyboard=True
    )
    text = 'š New welcome text Send the text of greeting in one message.You can use Telegram Markdown to format your message:*bold text* _italic text_'
    update.message.reply_text(text,reply_markup = keyboard)
def cancel(update,context):
    query = update.callback_query
    query.edit_message_text(text = 'ā Order cancelled') 
def bonus_rate(update,context):
    cancel = KeyboardButton(text='ā Cancel')

    keyboard = ReplyKeyboardMarkup(
        [
            [cancel]
        ],
        resize_keyboard=True
        
    )
    text = 'š¤ Bonus rate'
    update.message.reply_text(text,reply_markup = keyboard)
def notaviable(update,context):
    Users = KeyboardButton(text='š„ Users')
    Orders = KeyboardButton(text='š· Orders')
    Welcome = KeyboardButton(text='š Welcome text')
    Bonus = KeyboardButton(text='š¤ Bonus rate')
    Add = KeyboardButton(text='ā Add category')
    Remove = KeyboardButton(text='š Remove category')
    New = KeyboardButton(text='š¦ New product')
    Delete = KeyboardButton(text='š Delete product')
    Exit = KeyboardButton(text='šŖ Exit')
    keyboard = ReplyKeyboardMarkup(
        [
            [Users,Orders],
            [Welcome,Bonus],
            [Add,Remove],
            [New,Delete],
            [Exit]
        ],
        resize_keyboard=True
    )
    text = 'ā”ļø Not available in demo version.'
    update.message.reply_text(text,reply_markup=keyboard)
def addresses(update,context):
    query = update.callback_query
    bot = context.bot
    chat_id = update.callback_query.message.chat.id
    text = ' Please send the address to which you want your order to be delivered.'
    location = KeyboardButton(
        text = 'š Location',
        request_location=True
    )
    cancel = KeyboardButton(text = 'šŖ Exit')
    keyboard = ReplyKeyboardMarkup(
        [
            [location],
            [cancel]
        ],
        resize_keyboard=True
    )
    bot.sendMessage(chat_id,text=text,reply_markup=keyboard)
    
    query.answer('Working...')
def addaddresses(update,context):
    text ='š Please send the address to which you want your order to be delivered.'
    bot = context.bot 
    query = update.callback_query
    chat_id = update.callback_query.message.chat.id 
    bot.sendMessage(chat_id,text=text)
    query.answer(text='Working...')
def accept(update,context):
    query = update.callback_query
    bot = context.bot
    chat_id = update.callback_query.message.chat.id
    text1 = 'š¦ Your order\n\nChili Pizza (14") - $22.99 x1 = $22.99\n\nšµ Amount to pay: $22.99\n\nš¬ Comment to the order: š¦ Orders'
    text2= 'ā Order placed!'
    query.edit_message_text(text1)
    bot.sendMessage(chat_id,text=text2)
def cancel(update,context):
    query = update.callback_query
    query.edit_message_text(text='ā Order cancelled')
def placeorder(update,context):
    query = update.callback_query
    bot = context.bot
    chat_id = update.callback_query.message.chat.id
    text = 'š Choose shipping address:'
    location = KeyboardButton(
        text = 'š Location',
        request_location=True
    )
    cancel = KeyboardButton(text='šŖ Exit')
    keyboard = ReplyKeyboardMarkup(
        [
            [location],
            [cancel]
        ],
        resize_keyboard=True
    )
    bot.sendMessage(chat_id,text=text,reply_markup=keyboard)
    query.answer('Waiting...')
def clear(update,context):
    query = update.callback_query
    query.edit_message_text(text='ā Cart cleared')
updater = Updater('5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('š³ Card'),catalog))
updater.dispatcher.add_handler(MessageHandler(Filters.text('š¦ Orders'),order))
updater.dispatcher.add_handler(MessageHandler(Filters.text('š Cart'),cart))
updater.dispatcher.add_handler(MessageHandler(Filters.text('š¤ User info'),userinfo))
updater.dispatcher.add_handler(MessageHandler(Filters.text('š Administration'),administration))
updater.dispatcher.add_handler(MessageHandler(Filters.text('šŖ Exit'),start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('š„ Users'),users))
updater.dispatcher.add_handler(MessageHandler(Filters.text('š Welcome text'),welcome_text))
updater.dispatcher.add_handler(MessageHandler(Filters.text('ā Cancel'),administration))
updater.dispatcher.add_handler(MessageHandler(Filters.text('š¤ Bonus rate'),bonus_rate))
updater.dispatcher.add_handler(MessageHandler(Filters.text('ā Add category'),notaviable))
updater.dispatcher.add_handler(MessageHandler(Filters.text('š¦ New product'),notaviable))
updater.dispatcher.add_handler(MessageHandler(Filters.text('š Remove category'),notaviable))
updater.dispatcher.add_handler(MessageHandler(Filters.text('š Delete product'),notaviable))


updater.dispatcher.add_handler(CallbackQueryHandler(addaddresses,pattern='add'))
updater.dispatcher.add_handler(CallbackQueryHandler(addresses,pattern='iplace'))
updater.dispatcher.add_handler(CallbackQueryHandler(accept,pattern='accept'))
updater.dispatcher.add_handler(CallbackQueryHandler(cancel,pattern='cancel'))
updater.dispatcher.add_handler(CallbackQueryHandler(placeorder,pattern='placeorder'))
updater.dispatcher.add_handler(CallbackQueryHandler(clear,pattern='clear'))

updater.start_polling()
updater.idle()