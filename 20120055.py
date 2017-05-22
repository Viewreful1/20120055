import Queue

def dfs(g, V) :
	visited = []
	s = []
	s.append(V)
	while(len(s)) :
		v = s.pop()
		if v not in visited :
			print v,
			visited.append(v)
			for neighbor in g[v][::-1] :
				s.append(neighbor)

def bfs(g, V) :
	visited = []
	q = Queue.Queue()
	print V,
	visited.append(V)
	q.put(V)
	while(q.qsize()) :
		v = q.get()
		for neighbor in g[v] :
			if neighbor not in visited :
				q.put(neighbor)
				visited.append(neighbor)
				print neighbor,

if __name__ == '__main__' :
	N, M, V = map(int, raw_input().split())
	g = {}
	for _ in range(M) :
		s, e = map(int, raw_input().strip().split())
		if s not in g :
			g[s] = []
		if e not in g :
			g[e] = []
		g[s].append(e)
		g[e].append(s)
		g[s].sort()
		g[e].sort()
	dfs(g, V)
	visited = []
	print ''
	bfs(g, V)