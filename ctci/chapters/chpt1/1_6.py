#O(N^2) time and constant space
def rotateMatrix(M):
	if not M: return False
	if len(M) != len(M[0]): return False
	N = len(M)

	for layer in range(N//2):	#layering

		for i in range(layer, N-layer-1):

			#temp <- top
			temp = M[layer][i]

			#top <- L
			M[layer][i] = M[N-i-1][layer]

			#L <- B
			M[N-i-1][layer] = M[N-layer-1][N-i-1]

			#B <- R
			M[N-layer-1][N-i-1] = M[i][N-layer-1]

			#R <- temp (T)
			M[i][N-layer-1] = temp

	return M

M = [ [1,2,3],[4,5,6],[7,8,9]]
M = [ [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(rotateMatrix(M))