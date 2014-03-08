#include <tuple>

//
// Convert a binary tree into a doubly linked list.

struct Node {
    Node *left;
    Node *right;
};

//template <typename... Types> using tuple = std::tuple<Types...>;
using namespace std;

tuple<Node*,Node*> convertToList(Node *root)
{
    if (!root) {
        return tuple<Node*,Node*>(nullptr, nullptr);
    }

    // Convert children
    auto leftList = convertToList(root->left);
    auto rightList = convertToList(root->right);

    // staple left list to root
    if (root->left) {
        get<1>(leftList)->right = root;
        root->left = get<1>(leftList);
    } 
    // Staple right list to root
    if (root->right) {
        get<0>(rightList)->left = root;
        root->right = get<0>(rightList);
    }

    // return the first and last nodes in the chain
    tuple<Node*,Node*> ret {root, root};
    if (root->left) {
        get<0>(ret) = get<0>(leftList); 
    }
    if (root->right) {
        get<1>(ret) = get<1>(rightList);
    }
    return ret;
}



int main()
{
    return 0;
}
