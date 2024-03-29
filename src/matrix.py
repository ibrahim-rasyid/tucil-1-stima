import time

def displayMatrix(matrix):
    print("Matriks: ")
    time.sleep(1)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
        time.sleep(0.3)

def displaySequences(sequences):
    print("Sekuens beserta rewardnya: ")
    time.sleep(1)
    for sequence in sequences:
        print(f"{sequence}\n{sequences[sequence]}")
        time.sleep(0.3)

def displayResult(matrix, max_score, exe_time, best_steps):
    print(f"Skor maksimal: {max_score}")
    time.sleep(0.3)
    print("Urutan token:")
    for step in best_steps:
        print(f"{matrix[step[0]][step[1]]}", end=" ")
    print()
    time.sleep(0.3)
    print("Token berada pada koordinat berikut:")
    for step in best_steps:
        print(f"{step[1]+1} {step[0]+1}")
    time.sleep(0.3)
    print(f"Waktu eksekusi: {exe_time} ms")


def readMatrix(data_matrix):
    m = []
    for data in data_matrix:
        m.append(data.split())
    return m

if __name__ == "__main__":
    m = [['E9', 'BD', '55', 'E9', '55', 'E9'], 
         ['1C', 'E9', 'BD', '55', '7A', '1C'], 
         ['7A', 'BD', '7A', 'BD', '1C', '7A'], 
         ['7A', 'E9', '1C', 'BD', '1C', '1C'], 
         ['55', 'E9', '7A', 'BD', '1C', '55'], 
         ['1C', '1C', 'BD', 'BD', '55', 'BD']]
    displayMatrix(m)
    seq = {'1C E9 BD E9 ': 40, 
           '55 1C BD ': 5, 
           '7A E9 7A ': 25
           }
    displaySequences(seq)
