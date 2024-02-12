import matrix
import random
import time

def getSequences(sequences):
    seq_num = int(input("Number of sequences: "))
    for i in range(seq_num):
        seq = input("Sequence: ")
        reward = int(input("Sequence Reward: "))
        sequences[seq] = reward

def generateRandom(unique_token, tokens, matrix_size, num_seq, max_seq_len):
    tokens = tokens.split()
    print("Membuat matriks...")
    time.sleep(1)
    m = []
    matrix_size = matrix_size.split()
    matrix_height = int(matrix_size[1])
    matrix_width = int(matrix_size[0])
    for i in range(matrix_height):
        n = []
        for j in range(matrix_width):
            token_num = random.randint(0, unique_token-1)
            n.append(tokens[token_num])
        m.append(n)
    print("Matriks berhasil dibuat!")
    time.sleep(0.5)
    print("Membuat sekuens beserta rewardnya...")
    time.sleep(1)
    sequences = {}
    for i in range(num_seq):
        seq_len = random.randint(2, max_seq_len)
        seq = ""
        for i in range(seq_len):
            seq_num = random.randint(0, unique_token-1)
            seq += tokens[seq_num]+" "
        seq_reward = random.randint(1, 10)
        seq_reward *= 5
        sequences[seq] = seq_reward
    print("Sekuens berhasil dibuat!")
    time.sleep(0.5)

    return m, sequences

def protocol(matrix, buff_size, vert, seq, rc, prev_idx, sequences, steps):
    if buff_size == 0:
        score = 0
        process_seq = ""
        for elmt in seq:
            process_seq += elmt+" "
        for seq_elmt in sequences:
            if seq_elmt in process_seq:
                score += sequences[seq_elmt]
        return score, steps
    
    else:
        max_score = 0
        best_steps = []
        if vert:
            for i in range(0, len(matrix)):
                if prev_idx != [i, rc]:
                    seq.append(matrix[i][rc])
                    score, step = protocol(matrix, buff_size-1, not vert, seq, i, [i, rc], sequences, [*steps, (i, rc)])
                    seq.pop()
                    if score > max_score:
                        max_score = score
                        best_steps = step


        else:
            for i in range(0, len(matrix[rc])):
                if prev_idx != [rc, i]:
                    seq.append(matrix[rc][i])
                    score, step = protocol(matrix, buff_size-1, not vert, seq, i, [rc, i], sequences, [*steps, (rc, i)])
                    seq.pop()
                    if score > max_score:
                        max_score = score
                        best_steps = step
                        
        return max_score, best_steps

if __name__ == "__main__":
    m = []
    buff = 3
    sequences = {}
    m, sequences = generateRandom(5, "BD 1C 7A 55 E9", "6 6", 3, 4)
    print(m)
    print(sequences)
    score, best_steps = protocol(m, buff, False, [], 0, [-1, -1], sequences, [])
    print(score)
    print(type(best_steps[0][0]))