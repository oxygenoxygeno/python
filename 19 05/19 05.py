def ask_password(login: str, password: str, success: callable, failure: callable):
    count_v, count_c, pos_c = 0, 0, 0
    for pos, symbol in enumerate(password.lower()):
        if symbol in "aeiouy":
            count_v += 1
        elif symbol in login.lower():
            count_c, pos_c = 0 if pos_c > pos else count_c + 1, pos
    if count_v < 3 and count_c < 3:
        failure(login, "Everything is wrong")
    elif count_v < 3:
        failure(login, "Wrong number of vowels")
    elif count_c < 3:
        failure(login, "Wrong consonants")
    else:
        success(login)



ask_password("login", "1",
             lambda login: print(f"SUCCES: #{login}"),
             lambda login, message: print(f"FAILURE: #{login} | info: {message}"))