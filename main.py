def data_input():
    age = int(input("введите возаст: "))
    citizenship = int(input("введите \"1\", если вы являетесь гражданином и \"0\", если нет: "))
    disqualification = int(input("введите \"1\", если вам запрещено участвовать в выборах и \"0\", если нет: "))
    return age, citizenship, disqualification


def check_permition(info_tuple):
    if (info_tuple[0] >= 18 and info_tuple[1] and not info_tuple[2]):
        print("вы можете голосовать")
    else:
        print("вы не можете голосовать")


check_permition(data_input())
