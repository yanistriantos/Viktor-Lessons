#include <iostream>
#include <vector>
#include <limits>

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
    vector<int> flowers;
    int num;
    // and == &&
    // or == ||
    while (cin >> num && num != -1) {
        flowers.push_back(num);
    }
    
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    
    vector<int> indexes = {};
    int number;
    while (cin >> number && number != -1) {
        indexes.push_back(number);
    }
    
    // "water the flowers"
    for (unsigned int index : indexes) {
        if (index < flowers.size()  &&  flowers[index] != 0)
            flowers[index]--;
    }
    
    for (int flower : flowers) {
        cout << flower << " ";
    }
    cout << endl;
    
    int a = 10
    if (a > 20) {
        cout << "bigger than 20" << endl;
    } else if (a < 20) {
        cout << "smaller than 20" << end;
    }
    
    // break falltrough
    switch (a) {
        case a > 20:
            cout << "bigger than 20" << endl;
            break;
        case a < 20:
            cout << "bigger than 20" << endl;
            break;
        default:
            cout << "default case hitted" << endl;
            break;
    }
}
