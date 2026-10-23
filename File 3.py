nilai = 82
kehadiran = 90

syarat_nilai = nilai >= 75
syarat_kehadiran = kehadiran >= 80

print("Lulus Syarat Nilai:", syarat_nilai)
print("Lulus Syarat Kehadiran:", syarat_kehadiran)

memenuhi_semua = syarat_nilai and syarat_kehadiran
print("Memenuhi Kedua Syarat:", memenuhi_semua)

nilai = 70
syarat_nilai_baru = nilai >= 75
print(nilai >= 75 and kehadiran >= 80)

print(nilai >= 75 or kehadiran >= 80)