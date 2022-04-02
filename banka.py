# Web Sitem : https://arinweb.epizy.com
# Instagram : @arin_web
# Daha fazlası için takipte kal
# - - Arin Bank - - 

from getpass import getpass
import os
clear = lambda: os.system('clear')
clear()

pass_x = 1

while pass_x == 1:
  print('''
  -- Arin Bank --
  => @arin_web
  => https://arinweb.epizy.com
''')
  password = getpass('Banka Şifreniz: ')
  if password == '0000':
    print('Şifreniz Doğru')
    clear()
    pass_x = 0
  else:
    print('--- Şifreniz Yanlış!!')
    clear()

x = 1
elde_para = int(100)
bankadaki_para = int(50)
kredi = int(100000)
kredi_odenecek = int(0)

#-- FAİZ --
def faiz(x,y=30):
  x = x/y
  int(x)
  return x

while x == 1:
  if kredi_odenecek > 0:
    kredi_odenecek += 1
  print('''
  -- Arin Bank --

   [ 1 ] Hesabımdan Çek
   [ 2 ] Hesabıma Yatır
   [ 3 ] Kredi Çek
   [ 4 ] Kredi Öde
   [ 5 ] Sayfayı Yenile

   [ 0 ] Çıkış Yap

   Hesabımdaki Para: {x_para} TL | Elde Bulunan Para: {y_para} TL

   Kredi Ödenecek Tutar: {z_para} TL | Faiz: {faiz_text} TL
  '''.format(x_para=bankadaki_para,y_para=elde_para,z_para=int(kredi_odenecek),faiz_text=int(faiz(kredi_odenecek)))) 

  in_x = int(input(' [ARİN] İşlem Numarası: ')) 

  if in_x == 1:
      cekilecek_tutar = int(input(' [ARİN] Çekilecek Tutar: '))
      if bankadaki_para < cekilecek_tutar or cekilecek_tutar < 0: 
        clear()
        print('  Paranız Yetersiz: '+str(bankadaki_para)+' TL')
      else:
        clear()
        print('  Para Çekme İşlemi Başarılı: '+str(cekilecek_tutar)+' TL')
        bankadaki_para -= cekilecek_tutar
        elde_para += cekilecek_tutar

  elif in_x == 2:
      yatirilacak_tutar = int(input(' [ARİN] Yatırılacak Tutar: '))
      if elde_para < yatirilacak_tutar or yatirilacak_tutar < 0:
        clear()
        print('  Paranız Yetersiz: '+str(elde_para)+' TL')
      else:
        clear()
        print('  Para Yatırma İşlemi Başarılı: '+str(yatirilacak_tutar)+' TL')
        elde_para -= yatirilacak_tutar
        bankadaki_para += yatirilacak_tutar

  elif in_x == 3:
      cekilecek_kredi = int(input(' [ARİN] Çekilecek Kredi: '))
      if cekilecek_kredi > kredi or cekilecek_kredi < 0:
        clear()
        if kredi == 0:
          print('  Kredi Limitiniz Dolmuştur!!')
        else:
          print('  Çekeceğiniz Kredi 0 ile {x} TL Arasında Olmalıdır '.format(x=kredi))
      else:
        clear()
        print('''
  -- Arin Bank --

   {x} TL Hangi konuma yatırılsın ?

   [ 1 ] Hesabıma Yatır
   [ 2 ] Elden Al

   [ 0 ] İptal Et
        '''.format(x=cekilecek_kredi))
        kredi_konum = int(input(' [ARİN] Kredi Konumu: '))
        match kredi_konum:
          case 1:
            clear()
            print('  Kredi Çekme İşlemi Başarılı')
            print('  Krediniz Hesabınıza Yüklendi: '+str(cekilecek_kredi)+' TL')
            kredi -= cekilecek_kredi
            bankadaki_para += cekilecek_kredi
            kredi_odenecek = kredi_odenecek+cekilecek_kredi+faiz(kredi_odenecek)
          case 2:
            clear()
            print('  Kredi Çekme İşlemi Başarılı')
            print('  Krediniz Elden Verildi: '+str(cekilecek_kredi)+' TL')
            kredi -=  cekilecek_kredi
            elde_para += cekilecek_kredi
            kredi_odenecek = kredi_odenecek+cekilecek_kredi+faiz(kredi_odenecek)
          case 0:
           clear()
           print('  İşleminiz İptal Edilmiştir!!')

  elif in_x == 4:
    if kredi_odenecek <= 0:
      clear()
      print('  Kredi Ödeneğiniz Bulunmamaktadır!!')
    else:
      clear()
      print('''
  -- Arin Bank --
   Kredi ödeme tipi seçin?

   Toplam Kredi Ödeneği: {x} TL

   [ 1 ] Tümünü Öde
   [ 2 ] Miktar Öde

   [ 0 ] İptal Et
      '''.format(x=kredi_odenecek))
      kredi_odeme_tipi = int(input(' [ARİN] Kredi Ödeme Tipi: '))
      match kredi_odeme_tipi:
        case 1:
          if kredi_odenecek > bankadaki_para:
            clear()
            print('Bakiyeniz Yetersiz!!')
          else:
            clear()
            print('Tüm Krediniz Ödenmiştir | {x}'.format(x=kredi_odenecek))
            bankadaki_para -= kredi_odenecek
            kredi_odenecek = 0
        case 2:
          odenecek_kredi = int(input(' [ARİN] Ödenecek Kredi: '))
          if kredi_odenecek <= odenecek_kredi or odenecek_kredi > 0:
            clear()
            bankadaki_para -= odenecek_kredi
            kredi_odenecek -= odenecek_kredi
        case 0:
          clear()
          print('  İşleminiz İptal Edilmiştir!!')
  elif in_x == 5:
    print('Sayfa Yenileniyor...')
    clear()
  elif in_x == 0:
    print('-- Hoşçakal --')
    exit();
  else:
    clear()
