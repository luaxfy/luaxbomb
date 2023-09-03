from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if not attribute.startswith('__'):
            servisler_sms.append(attribute)

while True:
    system("cls||clear")
    print(f"""{Fore.LIGHTRED_EX}
\033[93m _                  
| |_   _  __ ___  __
| | | | |/ _` \ \/ /
| | |_| | (_| |>  < 
|_|\__,_|\__,_/_/\_\     
    
    Sms: {len(servisler_sms)}           \033[91mby {Fore.LIGHTRED_EX}@luaxfy\n
    """)
    try:
        menu = input(Fore.LIGHTMAGENTA_EX + " 1- Başlat\n 2- Çıkış\n" + Fore.LIGHTYELLOW_EX + " Bir seçenek seçin: ")
        
        if menu == "":
            continue
        
        menu = int(menu)
        
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Geçersiz giriş.")
        sleep(3)
        continue

    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon Numarasını Girin (örnek: 5555555555): ", end="")
        tel_no = input()
        
        if tel_no == "":
            continue
        
        tel_liste = []
        
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
            tel_liste.append(tel_no)
            sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
            sleep(3)
            continue
        
        system("cls||clear")
        
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        
        system("cls||clear")
        
        try:
            print(Fore.LIGHTYELLOW_EX + f"Kaç adet SMS göndermek istiyorsunuz {sonsuz}: "+ Fore.LIGHTGREEN_EX, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.") 
            sleep(3)
            continue
        
        system("cls||clear")
        
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsunuz: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.") 
            sleep(3)
            continue
        
        system("cls||clear")
        
        if kere is None: 
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if not attribute.startswith('__'):
                            exec("sms."+attribute+"()")
                            sleep(aralik)
        for i in tel_liste:
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                while sms.adet < kere:
                    for attribute in dir(SendSms):
                        attribute_value = getattr(SendSms, attribute)
                        if callable(attribute_value):
                            if not attribute.startswith('__'):
                                if sms.adet == kere:
                                    break
                                exec("sms."+attribute+"()")
                                sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()
        
    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
