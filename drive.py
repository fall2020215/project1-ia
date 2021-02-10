import node as n
import heapq
import algorithm as a


######################### Part I: extract the input file into list_node, which is the same to an array 2D ###############
######################### BIGINNING PART I ######################################################

list_node = [] # Keep all nodes like an array 2D
size_maze = [] #keep the size of list_node (row and column)
hashtable_node = {} # key of hashtable_node is the name of node, and the value is the tuple of (row, column) in the array (list_node)
hashtable_heap = {} # key of hashtable_heap is the name of node, and the value is ....
current_heap = [] #current_heap is a list (array) of tuples that store all information about node_name, travel_distance, total_distance, and path
 
#extract all information from maza.txt into list_node
with open ("maze.txt") as file:
    size_maze = file.readline() 
    row = int(size_maze.split()[0])
    column = int(size_maze.split()[1])
    for i in range(1,row + 1):
        list_row_node  = file.readline().split()
        list_mid = []
        for j in range (1, column + 1):
            list_each_node = list_row_node[j-1].split('-')
            list_mid.append(n.Node(list_each_node[0],list_each_node[1],int(list_each_node[2]),int(list_each_node[3]),i-1,j-1))
        list_node.append(list_mid)

#example to connect data member of the node number 8 at row 0 and column 7. The list_node is the same to an array 2D
#print(list_node[1][0].get_name())
#print(list_node[1][0].get_direction())
#print(list_node[1][0].get_x())
#print(list_node[1][0].get_y())
#print(list_node[1][0].get_row())
#print(list_node[1][0].get_column())


#add all nodes from list_node to hashtable_node --> to look at quickly where a node is the list_node
# key of hashtable_node is the name of node, and the value is the tuple of (row, column) in the array (list_node)
for row in range (1, int(size_maze.split()[0]) + 1):
    for column in range (1, int(size_maze.split()[1]) + 1):
        name_node = list_node[row-1][column-1].get_name()
        hashtable_node[name_node] = (row-1, column-1)

#print(hashtable_node)
#print(len(hashtable_node))


#get position final_x and final_y of final node
final_row, final_column = hashtable_node['O']
final_x = list_node[final_row][final_column].get_x()
final_y = list_node[final_row][final_column].get_y()

################### FINISH PART I #############################################################


################### BEGINNING ---  A* Algorithm for shortest path #############################



#################################
#WE HAVE TO CHANGE THE FIRST NODE
##################################
first_name = 'B44'
first_neighbor = a.neighbor_nodes(first_name,hashtable_node, list_node)

row_first_node, column_first_node = hashtable_node[first_name]
first_node = list_node[row_first_node][column_first_node]



#################################
#CHANGE THE FIRST NODE
#################################

#innital for current_heap and hashtable_heap for first node:
#heapq.heappush(customers, (9, "Stacy"))
distance_straight = a.distance_straight_to_final_node(first_name,final_x,final_y,hashtable_node, list_node)
heapq.heappush(current_heap, (distance_straight, (first_name, 0, distance_straight, first_name)))
hashtable_heap[first_name] = (first_name, 0 , distance_straight, first_name)



#print(heapq.heappop(current_heap))
#print(hashtable_heap)
#print(heapq.heappop(current_heap)[1][0])
#print(heapq.heappop(current_heap)[0])

################### ENDING  --- A* Algorithm for shortest path ################################

#print(a.distance_straight_to_final_node('B16',final_x, final_y, hashtable_node, list_node))
#print(hashtable_node['B16'])
#print(a.distance_between_two_nodes('R0','B16',hashtable_node, list_node))

'''
THe result will include the final node "O" in the list.
neighbor = a.neighbor_nodes('B16',hashtable_node, list_node)
print(len(neighbor))
for element in neighbor:

    print(element.get_name())
'''

a.shortest_path(current_heap,hashtable_node,hashtable_heap,list_node,final_x,final_y,'O')
