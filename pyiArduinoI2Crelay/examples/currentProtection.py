# Данный пример защищает 3 и 4 каналы от превышения тока.
                                             # * Строки со звёздочкой являются необязательными.
from pyiArduinoI2Crelay import *             # Подключаем модуль для работы с ключём
from time import sleep                       # Подключаем функцию ожидания из модуля времени
pwrkey = pyiArduinoI2Crelay(0x09)            # Объявляем объект pwrkey
pwrkey.digitalWrite(1,LOW)                   # * Отключаем 1 канал модуля.
pwrkey.digitalWrite(2,LOW)                   # * Отключаем 2 канал модуля.
pwrkey.digitalWrite(3,HIGH)                  #   Включаем  3 канал модуля.
pwrkey.digitalWrite(4,HIGH)                  #   Включаем  4 канал модуля.
#  Устанавливаем защиту по току: 
pwrkey.setCurrentProtection(3, 1.0, 
                            CURRENT_LIMIT)   # Включаем функцию ограничения тока до 1А на третьем канале.
pwrkey.setCurrentProtection(4, 2.0,
                            CURRENT_DISABLE) # Включаем функцию отключения нагрузки при повышении тока выше 2А на четвёртом канале.
                                             # Если для одного канала включить сразу две функции, то будет работать только последняя.
                                             #
while True:                                  #
#  Проверяем выполняется ли функция ограничения тока, включенная на 3 канале #
    if pwrkey.getCurrentProtection(3):       # Если на третьем канале выполняется функция ограничения тока, то ...
        print("На 3 канале "                 # Выводим сообщение о том что ток третьего канала 
              "выполняется функция "         # ограничивается модулем при помощи ШИМ.
              "ограничения тока." )          #
                                             #
#  Проверяем не отключена ли нагрузка на 4 канале в связи с превышением тока
    if pwrkey.getCurrentProtection(4):       # Если на четвёртом канале выполнено отключение нагрузки 
        print("Нагрузка 4 канала "           # Выводи сообщение о том что нагрузка четвёртого канала отключена.
              "отключена из-за " 
              "превышения тока.")  
    # Для восстановления работы нагрузки
    # разкомментируйте следующие строки:
    #  pwrkey.resCurrentProtection(4)        # * Перезапускаем защиту 4 канала.
    #  pwrkey.digitalWrite(4,HIGH)           # * Включаем 4 канал модуля (если ток по прежнему превышает
                                             # указанные ранее 2А, то нагрузка вновь отключится).
    sleep(1)                                 #
#  ПРИМЕЧАНИЕ:                                                              
#  Если нагрузка канала отключена, то для её включения необходимо ...
#  - либо отключить     защиту функцией delCurrentProtection()
#  - либо перезапустить защиту функцией resCurrentProtection()
#  В противном случае канал останется отключённым.
