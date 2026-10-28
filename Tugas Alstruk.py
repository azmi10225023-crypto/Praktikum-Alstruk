nama = input("Masukkan Nama Mahasiswa : ")
tugas = float(input("Masukkan Nilai Tugas : "))
uts = float(input("Masukkan Nilai UTS : "))
uas = float(input("Masukkan Nilai UAS : "))

nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

if nilai_akhir >= 60:
    status = "Lulus"
else:
    status = "Belum Lulus"

print("----------------------------")
print("Nama Mahasiswa : " + nama)
print("Nilai Akhir    : " + str(nilai_akhir))
print("Status         : " + status)
