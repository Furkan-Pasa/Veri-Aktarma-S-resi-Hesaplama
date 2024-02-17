# Furkan "Paşa" Çelik
# 2024.02.17

import os
import time
import subprocess

# Kullanılan Değişkenler:
# temp , dongu , e , boyut , boyut_mb , hiz , hiz_mb , sure , gun , saat , dakika , saniye

def main():
    
    # Windows terminalinde açık mor rengi ayarlar.
    if os.name == 'nt':
        subprocess.run(["cmd", "/c", "color d"])
    # Linux terminalinde mor rengi ayarlar. 
    if os.name == 'posix':
        subprocess.run(["tput", "setaf", "5"])
        
    print("\n Veri Aktarma Süresini Hesaplama Programı \n ")
    
    time.sleep(1)
    # Verinin boyutu alınır.
    boyut, boyut_mb = boyut_al()
    
    # Programın sonunda, aynı veri boyutunu farklı bir hızla hesaplamak istendiğinde döngü tekrarlanır.
    dongu = 1
    while dongu == 1:
        
        time.sleep(1) 
        # Aktarma hızı alınır.
        hiz, hiz_mb = hiz_al()
    
        time.sleep(2) 
        # Eğer işletim sistemi Windows ise, 'cls' komutunu kullanarak terminali temizler. 
        # Değil ise clear komutu kullanarak terminali temizler.
        os.system('cls' if os.name == 'nt' else 'clear')
    
        # Sonuç ekrana yazdırılır
        sonuc(boyut,hiz,boyut_mb,hiz_mb)
        
        # Döngünün kırılması için 0 değeri verilir.
        dongu = 0
    
        print("\n     Farklı bir hız girmek için 1 yazın")
        temp = input("\n     Çıkmak için enter tuşuna basın...\n\n      ")
        
        if temp == '1':
            # Döngünün tekrar etmesi için 1 değeri verilir.
            dongu = 1
            print("")
            
        elif temp == '':
            print("     Program sonlandırılıyor.")
            time.sleep(2)
            quit()
            
        else:
            print("   Hata-F1: Geçersiz bir seçim yaptınız. Program sonlandırılıyor.")
            time.sleep(3)
            quit()
        
    
#  Veri Boyutunu almak için kullanılan fonksiyon.
def boyut_al():
  
    print(" 1) Aktarılacak verinin boyutunu \"GigaByte\" olarak girmek istiyorum")
    print(" 2) Aktarılacak verinin boyutunu \"MegaByte\" olarak girmek istiyorum")

    temp = input("\n Yukarıda listelenen ölçü birimlerinden birini seçiniz. (Varsayılan değer 1) > ")
    
    if temp == '1' or temp == '':
        try:
            # Girdi String olarak alınır.
            boyut = input("\n Dosyanın boyutunu \"GigaByte\" olarak giriniz: ")
            # Kullanıcının girdisinde virgül varsa noktaya çevirilir.
            boyut = boyut.replace(',', '.')
            # Ondalıklı sayıya çevirilir.
            boyut_mb = float(boyut)
            # GB dan MB ölçüsüne dönüştürülür.
            boyut_mb *= 1024
            # İleride ekrana yazdırmak için stringin sonuna Gb takısı eklenir.
            boyut = boyut + ' Gb'
            # Eğer girilen sayı 0 veya negatif sayı ise bu hata mesajı yazdırılır.
            if boyut_mb <= 0:
                raise ValueError("\n\n Hata-B11: Negatif bir değer veya 0 girdiniz! Program sonlandırılıyor.")
        except ValueError as e:
            print(e)
            time.sleep(5)
            quit()
        except:
            print("\n\n Hata-B12: Beklenmeyen bir hata oluştu! Lütfen pozitif bir sayı girdiğinizden emin olun!")
            time.sleep(5)
            quit()
          
    elif temp == '2':
        try:
            # Girdi String olarak alınır.
            boyut = input("\n  Dosyanın boyutunu \"MegaByte\" olarak giriniz: ")
            # Kullanıcının girdisinde virgül varsa noktaya çevirilir.
            boyut = boyut.replace(',', '.')
            # Ondalıklı sayıya çevirilir.
            boyut_mb = float(boyut)
            # İleride ekrana yazdırmak için stringin sonuna Mb takısı eklenir.
            boyut = boyut+' Mb'
            # Eğer girilen sayı 0 veya negatif sayı ise bu hata mesajı yazdırılır.
            if boyut_mb <= 0:
                raise ValueError("\n\n Hata-B21:Negatif bir değer veya 0 girdiniz! Program sonlandırılıyor.")
        except ValueError as e:
            print(e)
            time.sleep(5)
            quit()
        except:
            print("\n\n Hata-B22: Beklenmeyen bir hata oluştu! Lütfen pozitif bir sayı girdiğinizden emin olun!")
            time.sleep(5)
            quit()
  
    else:
        print("\n   Hata-B30: Geçersiz bir seçim yaptınız. Program sonlandırılıyor.")
        time.sleep(3)
        quit()
    
    print("")
    return boyut, boyut_mb
    
    
#  Aktarma hızını almak için kullanılan fonksiyon.
def hiz_al():   
    
    print(" 1) Aktarma hızını \"MegaBit/s\" olarak girmek istiyorum")
    print(" 2) Aktarma hızını \"MegaByte/s\" olarak girmek istiyorum")
    
    temp = input("\n Yukarıda listelenen aktarım hızı birimlerinden birini seçiniz. (Varsayılan değer 1) > ")
 
    if temp == '1' or temp == '': 
        try:
            # Girdi String olarak alınır.
            hiz = input("\n Aktarma hızını \"MegaBit/s\" olarak giriniz: ")
            # Kullanıcının girdisinde virgül varsa noktaya çevirilir.
            hiz = hiz.replace(',', '.')
            # Ondalıklı sayıya çevirilir.
            hiz_mb = float(hiz)
            # Mbps dan Mb/s ölçüsüne dönüştürülür.
            hiz_mb /= 8
            # İleride ekrana yazdırmak için stringin sonuna Mbps takısı eklenir.
            hiz = hiz + ' Mbps'
            # Eğer girilen sayı 0 veya negatif sayı ise bu hata mesajı yazdırılır.
            if hiz_mb <= 0:
                raise ValueError("\n\n Hata-H11: Negatif bir değer veya 0 girdiniz! Program sonlandırılıyor.")
        except ValueError as e:
            print(e)
            time.sleep(5)
            quit()
        except:
            print("\n\n Hata-H12: Beklenmeyen bir hata oluştu! Lütfen pozitif bir sayı girdiğinizden emin olun!")
            time.sleep(5)
            quit()     
       
    elif temp == '2':

        try:
            # Girdi String olarak alınır
            hiz = input("\n Aktarma hızını \"MegaByte/s\" olarak giriniz: ")
            # Kullanıcının girdisinde virgül varsa noktaya çevir
            hiz = hiz.replace(',', '.')
            # Ondalıklı sayıya çevirilir
            hiz_mb = float(hiz)
            # İleride ekrana yazdırmak için stringin sonuna Mb/s takısı eklenir
            hiz = hiz+' Mb/s'
            # Eğer girilen sayı 0 veya negatif sayı ise bu hata mesajı yazdırılır.
            if hiz_mb <= 0:
                raise ValueError("\n\n Hata-H21:Negatif bir değer veya 0 girdiniz! Program sonlandırılıyor.")
        except ValueError as e:
            print(e)
            time.sleep(5)
            quit()
        except:
            print("\n\n Hata-H22: Beklenmeyen bir hata oluştu! Lütfen pozitif bir sayı girdiğinizden emin olun!")
            time.sleep(5)
            quit()
        
    else:
        print("\n   Hata-H30: Geçersiz bir seçim yaptınız. Program sonlandırılıyor.")
        time.sleep(3)
        quit()
    
    print("")
    return hiz, hiz_mb
    
    
def sonuc(boyut,hiz,boyut_mb,hiz_mb):
    
    print("\n\n    Boyut =",boyut,"| Hız =",hiz)
    
    sure = int(boyut_mb/hiz_mb)
    
    # print("\n Aktarma İşleminin Süresi:",sure,"Saniye")

    gun = int(sure / 86400)
    sure %= 86400
    saat = int(sure / 3600)
    sure %= 3600
    dakika = int(sure / 60)
    sure %= 60
    saniye = int(sure)
    print(f"\n    Aktarma İşleminin Süresi: {gun} gun, {saat} saat, {dakika} dakika, {saniye} saniye \n ")
    
    
 
main()