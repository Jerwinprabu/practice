#include <vector>
#include <iterator>
#include <algorithm>
#include <iostream>
#include <cassert>
#include <deque>

void reverse(std::vector<char> &s) 
{
    if (s.size() == 0 || s.size() == 1) return;
    std::reverse(begin(s), --end(s));
}

void reverse2(std::vector<char> &s)
{
    std::vector<char>::iterator head, tail;

    head = begin(s);
    tail = ----end(s);
    
    for (int i = 0; i < (s.size()-1) / 2; i++) {
        std::swap(*head, *tail);
        ++head;
        --tail;
    }
}

void print(std::vector<char> &s)
{
    for (auto i = begin(s); i != end(s); ++i) {
        std::cout << *i;
    }
    std::cout << std::endl;
}


struct StringTree {
    char *contents;
    StringTree *leftChild, *rightChild;
};


void printStringTree(StringTree *root, std::ostream &out) 
{
    if (!root) {
        return;
    }
    printStringTree(root->leftChild, out); 
    out << root->contents;
    printStringTree(root->rightChild, out);
}

void appendStringTree(StringTree *&root, char *str)
{
    StringTree *addNode = new StringTree{str, nullptr, nullptr};
    if (!root) {
        root = addNode;
    }
    StringTree *curNode = root;
    while (curNode->rightChild) {
        curNode = curNode->rightChild;
    }
    assert(curNode->rightChild);
    curNode->rightChild = addNode;
}

void freeStringTree(StringTree *root)
{
    if (!root) {
        return;
    }
    std::deque<StringTree*> q = {root};
    while (q.size()) {
        StringTree *cur = q.front();
        q.pop_front();
        if (cur->leftChild) {
            q.push_back(cur->leftChild);
        }
        if (cur->rightChild) {
            q.push_back(cur->rightChild);
        }
        delete cur;
    }
}

int main()
{

    const char cstr[] = "fooood";
    std::vector<char> vstr;
    for (char i : cstr) {
        vstr.push_back(i); 
    }

    print(vstr);
    reverse(vstr); 
    print(vstr);
    reverse2(vstr);
    print(vstr);

     
    return 0;    
}
