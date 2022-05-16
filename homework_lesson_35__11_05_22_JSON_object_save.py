### Task: lesson 35 JSON ###
import json

print("Задание: \n"
      "Сохранить в Формате Объека(JSON)[Python(DICT)], \"Номер\":{\"name\": \"\",\"tel\": \"\"}")

from random import choice


def gen_dict():
    id = ""
    name = ""
    tel = ''

    letters = f"abcdefghiklmnoprstwyz"
    nums = f"0123456789"

    while len(id) != 10:
        id += choice(nums)

    # print(id)

    while len(name) != 7:
        name += choice(letters)
    #     print(name)

    while len(tel) != 10:
        tel += choice(nums)
    #     print(tel)

    dict1 = {
        id: {
            "name": name,
            "tel": tel
        }
    }

    return dict1


def write_json(personal_dict):
    try:
        data = json.load(open("dict_35hw.json"))
    except FileNotFoundError:
        data = dict()

    data.update(personal_dict)
    with open("dict_35hw.json", 'w') as fh_hw_35:
        json.dump(data, fh_hw_35, indent=3)


for i in range(7):
    write_json(gen_dict())

with open("dict_35hw.json", "r") as fh_hw_35:
    print(json.load(fh_hw_35))

print("Variant 2")


def gen_dict2():
    name = ""
    tel = ''

    letters = f"abcdefghiklmnoprstwyz"
    nums = f"0123456789"

    while len(name) != 7:
        name += choice(letters)
    #     print(name)

    while len(tel) != 10:
        tel += choice(nums)
    #     print(tel)

    dict2 = {
        "name": name,
        "tel": tel
    }

    return dict2, tel


def write_json(personal_dict, num):
    try:
        data = json.load(open("dict_35_2hw.json"))
    except FileNotFoundError:
        data = dict()

    data[num] = personal_dict
    with open("dict_35_2hw.json", 'w') as fh_hw_35_2:
        json.dump(data, fh_hw_35_2, indent=3)


for i in range(7):
    write_json(gen_dict2()[0], gen_dict2()[1])

with open("dict_35_2hw.json", "r") as fh_hw_35_2:
    print(json.load(fh_hw_35_2))
