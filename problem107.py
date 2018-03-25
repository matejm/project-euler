from queue import PriorityQueue 

with open('network') as f:
	g = f.readlines()

g = [[(int(j), i) for i, j in enumerate(k.rstrip().split(',')) if j != '-'] for k in g]

added = [False for i in range(len(g))]

pq = PriorityQueue()

added[0] = True

for l in g[0]:
	pq.put(l)

s = 0
while not pq.empty():
	distance, vertex = pq.get()
	
	if not added[vertex]:
		added[vertex] = True
		s += distance
		for l in g[vertex]:
			if not added[l[1]]:
				pq.put(l)

total = sum(sum(i for i, j in k) for k in g)
print(total - s)