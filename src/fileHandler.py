import os
import time
import protocol, matrix
import datetime

def readFile(filePath):
    lines = []
    if os.path.isfile("test/" + filePath):
        try:
            with open("test/" + filePath) as file:
                lines = [line.rstrip() for line in file]
            print("File ditemukan! Melakukan parsing...")
        except IOError as e:
            print("File tidak bisa dibuka.")
            exit(0)
    else:
        print('{} :File tidak ditemukan.'.format(filePath))
        exit(0)
    return lines

def parseFile(lines):
    buff_size = lines[0]
    matrix_size = lines[1]
    matrix_height = int(matrix_size.split()[1])
    data_matrix = lines[2:2+matrix_height]
    matrix_token = matrix.readMatrix(data_matrix)
    num_seq = int(lines[matrix_height+2])
    sequences = {}
    for i in range(0, 2*num_seq, 2):
        sequences[lines[matrix_height+3+i]] = int(lines[matrix_height+4+i])
    
    parsedLines = {
        "buffer size"           : buff_size,
        "matrix size"           : matrix_size,
        "matrix of token"       : matrix_token,
        "number of sequence"    : num_seq,
        "sequences"             : sequences
    }
    print("File berhasil di-parse!")
    return parsedLines

def simpan_solusi(score, exe_time, best_steps):
    dt = datetime.datetime.now().strftime("%d-%m-%y")
    parent_dir = "test/save_file/"
    dir = os.path.join(parent_dir, dt)
    try:
        os.mkdir(dir)
        print(f"Directory {dt} telah dibuat. Menyimpan...")
    except FileExistsError:
        print(f"Directory {dt} sudah ada. Menyimpan...")
    time.sleep(0.8)
    file_name = input("Masukkan nama file: ")
    path = os.path.join(dir, file_name)
    if os.path.exists(path):
        print(f"File {file_name} sudah ada. Overwrite otomatis...")
    else:
        print(f"Membuat file {file_name}...")
    time.sleep(0.8)
    f = open(path, "w")
    f.write(f"{score}\n")
    for step in best_steps:
        f.write(f"{step[0]+1} {step[1]+1}\n")
    f.write(f"{exe_time} ms\n")
    f.close()
    print("Selesai menyimpan")
    time.sleep(0.5)

if __name__ == "__main__":
    lines = readFile("test1.txt")
    parsed = parseFile(lines)
    print(parsed)