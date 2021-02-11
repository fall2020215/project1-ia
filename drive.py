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


flag_algorithm = True
flag_step = True
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
'''
first_name = 'R26'
first_neighbor = a.neighbor_nodes(first_name,hashtable_node, list_node)

row_first_node, column_first_node = hashtable_node[first_name]
first_node = list_node[row_first_node][column_first_node]
'''



#################################
#CHANGE THE FIRST NODE
#################################

#innital for current_heap and hashtable_heap for first node:
#heapq.heappush(customers, (9, "Stacy"))
'''
distance_straight = a.distance_straight_to_final_node(first_name,final_x,final_y,hashtable_node, list_node)
heapq.heappush(current_heap, (distance_straight, (first_name, 0, distance_straight, first_name)))
hashtable_heap[first_name] = (first_name, 0 , distance_straight, first_name)

'''


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

#a.shortest_path(current_heap,hashtable_node,hashtable_heap,list_node,final_x,final_y,'O')

#FOR FEWEST NODE PATH
'''
heapq.heappush(current_heap, (1, (first_name, 0, 1, first_name)))
hashtable_heap[first_name] = (first_name, 0 , 1, first_name)
'''


#a.fewest_node_path(current_heap,hashtable_node,hashtable_heap,list_node,final_x,final_y,'O')


print()
print("Select one of A* algorithm heuristics following:\n")
print("(1) Straight-Line ") 
print("(2) Fewest-Nodes")
choice_algorithm  = input("Your algorithm_option: ")
#check the right value of input from user
choice_algorithm = a.check_option(choice_algorithm,1,2)


print("Select one of below options:\n")
print("(1) Step by Step ") 
print("(2) NO - Step by Step ")
choice_step = input("Your step_option: ")
#check the right value of input from user
choice_step = a.check_option(choice_step,1,2)


if choice_algorithm == "2":
    flag_algorithm = False
if choice_step == "2":
    flag_step = False


choice_node = input("Select a starting node: ")
#check the node's name if it is correct with input file
while choice_node not in hashtable_node:
    print("\nThe node's name is wrong. Please try again!\n")
    choice_node = input("Select a starting node: ")

first_name = choice_node
first_neighbor = a.neighbor_nodes(first_name,hashtable_node, list_node)

row_first_node, column_first_node = hashtable_node[first_name]
first_node = list_node[row_first_node][column_first_node]


if flag_algorithm:
    distance_straight = a.distance_straight_to_final_node(first_name,final_x,final_y,hashtable_node, list_node)
    heapq.heappush(current_heap, (distance_straight, (first_name, 0, distance_straight, first_name)))
    hashtable_heap[first_name] = (first_name, 0 , distance_straight, first_name)
    a.shortest_path(current_heap,hashtable_node,hashtable_heap,list_node,final_x,final_y,'O',flag_step)
else:
    heapq.heappush(current_heap, (1, (first_name, 0, 1, first_name)))
    hashtable_heap[first_name] = (first_name, 0 , 1, first_name)
    a.fewest_node_path(current_heap,hashtable_node,hashtable_heap,list_node,final_x,final_y,'O',flag_step)




