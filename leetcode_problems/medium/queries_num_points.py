#O(P*Q) time; O(Q) space
def countPoints(points, queries):
	answer = []

	if points and queries:	#empty check
		#loop through all pairs of queries and points
		for (xj, yj, rj) in queries:
			counter = 0					#counter for number of points in query j
			for (xi, yi) in points:
				#check that the ith point is within the jth query
				if (xi - xj)**2 + (yi - yj)**2 <= rj**2:		#euclidean distance
					counter += 1

			answer.append(counter)		#add the counter for jth query


	return answer



points = [[1,3],[3,3],[5,3],[2,2]]
queries = [[2,3,1],[4,3,1],[1,1,2]]


print(countPoints(points, queries))