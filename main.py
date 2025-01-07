real_password = "qwerty123"
enterned_password = ""

while real_password != enterned_password:
    enterned_password = input("введите пароль: ")
    if enterned_password == real_password:
        print("пароль верный")
    else:
        print("пароль не верный")