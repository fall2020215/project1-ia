import heapq
customers = []
heapq.heappush(customers, (9, "Stacy"))
heapq.heappush(customers, (6, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))

#print(heapq.heappop(customers))


#Will print names in the order: Riya, Harry, Charles, Stacy.
print(customers)
customers.remove((6, "Harry"))
#heapq.heappush(customers, (5, "Riya"))

print(customers)
heapq.heappush(customers, (2, "Harry"))

print(heapq.heappop(customers))

print(customers)

print(heapq.heappop(customers))

print(customers)

heapq.heappush(customers, (3, "thinh"))

print(customers)

print(heapq.heappop(customers))

print(customers)

print(heapq.heappop(customers))

print(customers)

