#ifndef matrix_cpp
#define matrix_cpp

#include <matrix.hpp>
#include <iostream>
#include <vector>
using namespace std;

Matrix::Matrix(const Matrix &m) {
    for (int i=0; i<m.row_len(); i++) {

    }
}

int Matrix::row_len() const {
    return content.size();
}

int Matrix::col_len() const {
    return content[0].size();
}

void Matrix::setElmt(int i, int j, string val) {
    content[i][j] = val;
}

string Matrix::getElmt(int i, int j) {
    return content[i][j];
}

void Matrix::displayMatrix() {
    for (int i=0; i<content.size(); i++) {
        for (int j=0; j<content[i].size(); j++) {
            std::cout << content[i][j] << " ";
        }
        std::cout << endl;
    }
}

Matrix Matrix::getFromTxt(std::string filename, char delim) {
    Matrix m;

}


int main() {
    Matrix m1();
}

#endif