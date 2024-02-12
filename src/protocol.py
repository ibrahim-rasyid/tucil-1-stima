import matrix

def getSequences(sequences):
    seq_num = int(input("Number of sequences: "))
    for i in range(seq_num):
        seq = input("Sequence: ")
        reward = int(input("Sequence Reward: "))
        sequences[seq] = reward

def protocol(matrix, buff_size, vert, seq, rc, prev_idx, sequences, steps):
    if buff_size == 0:
        score = 0
        process_seq = ""
        for elmt in seq:
            process_seq += elmt+" "
        for seq_elmt in sequences:
            if seq_elmt in process_seq:
                score += sequences[seq_elmt]
        return score
    
    else:
        max_score = 0
        if vert:
            for i in range(0, len(matrix)):
                if prev_idx != [i, rc]:
                    seq.append(matrix[i][rc])
                    score = protocol(matrix, buff_size-1, not vert, seq, i, [i, rc], sequences, steps)
                    seq.pop()
                    if score > max_score:
                        max_score = score

        else:
            for i in range(0, len(matrix[rc])):
                if prev_idx != [rc, i]:
                    seq.append(matrix[rc][i])
                    score = protocol(matrix, buff_size-1, not vert, seq, i, [rc, i], sequences, steps)
                    seq.pop()
                    if score > max_score:
                        max_score = score
                        
        return max_score

if __name__ == "__main__":
    m = matrix.getMatrix(3, 3)
    buff = 3
    sequences = {}
    getSequences(sequences)
    score = protocol(m, buff, False, [], 0, [-1, -1], sequences, [])
    print(score)