#include <iostream>
using namespace std;

// Клас А
class A {
public:
    A() {
        cout << "Конструкторът на класа A" << endl;
    }
};

// Клас Б
class B {
public:
    B() {
        cout << "Конструкторът на класа B" << endl;
    }
};

// Наследен клас В от А
class V : public A {
    B b; // Обект от клас Б в клас В
};

int main() {
    V v; // Създаване на обект от клас В

    return 0;
}