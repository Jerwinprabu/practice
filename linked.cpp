#include <chrono>
#include <string>
#include <iostream>
#include <cstdint>

struct ListNode {
    ListNode *next;
    uint64_t data; 
};

ListNode *listA, *listB;

int main(int argc, char *argv[])
{
    const long long iterations = 100000000;
    using namespace std;
    for (long long i = 0; i < iterations; i++) {
        ListNode *node = new ListNode{listA, 0xdeadbeef};
        listA = node;
    }

    chrono::time_point<chrono::high_resolution_clock> start, end;
    start = chrono::high_resolution_clock::now();
    while (listA) {
        ListNode *node = listA;
        listA = node->next;
        node->next = listB;
        listB = node;
    }
    end = chrono::high_resolution_clock::now();

    chrono::duration<double> elapsed = end - start;
    cout << chrono::high_resolution_clock::period().num << " " << chrono::high_resolution_clock::period().den  << endl;
    cout << elapsed.count() << endl;    
    cout << elapsed.count() / iterations << endl;


    LitNode *foo;
    return 0;

    
}
