# Данный пример демонстрирует чтение тока с третьего канала.
                                    # * Строки со звёздочкой являются необязательными.
from pyiArduinoI2Crelay import *    # Подключаем модуль для работы с ключём
from time import sleep              # Подключаем функцию ожидания из модуля времени
pwrfet = pyiArduinoI2Crelay(0x09)   # Объявляем объект pwrfet
i = 0                               #
                                    #
pwrfet.digitalWrite(ALL_CHANNEL,LOW)# * Выключаем все каналы модуля.
                                    #
while True:                         #
#  Управляем каналом N 3:
    if i==0:                        # Если в переменной хранится значение 0
        pwrfet.digitalWrite(4,HIGH) # включаем 3 канал
    if i==128:                      # если в переменной хранится значение 128
        pwrfet.digitalWrite(4, LOW) # отключаем 3 канал 
                                    #
#  Выводим силу тока 
#  проходещего по 3 каналу:
    j = pwrfet.currentRead(4)       # Считываем силу тока с третьего канала в переменную j.
    print("Сила тока %.3f" % j      #
          +" А.", end = '\r')       # Выводим силу тока в stdout.
#  Приостанавливаем
#  выполнение скетча:
    i+=4                            # Увеличиваем счётчик i на 4
    sleep(.1)                       # и ждем 100 мс, до сброса переменной i пройдет = 6,4 сек.
    if i > 255: i = 0               # Сбрасываем i при достижении 256 
                                                                   
# ПРИМЕЧАНИЕ: Третий канал будет включаться и отключаться.
# Если к третьему каналу подключить нагрузку, то в stdout
# будет отображаться ток потребляемый нагрузкой в то время пока
# канал включён. Если канал выключен
# (или нагрузка отсутствует) ток будет равен 0.00 А
