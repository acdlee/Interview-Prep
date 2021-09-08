//SPOJ username: quietroom
//Status: https://www.spoj.com/status/INVENT,quietroom/
//Compiler: C++14 (clang 8.0)

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

//struct edge is a representation of an edge in a graph
struct edge {
	int v1, v2;	//verticies
	long weight; //edge weight
};

//function  declarations
long findConnectWeight(vector<edge>, int);
void printEdges(vector<edge>);
int union_sets(vector<int> &, vector<int> &, int, int);
int find_PC(vector<int> &, int);
void printVect(vector<int> );
bool edgeSorter(edge, edge);

int main() {
	//let's first handle input
	int n;	//number of test cases
	cin >> n;

	//process each test case
	for (int i = 0; i < n; i++) {
		//create a vector of edges
		vector<edge> E;

		//get the number of nodes
		int nodes;
		cin >> nodes;

		//process each line as: v1 v2 w
		//Note: MST's have nodes-1 edges
		for (int j = 0; j < nodes - 1; j++) {
			edge new_edge;
			cin >> new_edge.v1;
			cin >> new_edge.v2;
			cin >> new_edge.weight;

			//add the edge to E
			E.push_back(new_edge);
		}
		//sort the MST edges
		sort(E.begin(), E.end(), edgeSorter);

		//find the min weight of the connected graph
		cout << findConnectWeight(E, nodes) << endl;
	}

	return 0;
}

//function that finds, given an edge struct vector
//of edges and weights of an MST, the minimum weight
//of the connected graph of that MST.
long findConnectWeight(vector<edge> E, int n) {
	//let's first create our union_find data structure
	vector<int> union_find(n);
	//let's also create a tree-size array
	vector<int> tree_size(n);	//if our forest is (with 1 root) 1-2-3    4
								//tree_size: [_, 2, _, 0] where _ can be 0 or 1 depending on order added

	long sum = 0;
	//let's loop through each edge
	for (edge e : E) {
		
		//find the set identifier for both verticies
		int set_v1 = find_PC(union_find, e.v1);
		int set_v2 = find_PC(union_find, e.v2);

		//let's get their tree sizes before we union
		int set_v1_size = tree_size[set_v1 - 1] + 1; //+1 for set indentifier
		int set_v2_size = tree_size[set_v2 - 1] + 1; 

		//union the verticies
		int set_union = union_sets(union_find, tree_size, set_v1, set_v2);

		//add the weight of the edge to the sum
		sum += e.weight;

		//add weights for connected edges
		int size = tree_size[set_union - 1] + 1;	//+1 to count set identifier

		//fully connected graph will have n(n-1)/2 edges (n = #verticies)
		int total_edges = (size * (size - 1)) / 2;

		//we have to know the sizes of the two sets to see
		//what they've already contributed to the sum
		total_edges -= (set_v1_size * (set_v1_size - 1)) / 2;
		total_edges -= (set_v2_size * (set_v2_size - 1)) / 2;

		//the new edges will contribute total_edges - 1 to sum.
		// - 1 because we've already added the MST edge
		sum += (long) (total_edges - 1) * (e.weight + 1);

	}

	return sum;
}

//custom sortere for sorting edges. an edge is "greater" if
//its edge weight is greater
//
//returns true if lhs has a greater edge weight
//than rhs
bool edgeSorter(edge lhs , edge rhs) {
	return (lhs.weight < rhs.weight);
}

//unions two sets and increases tree size for the
//returned indentifier. ignores rank
//
//returns the new set identifier for the unioned tree
int union_sets(vector<int>& union_find, vector<int>& tree_size, int set_a, int set_b) {
	//ingore rank for now
	union_find[set_a - 1] = set_b;
	//+= number of nodes connected to set_a + 1 for set_a identifier
	tree_size[set_b - 1] += tree_size[set_a - 1] + 1;
	//set a note that this node is a tree
	return set_b;
}

//find operation implemented with path compression (PC)
//returns the set identifier in union_find associated 
//with vertex x
//
//returns the associated node number of the parent.
int find_PC(vector<int>& union_find, int x) {
	if (!union_find[x-1]) return x;
	return union_find[x-1] = find_PC(union_find, union_find[x-1]);
}


//DEBUGGING TOOLS
void printVect(vector<int> A) {
	cout << "arrays: ";
	for (int i : A) {
		cout << i << ' ';
	}
	cout << endl;
}

//helper function just to print edges in a given
//edge vector
void printEdges(vector<edge> E) {
	cout << endl << "Your edges: " << endl;

	for (edge e: E) {
		cout << e.v1 << ' ';
		cout << e.v2 << ' ';
		cout << e.weight << endl;
	}

	return;
}