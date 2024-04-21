file1 = 'file1.txt'
file2 = 'file2.txt'

f1 = open(file1, 'r')
f2 = open(file2, 'r')

lines1 = f1.readlines()
lines2 = f2.readlines()

f1.close()
f2.close()

isi_line = max(len(lines1), len(lines2))

for i in range(isi_line):
    if i < len(lines1) and i < len(lines2):
        line1 = lines1[i].strip()
        line2 = lines2[i].strip()
        if line1 != line2:
            print(f'Baris {i+1}:')
            print(f'File 1: {line1}')
            print(f'File 2: {line2}')
  
    elif i < len(lines1):
        print(f'Baris {i+1}:')
        print(f'File 1: {lines1[i].strip()}')
        print('File 2: {lines2[i].strip()}')
        
    elif i < len(lines2):
        print(f'Baris {i+1}:')
        print('File 1: [lines1[i].strip()]')
        print(f'File 2: {lines2[i].strip()}')

