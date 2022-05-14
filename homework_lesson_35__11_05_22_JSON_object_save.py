### Task: lesson 35 JSON ###
import json

print("Задание: \n"
      "Сохранить в Формате Объека(JSON)[Python(DICT)], \"Номер\":{\"name\": \"\",\"tel\": \"\"}")
from random import choice


def gen_tel_of_name_by_id():
    jornal_id = ""
    name = ""
    tel = ''

    letters = f"abcdefghiklmnoprstwyz"
    nums = f"0123456789"

    while len(jornal_id) != 10:
        jornal_id += choice(nums)

    print(jornal_id)

    while len(name) != 7:
        name += choice(letters)
    print(name)

    while len(tel) != 10:
        tel += choice(nums)
    print(tel)

    worker = {
        jornal_id: {
            "name": name,
            "tel": tel
        }
    }

    try:
        data_include_id_name_tel = json.load(open("dict_id_dict_name_tel_35hw.json"))
    except FileNotFoundError:
        data_include_id_name_tel = dict()
    # data_include_id_name_tel.append(personal_dict)
    data_include_id_name_tel.fromkeys(name, tel)
    with open("dict_id_dict_name_tel_35hw.json") as fh_hw_35:
        json.dump(data_include_id_name_tel, fh_hw_35, indent=3)

    return worker


# def write_json(personal_dict):
    # try:
    #     data_include_id_name_tel = json.load(open("dict_id_dict_name_tel_35hw.json"))
    # except FileNotFoundError:
    #     data_include_id_name_tel = dict()
    # # data_include_id_name_tel.append(personal_dict)
    # data_include_id_name_tel.setdefault(gen_tel_of_name_by_id.jornal_id)
    # with open("dict_id_dict_name_tel_35hw.json") as fh_hw_35:
    #     json.dump(data_include_id_name_tel, fh_hw_35, indent=3)


for inst_funcs in range(3):
    gen_tel_of_name_by_id()

gen_tel_of_name_by_id()
