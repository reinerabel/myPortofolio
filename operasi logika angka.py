print("===========================Operasi Logika Angka==========================\n\n")

angka = float(input("masukan angka lebih dari 0 dan kurang dari 5 arau lebih dari 8 kurang dari 10 :"))
krgdari = (angka > 0)
lbhdari = (angka < 5)
hasil = (krgdari and lbhdari)

krgdari1 = (angka > 8)
lbhdari1 = (angka < 10)
hasil1 = (krgdari1 and lbhdari1)

print(hasil or hasil1)
