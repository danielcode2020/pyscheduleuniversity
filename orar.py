import os
cls = lambda: os.system('cls')
while True:
    print('Introdu ziua (l,ma,mi,j,v,s): ')
    d = input("")
    print('____________________________')
    if d=='l':
        print('Fizica 08:00')
        print('MS     09:45')
        print('MS     11:30')
        print('Smilja 13:30')
    if d=='ma':
        print('Ed fizica 09:45')
        print('lab SDA   11:15')
        print('MSp/SDA   13:30')
    if d=='mi':
        print('Fizica 08:00')
        print('MS     09:45')
    if d=='j':
        print('Lab Fizica 08:00')
        print('Fizica     09:45')
        print('FER        11:15')
    if d=='v':
        print('SDA    08:00')
        print('FER    09:45')
        print('FER    11:15')
    if d=='s':
        print('L FR   08:00')
        print('M Sp   09:45')
        print('M S    11:15')
    print('____________________________')
    print('Din nou (d/n ): ')
    a = input("")
    if a=='n':
        break
    if a=='d':
        cls()
        
