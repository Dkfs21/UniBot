
import telebot
from telebot import types

bot = telebot.TeleBot("1622542433:AAG5LXfUxrwzVVhu46Oa4hHyXuD0_DghdVE")

menuAdr = 'none'

@bot.message_handler(commands=['start'])
def send_welcome(message):
	main_murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	main_murkup.row('👨‍🎓 Я студент', '🤵 Я абітурієнт')
	bot.send_message(message.chat.id, 'Ласкаво просимо до телеграм боту! 😉' + '\n' + "Тут ви знайдете актуальну інформацію, яка зв'язана зі всім університетом. 🎓", reply_markup=main_murkup)


@bot.message_handler(func=lambda message: True)
def bot_main(message):
	if message.text == '👨‍🎓 Я студент': #menuKeys
		student_murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		student_murkup.row('⚙ ІКПІ', '🛡 КБКіРТ', '💼 БіСК', '🏠 ЗН')
		student_murkup.row('↩ Повернутися на початок')
		bot.send_message(message.chat.id, '🏫 З якого ви інституту?', reply_markup=student_murkup)

	if message.text == '⬅ Назад до вибору інституту': #menuKeys
		student_murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		student_murkup.row('⚙ ІКПІ', '🛡 КБКіРТ', '💼 БіСК', '🏠 ЗН')
		student_murkup.row('↩ Повернутися на початок')
		bot.send_message(message.chat.id, '🏫 З якого ви інституту?', reply_markup=student_murkup)

	#	----------------	Данные ІКПІ

	elif message.text == '⚙ ІКПІ':  # menuKeys
		repStud = open(r'Files\Reports\repStudIKPI.txt', 'a')
		repStud.write('1')
		repStud.close()
		student_murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		student_murkup.row('💳 Реквізити оплати ІКПІ', '📅 Розклад ІКПІ', "💬 Зв'язок з деканатом ІКПІ")
		student_murkup.row('⬅ Назад до вибору інституту', '↩ Повернутися на початок')
		bot.send_message(message.chat.id, '🤔 Що вас цікавить?', reply_markup=student_murkup)

	elif message.text == '💳 Реквізити оплати ІКПІ':
		bot.send_message(message.from_user.id, "Тут будет Реквезиты оплаты")

	elif message.text == '📅 Розклад ІКПІ':
		bot.send_message(message.from_user.id, "Зачекайте, відправляємо файл...")
		bot.send_document(message.chat.id, open(r'Files\Stud\Розклад ІКПІ.docx', 'rb'))


	elif message.text == "💬 Зв'язок з деканатом ІКПІ":
		bot.send_message(message.from_user.id, "Тут будет Зв'язок з деканатом")

	#	----------------	Данные КБКіРТ

	elif message.text == '🛡 КБКіРТ':  # menuKeys
		repStud = open(r'Files\Reports\repStudKBKiRT.txt', 'a')
		repStud.write('1')
		repStud.close()
		student_murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		student_murkup.row('💳 Реквізити оплати КБКіРТ', '📅 Розклад КБКіРТ', "💬 Зв'язок з деканатом КБКіРТ")
		student_murkup.row('⬅ Назад до вибору інституту', '↩ Повернутися на початок')
		bot.send_message(message.chat.id, '🤔 Що вас цікавить?', reply_markup=student_murkup)

	elif message.text == '💳 Реквізити оплати КБКіРТ':
		bot.send_message(message.from_user.id, "Тут будет Реквезиты оплаты")

	elif message.text == '📅 Розклад КБКіРТ':
		bot.send_message(message.from_user.id, "Зачекайте, відправляємо файл...")
		bot.send_document(message.chat.id, open(r'Files\Stud\Розклад КБКіРТ.docx', 'rb'))

	elif message.text == "💬 Зв'язок з деканатом КБКіРТ":
		bot.send_message(message.from_user.id, "Тут будет Зв'язок з деканатом")

	#	----------------	Данные БіСК

	elif message.text == '💼 БіСК':  # menuKeys
		repStud = open(r'Files\Reports\repStudBiSK.txt', 'a')
		repStud.write('1')
		repStud.close()
		student_murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		student_murkup.row('💳 Реквізити оплати БіСК', '📅 Розклад БіСК', "💬 Зв'язок з деканатом БіСК")
		student_murkup.row('⬅ Назад до вибору інституту', '↩ Повернутися на початок')
		bot.send_message(message.chat.id, '🤔 Що вас цікавить?', reply_markup=student_murkup)

	elif message.text == '💳 Реквізити оплати БіСК':
		bot.send_message(message.from_user.id, "Тут будет Реквезиты оплаты")

	elif message.text == '📅 Розклад БіСК':
		bot.send_message(message.from_user.id, "Зачекайте, відправляємо файл...")
		bot.send_document(message.chat.id, open(r'Files\Stud\Розклад БіСК.docx', 'rb'))

	elif message.text == "💬 Зв'язок з деканатом БіСК":
		bot.send_message(message.from_user.id, "Тут будет Зв'язок з деканатом")

	#	----------------	Данные ЗН

	elif message.text == '🏠 ЗН':  # menuKeys
		repStud = open(r'Files\Reports\repStudZN.txt', 'a')
		repStud.write('1')
		repStud.close()
		student_murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		student_murkup.row('💳 Реквізити оплати ЗН', '📅 Розклад ЗН', "💬 Зв'язок з деканатом ЗН")
		student_murkup.row('⬅ Назад до вибору інституту', '↩ Повернутися на початок')
		bot.send_message(message.chat.id, '🤔 Що вас цікавить?', reply_markup=student_murkup)

	elif message.text == '💳 Реквізити оплати ЗН':
		bot.send_message(message.from_user.id, "Тут будет Реквезиты оплаты")

	elif message.text == '📅 Розклад ЗН':
		bot.send_message(message.from_user.id, "Зачекайте, відправляємо файл...")
		bot.send_document(message.chat.id, open(r'Files\Stud\Розклад ЗН.docx', 'rb'))


	elif message.text == "💬 Зв'язок з деканатом ЗН":
		bot.send_message(message.from_user.id, "Тут будет Зв'язок з деканатом")

	################################################################## Данные Абитуриентов

	elif message.text == '🤵 Я абітурієнт': #menuKeys
		repStud = open(r'Files\Reports\repAbitur.txt', 'a')
		repStud.write('1')
		repStud.close()
		student_murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		student_murkup.row('💵 Ціни контрактів', '🧾 Інформація про ЗНО', '🏣 Гуртожитки')
		student_murkup.row('💂 Військова кафедра', '✅ Переваги', "📞 Зв'язатися з нами")
		student_murkup.row('↩ Повернутися на початок')
		bot.send_message(message.chat.id, '🤔 Що вас цікавить?', reply_markup=student_murkup)

	elif message.text == '💵 Ціни контрактів':
		bot.send_message(message.from_user.id, "Зачекайте, відправляємо файл...")
		bot.send_document(message.chat.id, open(r'Files\Abitur\Ціни контракту.pdf', 'rb'))

	elif message.text == '🧾 Інформація про ЗНО':
		bot.send_message(message.from_user.id, "📑 Для того щоб вступити до нас необхідно отримати наступні сертифікати ЗНО: \n - українська мова та література; \n - математика; \n - фізика, іноземна мова, історія, географія, біологія, хімія - на вибір.")

	elif message.text == '🏣 Гуртожитки':
		bot.send_message(message.from_user.id, "🛏 " + "Університет має 5 гуртожитків, розташованих у центрі м. Одеса та районі Аркадія\n \n Гуртожиток № 1 – вул. -Манежна, 42. \n Гуртожиток № 1/2 – вул. Композитора Ніщинського, 4. \n Гуртожиток № 2 – вул. \n Старопортофранківська, 71а. \n Гуртожиток № 3 – вул. Новосельського, 68а. \n Гуртожиток № 4 – вул. Академічна, 20. \n Гуртожиток № 5 – вул. Композитора Ніщинського, 4.")

	elif message.text == '💂 Військова кафедра':
		bot.send_message(message.from_user.id, "📈 Водночас з навчанням, студенти університету мають можливість отримати військове звання - молодшого лейтенанта після закінчення військової кафедри." + "\n\n" +"✅ Для цього між ДУІТЗ та Військовою академією укладено угоду про співпрацю. Навчання триває 2 роки, починаючи с третього курсу.")

	elif message.text == "📞 Зв'язатися з нами":
		bot.send_location(message.from_user.id, 46.4824768048826, 30.723331404791455)
		bot.send_message(message.from_user.id, "📍 Нас можна знайти за адресою, яка вказана вище, а також зателефонувавши на номери: " + "\n" + "048-705-04-11" + "\n" + "048-705-04-13")

	##	##	##	##	##	##	##	##	##	##	##	##	##	##	##	##	##

	elif message.text == '✅ Переваги':
		main_murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		main_murkup.row('📑 Подвійний диплом', '🎓 Подвійна освіта', '🌴 База відпочинку')
		main_murkup.row('🏆 Спортивні секції')
		main_murkup.row('⬅ Назад', '↩ Повернутися на початок')
		bot.send_message(message.chat.id, 'Переваги навчання:', reply_markup=main_murkup)

	elif message.text == '📑 Подвійний диплом':
		bot.send_message(message.from_user.id, "👩‍🎓 ДУІТЗ співпрацює з Університетом прикладних наук Анхальт (м.Кетен, Німеччина). Студенти мають право отримати подвійні дипломи - України та Німеччини.")

	elif message.text == '🎓 Подвійна освіта':
		bot.send_message(message.from_user.id, "📈 Студенти університету мають право додатково отримати другу управлінську спеціальність (економіка, менеджмент) поряд з основною технічною освітою."+ "\n\n" +"🕘 Навчання відбувається у вечірній формі. Після 4-х років навчання можна отримати два дипломи про вищу освіту!")

	elif message.text == '🌴 База відпочинку':
		bot.send_message(message.from_user.id, "Тут будет База відпочинку")

	elif message.text == '💂 Військова кафедра':
		bot.send_message(message.from_user.id, "Тут будет Військова кафедра")

	elif message.text == '🏆 Спортивні секції':
		bot.send_message(message.from_user.id, "Тут будет Спортивні секції")

	##	##	##	##	##	##	##	##	##	##	##	##	##	##	##	##	##

	elif message.text == '⬅ Назад': #menuKeys
		student_murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		student_murkup.row('💵 Ціни контрактів', '🧾 Інформація про ЗНО', '🏣 Гуртожитки')
		student_murkup.row('💂 Військова кафедра', '✅ Переваги', "📞 Зв'язатися з нами")
		student_murkup.row('↩ Повернутися на початок')
		bot.send_message(message.chat.id, '✖ Повертаємося...', reply_markup=student_murkup)

	##################################################################

	elif message.text == '↩ Повернутися на початок': #menuKeys
		main_murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		main_murkup.row('👨‍🎓 Я студент', '🤵 Я абітурієнт')
		bot.send_message(message.chat.id, '✖ Повертаємося...', reply_markup=main_murkup)

	elif message.text == 'Звіт' or message.text == 'Отчёт':
		file = open('Report.txt', 'r', encoding='utf-8')
		report = file.read()
		bot.send_message(message.chat.id, report)
		file.close()

bot.polling()
