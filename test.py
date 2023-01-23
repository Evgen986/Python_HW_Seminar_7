my_dir = {}

with open('for_import.csv', encoding='utf=8') as file:
    text = [str(el).split(';') for el in file.readlines()]
text[0][0] = 1
for i in range(len(text)):
    text[i][0] = int(text[i][0])
    my_dir[text[i][0]] = dict(zip(text[i][1::2], text[i][2::2]))
print(text)
print(my_dir)
