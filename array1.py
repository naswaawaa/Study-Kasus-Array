# Deklarasi array untuk menyimpan ngka
angka = []

# Meminta input pengguna
for i in range(5):
    elemen = int(input(f"Masukkan angka ke-{i+1}:"))
    angka.append(elemen)
  
# Menghitung frekuensi kemunculan   
frekuensi = {}
for elemen in angka:
    if elemen in frekuensi:
        frekuensi[elemen] += 1
    else:
        frekuensi[elemen] = 1
 
# Menampilkan hasil        
for elemen, jumlah in frekuensi.items():
    print(f"Angka {elemen} muncul sebanyak {jumlah} kali.")