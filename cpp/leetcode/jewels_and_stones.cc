#include <iostream>
#include <map>
#include <string>

using namespace std;

//declaration
int numJewelsInStones(string, string);

int main() {
	string jewels = "aA";
	string stones = "aAAbbbb";

	cout << numJewelsInStones(jewels, stones) << endl;

	return 0;
}


int numJewelsInStones(string jewels, string stones) {
	map<char, int> m;
	int count = 0;

	for (auto c : stones) {
		m[c]++;
	}

	//let's now count
	for (auto c : jewels) {
		if (m.count(c)) {
			count += m[c];
		}
	}

	return count;
}