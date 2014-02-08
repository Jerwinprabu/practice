#include <chrono>
#include <string>
#include <iostream>
#include <cstdint>
#Incl:w
:w

int main(int argc, char *argv[])
{
    using namespace std;

    chrono::time_point<chrono::high_resolution_clock> start, end;
    start = chrono::high_resolution_clock::now();
    end = chrono::high_resolution_clock::now();

    chrono::duration<double> elapsed = end - start;
    cout << chrono::high_resolution_clock::period().num << " " << chrono::high_resolution_clock::period().den  << endl;
    cout << elapsed.count() << endl;    


    return 0;
}
