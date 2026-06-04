#include <iostream>
using namespace std;

class Base {
public:
    Base() { cout << "Base Created\n"; }
    virtual ~Base() { cout << "Base Destroyed\n"; } 
};

class Derived : public Base {
public:
    Derived() { cout << "Derived Created\n"; }
    ~Derived() { cout << "Derived Destroyed\n"; }
};

int main() {
    Base* obj = new Derived();
    delete obj;
    return 0;
}
