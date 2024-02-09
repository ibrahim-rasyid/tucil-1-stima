#include <iostream>
#include <matrix.hpp>
using namespace std;

int jumlah(int a, int b) {
    return a+b;
}

int main () {
    int a, b, c;
    cin >> a;
    cin >> b;
    c = jumlah(a, b);
    cout << c;
    return 0;
}