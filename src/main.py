from fileHandler import readFile, parseFile, simpan_solusi
from protocol import protocol, generateRandom
from matrix import displaySequences, displayMatrix, displayResult
import time, datetime
import os

def opening():
    print("""
 _______   _______   ________   ______    ______   __    __        _______   _______    ______   ________  ______    ______    ______   __       
/       \ /       \ /        | /      \  /      \ /  |  /  |      /       \ /       \  /      \ /        |/      \  /      \  /      \ /  |      
$$$$$$$  |$$$$$$$  |$$$$$$$$/ /$$$$$$  |/$$$$$$  |$$ |  $$ |      $$$$$$$  |$$$$$$$  |/$$$$$$  |$$$$$$$$//$$$$$$  |/$$$$$$  |/$$$$$$  |$$ |      
$$ |__$$ |$$ |__$$ |$$ |__    $$ |__$$ |$$ |  $$/ $$ |__$$ |      $$ |__$$ |$$ |__$$ |$$ |  $$ |   $$ |  $$ |  $$ |$$ |  $$/ $$ |  $$ |$$ |      
$$    $$< $$    $$< $$    |   $$    $$ |$$ |      $$    $$ |      $$    $$/ $$    $$< $$ |  $$ |   $$ |  $$ |  $$ |$$ |      $$ |  $$ |$$ |      
$$$$$$$  |$$$$$$$  |$$$$$/    $$$$$$$$ |$$ |   __ $$$$$$$$ |      $$$$$$$/  $$$$$$$  |$$ |  $$ |   $$ |  $$ |  $$ |$$ |   __ $$ |  $$ |$$ |      
$$ |__$$ |$$ |  $$ |$$ |_____ $$ |  $$ |$$ \__/  |$$ |  $$ |      $$ |      $$ |  $$ |$$ \__$$ |   $$ |  $$ \__$$ |$$ \__/  |$$ \__$$ |$$ |_____ 
$$    $$/ $$ |  $$ |$$       |$$ |  $$ |$$    $$/ $$ |  $$ |      $$ |      $$ |  $$ |$$    $$/    $$ |  $$    $$/ $$    $$/ $$    $$/ $$       |
$$$$$$$/  $$/   $$/ $$$$$$$$/ $$/   $$/  $$$$$$/  $$/   $$/       $$/       $$/   $$/  $$$$$$/     $$/    $$$$$$/   $$$$$$/   $$$$$$/  $$$$$$$$/ 
          """)
    time.sleep(0.7)
    print("Selamat datang di program Breach Protocol. Selamat bermain!")

def initiate():
    print("""Apakah ingin import dari file .txt atau generate random?
(1 untuk import, 2 untuk generate)""")
    opsi = int(input())
    while opsi != 1 and opsi != 2:
        print("Masukan salah! Ulangi")
        opsi = int(input())
    return opsi

def play(opsi):
    if opsi == 1:
        matrix, buff_size, sequences = playFile()
    else:
        matrix, buff_size, sequences = playRandom()
    print("Melakukan pencarian...")
    time.sleep(1)
    start_time = time.time()
    max_score, best_steps = protocol(matrix, buff_size, False, [], 0, [-1, -1], sequences, [])
    end_time = time.time()
    print("Pencarian selesai!")
    time.sleep(0.5)
    exe_time = (end_time-start_time)*1000 # dalam ms
    displayResult(matrix, max_score, exe_time, best_steps)
    return max_score, exe_time, best_steps

def playFile():
    print("Anda memilih import dari file .txt")
    time.sleep(1)
    filePath = input("Masukkan file path txt (pastikan format benar): ")
    time.sleep(0.3)
    lines = readFile(filePath)
    time.sleep(0.5)
    parsed = parseFile(lines)
    time.sleep(0.7)
    matrix_token = parsed["matrix of token"]
    buff_size = int(parsed["buffer size"])
    sequences = parsed["sequences"]
    time.sleep(0.5)
    displayMatrix(matrix_token)
    time.sleep(0.7)
    displaySequences(sequences)
    time.sleep(0.7)

    return matrix_token, buff_size, sequences

def playRandom():
    print("Anda memilih generate random")
    time.sleep(0.3)
    unique_token = int(input("Banyaknya token unik: "))
    tokens = input("Token-token unik: ")
    buff_size = int(input("Ukuran buffer: "))
    matrix_size = input("Ukuran matriks: ")
    num_seq = int(input("Banyaknya sekuens: "))
    max_seq_len = int(input("Ukuran maksimal sekuens: "))
    matrix, sequences = generateRandom(unique_token, tokens, matrix_size, num_seq, max_seq_len)
    time.sleep(0.5)
    displayMatrix(matrix)
    time.sleep(0.7)
    displaySequences(sequences)
    time.sleep(0.7)
    return matrix, buff_size, sequences

def outro(score, exe_time, best_steps):
    simpan = input("Apakah ingin simpan? (Y/n): ")
    while simpan.lower() != "y" and simpan.lower() != "n":
        simpan = input("Masukan tidak benar! (Y/n): ")
    if simpan.lower() == "y":
        simpan_solusi(score, exe_time, best_steps)

def exitGame():
    print("Thanks for using!")
    print("""
 _______  __   __  _______  __    _  ___   _    __   __  _______  __   __    ___   ____   
|       ||  | |  ||   _   ||  |  | ||   | | |  |  | |  ||       ||  | |  |  |   | |    |  
|_     _||  |_|  ||  |_|  ||   |_| ||   |_| |  |  |_|  ||   _   ||  | |  |  |___| |_    | 
  |   |  |       ||       ||       ||      _|  |       ||  | |  ||  |_|  |   ___    |   | 
  |   |  |       ||       ||  _    ||     |_   |_     _||  |_|  ||       |  |   |   |   | 
  |   |  |   _   ||   _   || | |   ||    _  |    |   |  |       ||       |  |___|  _|   | 
  |___|  |__| |__||__| |__||_|  |__||___| |_|    |___|  |_______||_______|        |____|  
          """)
    time.sleep(0.5)

def main():
    opening()
    time.sleep(1)
    opsi = initiate()
    score, waktu, best_steps = play(opsi)
    outro(score, waktu, best_steps)
    exitGame()

if __name__ == "__main__":
    main()