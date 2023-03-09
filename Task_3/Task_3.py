from pprint import pprint


list_of_files = ["1.txt", "2.txt", "3.txt"]
dict_f = {}

for f in list_of_files:
    with open ("Task_3\\" + f, "rt", encoding="utf-8") as file:
        list_text = file.readlines()
        d ={f : list_text}
        dict_f[len(list_text)] = d

sorted_dict = dict(sorted(dict_f.items()))

with open ("Task_3/new_file", "wt", encoding="utf-8") as new_file:
    for len_file, value in sorted_dict.items():
        for name_file, text_file in value.items():
            x = (f"{name_file}\n{len_file}\n{' '.join(text_file)}\n")
            new_file.write(x)