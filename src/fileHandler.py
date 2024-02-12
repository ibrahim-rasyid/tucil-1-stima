import os
import protocol, matrix
import datetime

def readFile(filePath):
    lines = []
    if os.path.isfile("test/" + filePath):
        try:
            with open("test/" + filePath) as file:
                lines = [line.rstrip() for line in file]
        except IOError as e:
            print("File could not be opened.")
            exit(0)
    else:
        print('{} :File was not found in the specified path.'.format(filePath))
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
    return parsedLines

def simpan_solusi(solusi):
    dt = datetime.datetime.now().strftime("%d-%m-%y")
    parent_dir = "test/save_file/"
    dir = os.path.join(parent_dir, dt)
    try:
        os.mkdir(dir)
        print(f"Created {dt} directory. Saving...")
    except FileExistsError:
        print(f"Directory {dt} already exists. Saving...")
    file_name = input("Enter file name: ")
    path = os.path.join(dir, file_name)
    if os.path.exists(path):
        print(f"File {file_name} already exists. Automatically overwrite...")
    else:
        print(f"Creating file {file_name}...")
    f = open(path, "w")
    for elmt in solusi:
        f.write(f"{elmt}\n")

if __name__ == "__main__":
    lines = readFile("test1.txt")
    parsed = parseFile(lines)
    print(parsed)