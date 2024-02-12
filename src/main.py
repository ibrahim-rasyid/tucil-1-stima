from fileHandler import readFile, parseFile, simpan_solusi
from protocol import protocol
import time, datetime
import os

def opening():
    print("WELCOME")

def initiate():
    print("""Txt atau generate?
(1 untuk txt, 2 untuk generate)""")
    opsi = int(input())
    while opsi != 1 and opsi != 2:
        print("Masukan salah! Ulangi")
        opsi = int(input())
    return opsi

def playFile():
    filePath = input("Masukkan file path txt (pastikan format benar): ")
    lines = readFile(filePath)
    parsed = parseFile(lines)
    matrix_token = parsed["matrix of token"]
    buff_size = int(parsed["buffer size"])
    sequences = parsed["sequences"]
    start_time = time.time()
    max_score = protocol(matrix_token, buff_size, False, [], 0, [-1, -1], sequences, [])
    end_time = time.time()
    exe_time = end_time-start_time
    return max_score, exe_time

def playRandom():
    unique_token = int(input("Banyaknya token unik: "))
    

def outro(solusi):
    simpan = input("Apakah ingin simpan? (Y/n): ")
    while simpan.lower() != "y" and simpan.lower() != "n":
        simpan = input("Masukan tidak benar! (Y/n): ")
    if simpan.lower() == "y":
        simpan_solusi(solusi)

def exitGame():
    print("Thanks for using!")

def main():
    opening()
    opsi = initiate()
    if opsi == 1:
        solusi, waktu = playFile()
    elif opsi == 2:
        pass
    print(solusi)
    print(waktu)
    outro(solusi)
    exitGame()

if __name__ == "__main__":
    main()