login = input()
print("OK" if "@" not in login else "Некорректный логин")
email = input()
print("OK" if "@" in email else "Некорректный адрес")