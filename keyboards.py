import telebot

#Скрипт скачан с канала https://t.me/RabotaDotOnion 

#Главное Меню
keyboardMain = telebot.types.ReplyKeyboardMarkup(True)
keyboardMain.row('Заказать', 'Профиль')
keyboardMain.row('История', 'Правила')
keyboardMain.row('Support', 'Работа')
#keyboardMain.row('Отзывы')

#Меню профиля
profile = telebot.types.ReplyKeyboardMarkup(True)
profile.row('Пополнить', 'Работа')
profile.row('Хочу скидку', 'Диспуты')
profile.row('Назад')

#Оплата (Оплатил)
oplata_oplatil = telebot.types.ReplyKeyboardMarkup(True)
oplata_oplatil.row('Оплатил','Отменить')

#Оплата Биткоин
oplata_bitcoin = telebot.types.ReplyKeyboardMarkup(True)
oplata_bitcoin.row = ('Проверить оплату')
oplata_bitcoin.row = ('Отменить')

#Оплата Карта
oplata_karta = telebot.types.ReplyKeyboardMarkup(True)
oplata_karta.row = ('Проверить перевод')
oplata_karta.row = ('Отменить')

#Пополнение
popolnenie =  telebot.types.ReplyKeyboardMarkup(True)
popolnenie.row('Пополнить счет')
popolnenie.row('Отменить')

oplata = telebot.types.ReplyKeyboardMarkup(True)
oplata.row('QIWI', 'Bitcoin')
oplata.row('Банк.Картой')
oplata.row('Отменить')

#Скрипт скачан с канала https://t.me/RabotaDotOnion 

#Админ меню
admin = telebot.types.ReplyKeyboardMarkup(True)
admin.row('Изменить Карту','Изменить Qiwi')
admin.row('Изменить Bitcoin')
admin.row('Количество мамонтов')
admin.row('Отменить')

#Города
city = telebot.types.ReplyKeyboardMarkup(True)
city.row('Москва', 'С.Петербург')
city.row('Владивосток', 'Екатеринбург')
city.row('Сочи', 'Краснодар')
city.row('Отменить')

#Районы Москва
moskow_rayons = telebot.types.ReplyKeyboardMarkup(True)
moskow_rayons.row('Измайлово','Внуково')
moskow_rayons.row('Сокольники','Кунцево')
moskow_rayons.row('Крюково', 'Лефортово')
moskow_rayons.row('Выхино', 'Медведково')
moskow_rayons.row('Щукино', 'Якиманка')
moskow_rayons.row('Отменить')

#Районы С.Петербург
sankt_rayons = telebot.types.ReplyKeyboardMarkup(True)
sankt_rayons.row('Центральный', 'Невский')
sankt_rayons.row('Кировский', 'Московский')
sankt_rayons.row('Петроградский', 'Василеостровской')
sankt_rayons.row('Отменить')

#Районы Владивосток
vl_rayons = telebot.types.ReplyKeyboardMarkup(True)
vl_rayons.row('Центр', 'Первая речка')
vl_rayons.row('Эгершельд', 'Чуркин')
vl_rayons.row('Седанка', 'Фрунзенский')
vl_rayons.row('Отменить')

#Районы Екатеринбург
ekb_rayons = telebot.types.ReplyKeyboardMarkup(True)
ekb_rayons.row('Верх-Исетский', 'Кировский')
ekb_rayons.row('Железнодорожный', 'Ленинский')
ekb_rayons.row('Октябрьский')
ekb_rayons.row('Отменить')

#Скрипт скачан с канала https://t.me/RabotaDotOnion 

#Районы Сочи
sochi_rayons = telebot.types.ReplyKeyboardMarkup(True)
sochi_rayons.row('Центральный', 'Адлерский')
sochi_rayons.row('Хостинский', 'Лазаревский')
sochi_rayons.row('Отменить')

#Районы Краснодар
krasnodar_rayons = telebot.types.ReplyKeyboardMarkup(True)
krasnodar_rayons.row('Западный', 'Прикубанский')
krasnodar_rayons.row('Карасунский', 'Центральный')
krasnodar_rayons.row('Отменить')

#Скрипт скачан с канала https://t.me/RabotaDotOnion 

#Варианты товара
tovar1 = telebot.types.ReplyKeyboardMarkup(True)
tovar1.row('Alpha PVP', 'Гашиш Euro')
tovar1.row('Амфетамин', 'Шишки (АК47)')
tovar1.row('Мефедрон', 'Героин HQ')
tovar1.row('Спайс', 'Шишко-План')
tovar1.row('Отменить')

tovar2 = telebot.types.ReplyKeyboardMarkup(True)
tovar2.row('Alpha PVP', 'Гашиш Euro')
tovar2.row('Амфетамин', 'Шишки (АК47)')
tovar2.row('Отменить')

tovar3 = telebot.types.ReplyKeyboardMarkup(True)
tovar3.row('Alpha PVP', 'Гашиш Euro')
tovar3.row('Амфетамин', 'Мефедрон')
tovar3.row('Спайс', 'Героин HQ')
tovar3.row('Отменить')

tovar4 = telebot.types.ReplyKeyboardMarkup(True)
tovar4.row('Alpha PVP', 'Гашиш Euro')
tovar4.row('Амфетамин', 'Мефедрон')
tovar4.row('Спайс', 'Героин HQ')
tovar4.row('Отменить')

tovar5 = telebot.types.ReplyKeyboardMarkup(True)
tovar5.row('Alpha PVP', 'Гашиш Euro')
tovar5.row('Амфетамин', 'Спайс')
tovar5.row('Отменить')

tovar6 = telebot.types.ReplyKeyboardMarkup(True)
tovar6.row('Alpha PVP', 'Гашиш Euro')
tovar6.row('Отменить')

tovar7 = telebot.types.ReplyKeyboardMarkup(True)
tovar7.row('Alpha PVP', 'Амфетамин')
tovar7.row('Отменить')

#Варианты фасовки
alpha_fas = telebot.types.ReplyKeyboardMarkup(True)
alpha_fas.row('0.3г (900 руб)', '0.5г (1300 руб)')
alpha_fas.row('1г (2200 руб)', '3г (5500 руб)')
alpha_fas.row('Отменить')

gash_fas = telebot.types.ReplyKeyboardMarkup(True)
gash_fas.row('1г (1100 руб)', '2г (2000 руб)')
gash_fas.row('5г (4000 руб)', '10г (6000 руб)')
gash_fas.row('Отменить')

amph_fas =  telebot.types.ReplyKeyboardMarkup(True)
amph_fas.row('1г (950 руб)', '2г (1800 руб)')
amph_fas.row('5г (4100 руб)', '10г (6500 руб)')
amph_fas.row('Отменить')

meph_fas =  telebot.types.ReplyKeyboardMarkup(True)
meph_fas.row('1г (2100 руб)', '2г (4000 руб)')
meph_fas.row('5г (8000 руб)')
meph_fas.row('Отменить')

shish_fas = telebot.types.ReplyKeyboardMarkup(True)
shish_fas.row('1г (1200 руб)', '2г (2200 руб)')
shish_fas.row('5г (4200 руб)')
shish_fas.row('Отменить')

gero_fas = telebot.types.ReplyKeyboardMarkup(True)
gero_fas.row('0.5 (1700 руб)')
gero_fas.row('Отменить')

spice_fas = telebot.types.ReplyKeyboardMarkup(True)
spice_fas.row('1г (500 руб)', '3г (1200 руб)')
spice_fas.row('Отменить')

plan_fas = telebot.types.ReplyKeyboardMarkup(True)
plan_fas.row('1г (550 руб)', '3г (1500 руб)')
plan_fas.row('Отменить')

#Скрипт скачан с канала https://t.me/RabotaDotOnion 