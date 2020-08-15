import re

with open("rohdaten.txt", "rb") as f:
    text = f.read()
    Schüler_all = str(text).split("Seite")

Kurse = re.findall(r"Q1[G|L]\w+\d", str(text))
Kurse = list(dict.fromkeys(Kurse))
Kurse.sort()
dict = {}

for Kurs in Kurse:
    list = []
    for Schüler in Schüler_all:
        match = re.search(Kurs, Schüler)
        try:
            Schüler_Namen = re.findall(r"Planung_SJ_20/21_1\s\S+\s*\S*,\s\S+\s*\S*",str(Schüler))
        except:
            print("Error: " + Schüler)
        if match != None:
            list.append(Schüler_Namen[0].replace("SF/BK:", '').replace("Planung_SJ_20/21_1", ''))
    dict[Kurs] = list

with open("sortiert.txt", "w") as f:
    for Kurs_loop, Schüler_loop in dict.items():
        f.write(Kurs_loop + ":\n")
        for i in Schüler_loop:
            f.write("  " + i + "\n")
