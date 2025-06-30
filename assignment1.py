import csv
import json

def file_reader():
    """Read csv data from user_data.csv, return as list of strings"""
    with open("user_data.csv") as _f:
        lines = _f.readlines()
        lines = lines[1:]
    return lines


def save_json(entries_list):
    with open("user_data.json", "w") as j_convert:
        json.dump(entries_list, j_convert)

def dict_maker(lines):
    entries_list = []
    for line in lines:
        split_line = line.split(";")
        name = split_line[1]
        email = split_line[0]
        md5 = split_line[2].strip("\n")
        dict = {"name": name,
                "email": email,
                "md5": md5}  
        entries_list.append(dict)
    return entries_list



if __name__ == "__main__":
    lines = file_reader()
    entries_list = dict_maker(lines)
    for entry in entries_list:
        print(entry)
    save_json(entries_list)
