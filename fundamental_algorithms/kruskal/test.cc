#include <iostream>
#include <vector>

using namespace std;

//struct edge is a representation of an edge in a graph
struct edge {
	int v1, v2;	//verticies
	long weight; //edge weight
};

bool edgeSorter(edge lhs , edge rhs) {
	return (lhs.weight < rhs.weight);
}

int main() {

	vector<edge> E; 
	int n = 6;
	for (int i = 0; i < n; ++i) {
		edge new_edge;
		new_edge.weight = n - i;
		new_edge.v1 = 1;
		new_edge.v2 = 2;
		E.push_back(new_edge);
	}

	// for (edge e : E) {
	// 	cout << e.weight << endl;
	// }

	sort(E.begin(), E.end(), edgeSorter);

	for (edge e : E) {
		cout << e.weight << endl;
	}


	return 0;
}