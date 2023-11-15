# Menampilkan Elemen List
list = [1, 2, 3, "aku", "baik"]
print(list[2])
print(list[1:4])
print(list[-1])

# Mengubah Elemen List
list = [1, 2, 3, "aku", "baik"]
list[3] = "dia"
print(list)
list[3:] = ["kamu" , "jahat"]
print(list)

# Tambah Elemen List
listA = [1, 2, 3, "kamu", "jahat"]
listB = listA[2:4]
print(listB)
listB.append("hallo")
print(listB)
listB.extend([4, 7, 9])
print(listB)
gabungkan_list = listB + listA
print(gabungkan_list)