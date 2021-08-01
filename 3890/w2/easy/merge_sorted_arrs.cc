#include <iostream>

/*
	O(N + M) space and time using the 
	two pointer technique.
*/


using namespace std;

//note: A is of size N + M
void mergeSortedArrs(int A[], int B[], int N, int M) {
	//2 pointer technique setup
	int index = M + N - 1, pointer_a = N - 1, pointer_b = M - 1;

	//iterate from back to front to make use of the
	//extra space in A
	while (pointer_a >= 0 && pointer_b >= 0) {
		if (A[pointer_a] > B[pointer_b]) {
			A[index] = A[pointer_a--];
		} else {
			A[index] = B[pointer_b--];
		}
		index--;
	}

	//finish the left over elements
	while (pointer_a >= 0) 
		A[index--] = A[pointer_a--];
	while(pointer_b >= 0) {
		A[index--] = B[pointer_b--];
	}
}

int main() {

	int A[9] = {-3, -1, 4, 5, 7};
	int B[4] = {-5, 0, 6, 12};
	int N = 5, M = 4;
	mergeSortedArrs(A, B, N, M);

	cout << "Result: ";
	for (int i = 0; i < N + M; i++) {
		cout << A[i] << " ";
	}

	cout << endl;

	return 0;
}