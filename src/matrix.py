
def getMatrix(m, n):
    mat = []
    for i in range(m):
        tokens = input().split()
        mat.append(tokens)
    return mat

def readMatrix(data_matrix):
    m = []
    for data in data_matrix:
        m.append(data.split())
    return m

if __name__ == "__main__":
    m = []
    getMatrix(m, 3, 3)
    print(m)