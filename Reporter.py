import time

a = 1
while a == 1:
    timeM = time.strftime('%M')
    timeS = time.strftime('%S')
    if int(timeS) == 00:

        regBiSK = 0
        regIKPI = 0
        regKBKiRT = 0
        regZN = 0
        regAbitur = 0
        newRegBiSK = 0
        newRegIKPI = 0
        newRegKBKiRT = 0
        newRegZN = 0
        newRegAbitur = 0
        globalRegBisk = 0
        globalRegIKPI = 0
        globalRegKBKiRT = 0
        globalRegZN = 0
        globalRegAbitur = 0

        # Считывание количества переходов

        fileStudBiSK = open(r'Files\Reports\repStudBiSK.txt', 'r')
        for row in fileStudBiSK:
            for letter in row:
                regBiSK = regBiSK + 1
        fileStudBiSK.close()
        fileStudIKPI = open(r'Files\Reports\repStudIKPI.txt', 'r')
        for row in fileStudIKPI:
            for letter in row:
                regIKPI = regIKPI + 1
        fileStudIKPI.close()
        fileStudKBKiRT = open(r'Files\Reports\repStudKBKiRT.txt', 'r')
        for row in fileStudKBKiRT:
            for letter in row:
                regKBKiRT = regKBKiRT + 1
        fileStudKBKiRT.close()
        fileStudZN = open(r'Files\Reports\repStudZN.txt', 'r')
        for row in fileStudZN:
            for letter in row:
                regZN = regZN + 1
        fileStudZN.close()
        fileAbitur = open(r'Files\Reports\repAbitur.txt', 'r')
        for row in fileAbitur:
            for letter in row:
                regAbitur = regAbitur + 1
        fileAbitur.close()

        # Подсчёт с общим количеством

        fileRep = open('Report.txt', 'r', encoding='utf-8')
        line = 1
        for row in fileRep:
            line = line + 1
            if line == 3:
                newRegBiSK = regBiSK + int(row)
                globalRegBisk = newRegBiSK
            if line == 5:
                newRegIKPI = regIKPI + int(row)
                globalRegIKPI = newRegIKPI
            if line == 7:
                newRegKBKiRT = regKBKiRT + int(row)
                globalRegKBKiRT = newRegKBKiRT
            if line == 9:
                newRegZN = regZN + int(row)
                globalRegZN = newRegZN
            if line == 11:
                newRegAbitur = regAbitur + int(row)
                globalRegAbitur = newRegAbitur
        fileRep.close()

        # Перезапись файла с отчётом

        fileRep = open('Report.txt', 'w', encoding='utf-8')
        fileRep.write('Всього перейшло до розділу студентів БіСК:\n')
        fileRep.write(str(globalRegBisk))
        fileRep.write('\nВсього перейшло до розділу студентів ІКПІ:\n')
        fileRep.write(str(globalRegIKPI))
        fileRep.write('\nВсього перейшло до розділу студентів КБКіРТ:\n')
        fileRep.write(str(globalRegKBKiRT))
        fileRep.write('\nВсього перейшло до розділу студентів ЗН:\n')
        fileRep.write(str(globalRegZN))
        fileRep.write('\nВсього перейшло до розділу абітурієнтів:\n')
        fileRep.write(str(globalRegAbitur))
        fileRep.close()

        # Удаление данных старых отчётов

        fileStudBiSK = open(r'Files\Reports\repStudBiSK.txt', 'w')
        fileStudBiSK.close()
        fileStudIKPI = open(r'Files\Reports\repStudIKPI.txt', 'w')
        fileStudIKPI.close()
        fileStudKBKiRT = open(r'Files\Reports\repStudKBKiRT.txt', 'w')
        fileStudKBKiRT.close()
        fileStudZN = open(r'Files\Reports\repStudZN.txt', 'w')
        fileStudZN.close()
        fileAbitur = open(r'Files\Reports\repAbitur.txt', 'w')
        fileAbitur.close()

    while int(timeS) == 00:
        timeM = time.strftime('%M')
        timeS = time.strftime('%S')


