# Реализация приложения, которое считывает данные с файла, и сохраняет рассчитанное значение в файл на ПК пользователя
# Планируемый результат:Реализовано приложение для обработки текстовой информации полученной с файла пользователя и
# сохраняющее результат в файловой системе ОС пользователя
# Программа считывает данные из файла user_file и помещает в файл config.yml в соответствующем порядке

import yaml

for_yaml = {}
with open('homework1_9/user_file.txt', mode='r') as file:
    reader = file.read()
reader = reader.replace(',', ' ')
reader = reader.replace('  ', ' ')
reader = reader.replace("'", '')
reader = reader.rstrip()
reader = reader.split(' ')
print(reader)

for i in range(0, len(reader), 2):
    if i == len(reader) - 1:
        break
    else:
        for_yaml[reader[i]] = reader[i + 1]
# for key,value in for_yaml.items():
#     print(key)
#     print(value)


print(for_yaml)

with open('homework1_9/config.yml', 'w') as file:
    yaml.dump(for_yaml, file)
