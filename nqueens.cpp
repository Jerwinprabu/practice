#include <vector>
#include <algorithm>
#include <unordered_set>
#include <iostream>

int main(int argc, char *argv[]) 
{
    using namespace std;
    using set = unordered_set<int>;
    using vec = vector<int>;
    const int n = 8;
    int i = 0;
    vec cols(n); 
    generate(begin(cols), end(cols), [&i](){ return i++; });
    do { 
        int i = 0, j = 0;
        vec t1(cols), t2(cols);
        for_each(begin(t1), end(t1), [&j](int &t){ t = t - j; j++; });
        for_each(begin(t2), end(t2), [&i](int &t){ t = t + i; i++; });
        if (set(begin(t1), end(t1)).size() == n && set(begin(t2), end(t2)).size() == n) {
            for_each(begin(cols), end(cols), [](int &n) { cout << n << " "; });
            cout << endl;
        }
    } while (next_permutation(begin(cols), end(cols)));
    return 0;
}
