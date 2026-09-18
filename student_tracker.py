ogrenciler = []
ayrac = '-' * 5

while True:
    menu_sorgu = input(
        f'\n\n{ayrac} MENÜ {ayrac}\n1 // 2 // 3\n1: Öğrenci Kaydı\n2: Öğrenci Sorgu\n3: Menüden Ayrıl\n:'
    )

    if menu_sorgu == '1':
        isim = input('İsminizi Girin: ')
        notu = int(input('Notunuzu Girin: ')) 
        
        ogrenciler.append({
            'İsim': isim,
            'Notu': notu
        })
        print(f'-> {isim} adlı öğrencinin kaydı başarıyla gerçekleşmiştir.')

    elif menu_sorgu == '2':
        if not ogrenciler:
            print('Error Code: 405\nKayıtlı öğrenci yok')
        else:
            for ogrenci in ogrenciler:
                print(f'Öğrenci İsmi: {ogrenci["İsim"]}, Öğrenci Notu: {ogrenci["Notu"]}')

    elif menu_sorgu == '3':
        print('Sistemden çıkılıyor...')
        break

    else:
        print('Error Code 406:\nYanlış tuşladınız')
