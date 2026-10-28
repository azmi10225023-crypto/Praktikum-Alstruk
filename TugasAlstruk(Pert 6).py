print(" SISTEM ABSENSI NGAJI PP MIFTAHUL HIDAYAH CIBALONG TASIKMALAYA")

nama_santri = input("Masukkan Nama Santri : ")
jumlah_absen = int(input("Jumlah Alpa/Absen Ngaji (Hari): "))

if jumlah_absen > 3:
    status = "Dihukum"
    catatan = "Wajib membersihkan balong beserta wc."
else:
    status = "Aman"
    catatan = "Bagus,pertahankan!"

print("Nama Santri  :", nama_santri)
print("Status Absen :", status)
print("Keterangan   :", catatan)
