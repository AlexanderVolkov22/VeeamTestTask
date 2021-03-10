# Usage python3 main.py <name>

import sys
import subprocess


def func(fl):
    sp1 = subprocess.Popen("lsblk -o type " + fl + " | head -2 | tail -1", shell=True, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)  # Получение типа файла
    tp = sp1.communicate()[0]
    tp = bytes.decode(tp, encoding='utf-8').rstrip()
    if tp == 'part':  # Проверка на раздел
        sp = subprocess.Popen('df -h --output=source,size,used,fstype,target ' + fl + " | tail -1", shell=True,
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  # Получение информации о разделе
        pt = sp.communicate()[0]
        pt = bytes.decode(pt, encoding='utf-8').rstrip().replace(fl, fl + " " + tp).replace('       ', '') #
        # Финальное форматирование информации
        print(pt)
    else:
        sp = subprocess.Popen('lsblk -o type,size ' + fl + ' | head -2 | tail -1', shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)  # Получение информации о диске или другом девайсе
        els = sp.communicate()[0]
        els = fl + " " + bytes.decode(els, encoding='utf-8').rstrip()  # Финальное форматирование информации
        print(els)


if __name__ == '__main__':
    fl = sys.argv[1]  # Получение аргумента из консоли linux
    func(fl)
