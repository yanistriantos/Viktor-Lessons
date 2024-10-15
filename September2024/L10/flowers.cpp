#include <iostream>
#include <vector>

using namespace std;

// 3 2 1 2 -1

// 0

// 1

// 2

// -1

// 1 1 1 1 -1
// 0
// 1
// 2
// 3
// -1

int main() {
    // // Read integers until -1 is encountered
    // int a = 10;
    // while (a > 5) {
    //     cout << "neshto" << endl;
    //     // a = a - 1;
    //     a--;
    // }

    // ...
    cout << "neshto" << endl;
    
    vector<int> numbers;
    int num;
    // and == &&
    // or == ||
    while (cin >> num && num != -1) {
        numbers.push_back(num);
    }
}
