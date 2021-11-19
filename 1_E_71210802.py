print('=====Kalkulator Akar dan Pangkat=====')
print('Pilihan menu :')
print('  1. Pangkat 2 (Kuadrat)')
print('  2. Pangkat 3 (Kubik)')
print('  3. Akar Kuadrat')

menu = input('Masukkan menu yang anda pilih: ')
print("")
if menu == '1':
    angka = eval(input('Masukkan bilangan yang ingin di pangkatkan: '))
elif menu == '2':
    angka = eval(input('Masukkan bilangan yang ingin di pangkatkan: '))
elif menu == '3':
    angka = eval(input('Masukkan bilangan yang ingin di akarkan: '))
        
if menu == '1':
  hasil = angka ** 2
  print(f'Hasil dari pemangkatan bilangan {angka} dengan {2} (Kuadrat) adalah {hasil}')
elif menu == '2':
  hasil = angka ** 3
  print(f'Hasil dari pemangkatan bilangan {angka} dengan {3} (Kubik) adalah {hasil}')
elif menu == '3':
  hasil = sqrt=angka**(1/2) 
  print(f'Hasil akar kuadrat dari bilangan {angka} adalah = {hasil}')
else:
  print('Pilihan menu yang dimasukkan tidak sesuai!')
