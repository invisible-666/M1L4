import telebot
from config import token
from logic import quiz_questions

user_responses = {} 

token = "7058753529:AAHEKGkWEwclTCOM6W8VG-AunOU-fu1QzpI"
bot = telebot.TeleBot(token)

def send_question(chat_id):
    bot.send_message(chat_id, quiz_questions[user_responses[chat_id]].text, reply_markup=quiz_questions[user_responses[chat_id]].gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    if call.data == "correct":
        bot.answer_callback_query(call.id, "Answer is correct")
    elif call.data == "wrong":
        bot.answer_callback_query(call.id,  "Answer is wrong")
      
    def get_quest():
        print(quiz_questions)

    if call.data == "correct":
            bot.answer_callback_query(call.id, "Answer is correct")
            coins += 1
    elif call.data == "wrong":
        bot.answer_callback_query(call.id,  "Answer is wrong")

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id not in user_responses.keys():
        user_responses[message.chat.id] = 0
        send_question(message.chat.id)


bot.infinity_polling()
