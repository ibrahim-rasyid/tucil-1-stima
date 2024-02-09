#ifndef matrix_hpp
#define matrix_hpp

#include <iostream>
#include <vector>
using namespace std;

class Matrix {
    public:
        std::vector<std::vector<string>> content;
        Matrix() {}
        Matrix(const Matrix &);

        int row_len() const;

        int col_len() const;

        void setElmt(int, int, std::string) {}

        string getElmt(int, int) {}

        void displayMatrix() {}

        Matrix getFromTxt(std::string, char) {}
};

#endif