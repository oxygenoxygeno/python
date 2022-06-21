password = input()
check = input()

if len(password) < 8:
    print("Короткий!")
elif password != check:
    print("Различаются.")
else:
    print("OK")