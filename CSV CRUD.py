import csv 
nim = []
nama = []
with open('DaftarNama.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        nim.append(row[0])
        namaCapital = row[1].title()
        nama.append(namaCapital)

def merge(list1, list2): 
    mergedList = [[list1[i], list2[i]] for i in range(0, len(list1))] 
    return mergedList 

def lihatData():
    print(20*'='+'Lihat Data'+20*'=')
    for row in nim:
        index = nim.index(row)
        print(row, end = " ")
        print(nama[index])

def tambahData():
    print(20*'='+'Tambah Data'+20*'=')
    nim.append(input("NIM =  "))
    namaBaru = ' '+(input("Nama = "))
    nama.append(namaBaru)
    with open('DaftarNama.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')        
        for i,j in zip(nim,nama):
            writer.writerow([i]+[j])
    csv_file.close()
    print('Data telah ditambahkan!')

def cariData():
    data = merge(nim,nama)
    print(20*'='+'Cari Data'+20*'=')
    pil = int(input('1. Cari dengan NIM(binary search)\n2. Search partial (yang mengandung unsur)\nPilihan = '))
    if pil==1:
        nimInt =[]
        for i in range(len(nim)):
            nimInt.append(int(nim[i]))
        left = 0
        right = len(nim)-1
        cari = int(input('Input = '))
        while left<=right:
            mid = (left+right)//2
            if nimInt[mid]==cari:
                print("NIM = "+nim[mid]+'\nNama = '+nama[mid])
                break
            elif nimInt[mid]<cari:
                left = mid+1
            else:
                right = mid-1
        else:
            print('Pencarian selesai\nGunakan pencarian partial agar lebih mudah')
    elif pil==2:
        cari = input('\nCari parsial(no capital) = ')
        for i in range(len(data)):
            if (data[i])[0].find(cari)==-1:
                continue
            else:
                print((data[i])[0]+(data[i])[1])
        for i in range(len(data)):  
            if ((data[i])[1].lower()).find(cari)==-1:
                continue
            else:
                print((data[i])[0]+(data[i])[1])
        else:
            print('Pencarian selesai!')

def hapusData():
    print(20*'='+'Hapus Data'+20*'=')
    drop = input('Data yang dihapus = ')
    if drop in nim:
        place = nim.index(drop)
        nim.remove(nim[place])
        nama.remove(nama[place])
        with open('DaftarNama.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')        
            for i,j in zip(nim,nama):
                writer.writerow([i]+[j])
        print('Data telah dihapus!')
        csv_file.close()
    elif drop in nama:
        place = nim.index(drop)
        nim.remove(nim[place])
        nama.remove(nama[place])
        with open('DaftarNama.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')        
            for i,j in zip(nim,nama):
                writer.writerow([i]+[j])
        print('Data telah dihapus!')
        csv_file.close()
    else:
        print("Data tidak ditemukan!")

def urutkanData():
    data = merge(nim,nama)
    max = len(data)-1
    pil = int(input('1. Urut berdasarkan NIM asc\n2. Urut berdasarkan NIM desc\n3. Urut berdasarkan nama asc\n4. Urut berdasarkan nama desc\nPilihan = '))
    if pil==1:
        print('Urut berdasarkan NIM asc')
        for x in range(max,0,-1):
            for y in range(x):
                if (data[y])[0]>(data[y+1])[0]:
                    temp = data[y+1]
                    data[y+1] = data[y]
                    data[y] = temp
        for row in data:
            for col in row:
                print(col, end=' ')
            print()
    elif pil==2:
        print('Urut berdasarkan NIM desc')
        for x in range(max,0,-1):
            for y in range(x):
                if (data[y])[0]<(data[y+1])[0]:
                    temp = data[y+1]
                    data[y+1] = data[y]
                    data[y] = temp
        for row in data:
            for col in row:
                print(col, end=' ')
            print()
    elif pil==3:
        for x in range(max,0,-1):
            for y in range(x):
                if (data[y])[1]>(data[y+1])[1]:
                    temp = data[y+1]
                    data[y+1] = data[y]
                    data[y] = temp
        for row in data:
            for col in row:
                print(col, end=' ')
            print()
    elif pil==4:
        for x in range(max,0,-1):
            for y in range(x):
                if (data[y])[1]<(data[y+1])[1]:
                    temp = data[y+1]
                    data[y+1] = data[y]
                    data[y] = temp
        for row in data:
            for col in row:
                print(col, end=' ')
            print()
    else:
        print('Salah Input!')

while True :    
    print(100*'=')
    pilihan = int(input('\n\t\tProgram Manipulasi DaftarNama.csv\n1. Lihat seluruh isi data\n2. Menambah data\n3. Cari data\n4. Hapus data\n5. Urutkan data\n6. Exit\nPilihan = '))
    if pilihan >= 1 and pilihan <= 6:
        if pilihan == 1:
             lihatData()
        elif pilihan == 2:
             tambahData()
        elif pilihan == 3:
             cariData()
        elif pilihan == 4:
             hapusData()
             print()
        elif pilihan == 5:
             urutkanData()
        elif pilihan == 6:
             print(20*'='+'Closing the Program'+20*'=')
             exit()
    else:
        print('Maaf, Anda salah input pilihan')