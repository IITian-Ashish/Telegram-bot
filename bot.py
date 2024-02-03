from telegram.ext import Updater, CommandHandler
import requests

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
TELEGRAM_BOT_TOKEN = '6970957423:AAFKxnBRz9WuxYs7OU20g9a8ZYqTxmwWKSo'

# Replace 'YOUR_LINKSHORTIFY_API_KEY' with your actual Linkshortify API key
LINKSHORTIFY_API_KEY = 'ba167f0c6934df8261f462a659dbf09bbf2de209'

# Your link shortening service URL
LINKSHORTIFY_URL = 'https://linkshortify.com/member/tools/api'

def shorten_url(url):
    params = {'api': LINKSHORTIFY_API_KEY, 'url': url}
    response = requests.get(LINKSHORTIFY_URL, params=params)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return 'Error: Unable to shorten URL'

def get_link(update, context):
    # Extract the link requested by the user from the message
    link_requested = ' '.join(context.args)
    shortened_link = shorten_url(link_requested)
    update.message.reply_text(f"Shortened Link: {shortened_link}")

def main():
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    # Command handler for users to request a link
    dispatcher.add_handler(CommandHandler("getlink", get_link))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
