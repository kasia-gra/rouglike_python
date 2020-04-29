import csv 
import os


DIRPATH = os.getcwd()

def change_numbers_to_intigers(character):
    try: 
        character = int(character)
    except ValueError:
        character = character
    return character


def import_data_to_dict(DIRPATH, folder, filename):
    items = {}
    with open(f"{DIRPATH}/{folder}/{filename}", "r") as file:
        items_list = list(csv.reader(file))
        items_keys = items_list[0]
        for col_index in range(1, len(items_list)):
            atributes = {}
            for item_index in range(len(items_list[col_index])):
                if col_index != 0 and item_index != 0:
                    atributes[items_keys[item_index]] = change_numbers_to_intigers(items_list[col_index][item_index])
                else:
                    items[items_list[col_index][item_index]] = atributes
    return items

def read_image_file(DIRPATH, folder, filename):
    with open(f"{DIRPATH}/{folder}/{filename}", "r") as file:
        image = file.read()
        return image