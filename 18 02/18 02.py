def letter(name, pl, d, email):
    return f'''To: {email}
Здравствуйте, {name}!
Были бы рады видеть вас на встрече начинающих программистов в {pl}е, которая пройдет {d}.'''


place = 'Кёльн'
name = 'Данил'
date = '21.02.20'
email = 'danya65@mail.ru'
print(letter(name, place, date, email))
name = 'Кирилл'
place = 'Париж'
date = '09.05.20'
email = 'k.krutoy05@yandex.ru'
print(letter(name, place, date, email))
