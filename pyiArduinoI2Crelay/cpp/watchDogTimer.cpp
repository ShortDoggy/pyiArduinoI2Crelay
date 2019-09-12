// Данный пример демонстрирует защиту от зависания шины или Arduino      // * Строки со звёздочкой являются необязательными.
                                        //
#include <iostream>                     //
#include "../iarduino_I2C_Relay.h"      //   Подключаем библиотеку для работы с реле и силовыми ключами.
iarduino_I2C_Relay pwrfet(0x09);        //   Объявляем объект pwrfet для работы с функциями и методами библиотеки iarduino_I2C_Relay, указывая адрес модуля на шине I2C.
                                        //   Если объявить объект без указания адреса (iarduino_I2C_Relay pwrfet;), то адрес будет найден автоматически.
void loop(void);                        //
                                        // 
int main(){                             //
//  Готовим модуль к работе:            //
    pwrfet.begin();                     //   Инициируем работу с модулем.
    pwrfet.enableWDT(5);                //   Разрешаем работу сторожевого таймера модуля, задав время до перезагрузки 5 сек.
    loop();                             //
}                                       //   Отключить работу сторожевого таймера модуля можно функцией disableWDT().
                                        //
void loop(){                            //
    while (true) {                      //
        //  Переключаем 1 и 2 каналы модуля:
        pwrfet.digitalWrite(1,HIGH);    // Включаем 1 канал
        pwrfet.digitalWrite(2,LOW);     // выключаем 2 канал 
        delay(500);                     // ждём 500 мс.
        pwrfet.digitalWrite(2,HIGH);    // Включаем 2 канал
        pwrfet.digitalWrite(1,LOW);     // выключаем 1 канал 
        delay(500);                     // ждём 500 мс.
        //  Сбрасываем (перезапускаем) сторожевой таймер модуля:
        pwrfet.resetWDT();              //   Теперь таймер модуля начнёт заново отсчитывать 5 секунд до перезагрузки.
        //  Сообщаем, что сработал сторожевой таймер:
        if (pwrfet.getStateWDT()        //
                        == false ) {    // * Если таймер отключился, значит он досчитал до 0 
            std::cout << "ERROR\n";     // и перезагрузил модуль отключив все его каналы.
        }                               //             
    }                                   //   Если модуль не отвечает (отключилась шина I2C), то функция getStateWDT() так же вернёт false.
}                                       //
                                        //
/*  *******************************************************************
    ПРИМЕЧАНИЕ:
    Время назначенное сторожевому таймеру функцией enableWDT(),               (в примере назначено 5 секунд)
    должно быть больше чем время между вызовами функции resetWDT().           (в примере функция resetWDT вызывается один раз в секунду)

    ПРОВЕРКА:
    Если во время работы отключить вывод SDA или SCL шины I2C, то каналы
    перестанут переключаться, но 1 из каналов модуля останется включённым.
    Подождав от 4 до 5 секунд, сработает таймер и все каналы отключатся.      (время ожидания зависит от того, в каком месте выполнения кода был отключён вывод)
*/
