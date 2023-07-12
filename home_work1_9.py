# Реализация приложения, которое считывает данные с файла, и сохраняет рассчитанное значение в файл на ПК пользователя
# Планируемый результат:Реализовано приложение для обработки текстовой информации полученной с файла пользователя и
# сохраняющее результат в файловой системе ОС пользователя
# Программа считывает данные из файла user_file.txt и помещает в файл config.yml в соответствующем порядке
# Дополнительно установлена библиотека pyyaml

import yaml
import os

to_yaml = {}
with open('homework1_9/user_file.txt', mode='r') as file:
    reader = file.read()
reader = reader.replace(',', ' ')
reader = reader.replace('  ', ' ')
reader = reader.replace("'", '')
reader = reader.rstrip()
reader = reader.split(' ')

for i in range(0, len(reader), 2):
    if i == len(reader) - 1:
        break
    else:
        to_yaml[reader[i]] = reader[i + 1]

with open('homework1_9/config.yml', 'w') as file:
    yaml.safe_dump(to_yaml, file, sort_keys=False)

path = os.path.abspath('homework1_9/config.yml')
print(f'Программа завершила работу,результат сохранен в файле по адресу: {path}')
