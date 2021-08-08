#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

bool isAnagram(string s1, string s2) {
	//size checks
	if (s1.length() != s2.length()) return false;

	//use a map to keep track of char counts
	unordered_map<char, int> umap;
	int N = s1.length(), M = s2.length();

	for (int i = 0; i < N; i++) {
		umap[s1[i]] 
	}

}

int main() {
	string s1 = "hello";
	string s2 = "leloh";

	cout << isAnagram(s1, s2) << endl;

	return 0;
}