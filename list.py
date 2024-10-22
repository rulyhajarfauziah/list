
my_list = ["prodi TI",1,2,3,4,1,2]

panjang_my_list = len(my_list)

#cetak list
print("my list:", my_list)
print("panjang list:",panjang_my_list)
print("panggil index ke 5:", my_list[5])


my_list.append("keren")
print("my_list setelah diinput nilai baru: ", my_list)

print("my_list setelah menghapus nilai 2: ", my_list)

my_list.remove(2)

print("my_list setelah menghapus nilai 2: ", my_list)


del my_list[1]

print("my_list setelah menghapus index ke 1: ", my_list)
