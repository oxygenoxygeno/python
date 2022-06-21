while True:
    passwordOne = input("password 1:")
    passwordTwo = input("password 2:")
    a = True
    if len(passwordOne)<8:
        a = False
        print("Короткий")
    if passwordOne != passwordTwo:
        a = False
        print("Различаются")
    if "123" in passwordOne:
        a = False
        print("Простой")
    if a:
        break
print("OK")