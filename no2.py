file = open("soal.txt", "r")
lines = file.readlines()
file.close()

nomor_file = 1

for i in lines:
    soal = i.strip()
    if nomor_file == 1:
        print("nama file" + str(nomor_file) + ": soal.txt")
    print(soal.split("||")[0].strip())
    jawaban = input("Jawab: ")
    if nomor_file ==4:
        break
    
    if jawaban.lower() == soal.split("||")[1].strip().lower():
        print("Jawaban benar!")
    else:
        print("Jawaban salah!")
    
    nomor_file += 1
