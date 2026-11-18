stok = ["Beras", "Gula", "Minyak", "Telur"]
print("Stok awal :", stok)

stok.append("Kopi")
stok[1] = "Gula Pasir"
stok.remove("Telur")

print("Stok update :", stok)
print("Barang pertama :", stok[0])
print("Total jenis barang :", len(stok))