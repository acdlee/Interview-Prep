#include <iostream>
#include <string>

using namespace std;

#define ALPHA_SIZE 26	//dictionary size
#define CHAR_OFFSET 97 	//only handle lowercase letters
#define DEBUG 0			//debug tool

//class representation for a trie data structure
class Trie {
public:
	Trie *characters[ALPHA_SIZE];
	bool isLeaf;

	//Constructor
	Trie() {
		this->isLeaf = false;
		for (int i = 0; i < ALPHA_SIZE; i++) {
			this->characters[i] = nullptr;
		}
	}

	void insert(string);
	bool deletion(Trie*&, string);
	bool search(string);
	bool haveChildren(Trie const*);

};

/*
* This function iteratively searches for the consecutive
* letters of the input parameter string key.
* For the string key to be considered "in" the trie,
* the final node corresponding to the last letter in string key
* must be a leaf node. 
*
* Returns true if the string key is in the trie.
*/
bool Trie::search(string key) {
	if (this == nullptr) return false;
	Trie* curr = this;
	
	for (auto character : key) {
		curr = curr->characters[character];
		if (curr == nullptr) {
			return false;
		}
	}

	return curr->isLeaf;
}

bool Trie::deletion(Trie*& curr, string key) {

}