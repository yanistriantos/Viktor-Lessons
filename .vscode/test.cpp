#include <iostream>
#include <string>

using namespace std;

// Клас за куче
class Dog {
public:
    virtual void Print() {
        cout << "Кучето е просто куче." << endl;
    }
};

// Наследен клас Лабрадор от класа за куче
class Labrador : public Dog {
public:
    void Print() override {
        cout << "Това е Лабрадор." << endl;
    }
};

int main() {
    Dog dog;
    Labrador labrador;

    // Извикване на метода Print() за обектите от двете класа
    dog.Print();
    labrador.Print();

    return 0;
}