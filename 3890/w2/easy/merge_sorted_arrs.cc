#include <iostream>

using namespace std;

int *mergeSortedArrs(int A[], int B[], int N, int M) {
	int result[N + M];
	int index = 0;

	int pointer_a = 0, pointer_b = 0;

	while (pointer_a < N && pointer_b < M) {
		if (A[pointer_a] < B[pointer_b]) {
			result[index] = A[pointer_a];
			pointer_a++;
		} else {
			result[index] = B[pointer_b];
			pointer_b++;
		}
		cout << result[index] << " ";
		index++;
	}

	//finish the left over elements
	if (pointer_a < N) {
		while(pointer_a < N) {
			result[index] = A[pointer_a];
			cout << result[index++]<< " ";
			pointer_a++;
		}
	} else {
		while(pointer_b < M) {
			result[index] = B[pointer_b];
			cout << result[index++]<< " ";
			pointer_b++;
		}
	}

	return result;
}

int main() {

	int A[5] = {-3, -1, 4, 5, 7};
	int B[4] = {-5, 0, 6, 12};
	int N = 5, M = 4;
	int *result = mergeSortedArrs(A, B, N, M);

	// cout << "Result: ";
	// for (int i = 0; i < N + M; i++) {
	// 	cout << result[i];
	// }

	cout << endl;

	return 0;
}