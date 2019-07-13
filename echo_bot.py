импортный телебот

bot = telebot.TeleBot ( " 722344827:AAHvca0SfDlvFl6XRsUvVkEbdkrGKkOV2wU " )
@ bot.message_handler ( commands = [ ' start ' , ' help ' ])
 def  send_welcome ( message ):
	bot.reply_to (сообщение « Привет, как дела? » )
  @ bot.message_handler ( func = lambda  m : True )
 def  echo_all ( message ):
	bot.reply_to (message, message.text)
