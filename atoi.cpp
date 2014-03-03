#include <string>
#include <iostream>

using namespace std;
int main(int argc, char *argv[])
{
    string s{"a"}; 
    int sign = 1;
    int sum = 0;
    for (int i = 0; i < s.size(); i++) {
        char c = s[i];
        if (i == 0) {
            if (c == '-') {
                sign = -1;
                continue;
            }
        }   
        if (c >= '0' and c <= '9') {
            sum = sum * 10 + int(c - '0');
        }
        else {
            break;
        } 
    }
    cout << sum * sign << endl;
    return sum * sign;
}
