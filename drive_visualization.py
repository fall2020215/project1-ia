import node as n
import heapq
import algorithm as a

#For visualization
import matplotlib.pyplot as plt
import networkx as nx


######################### Part I: extract the input file into list_node, which is the same to an array 2D ###############
######################### BIGINNING PART I ######################################################

list_node = [] # Keep all nodes like an array 2D
size_maze = [] #keep the size of list_node (row and column)
hashtable_node = {} # key of hashtable_node is the name of node, and the value is the tuple of (row, column) in the array (list_node)
hashtable_heap = {} # key of hashtable_heap is the name of node, and the value is ....
current_heap = [] #current_heap is a list (array) of tuples that store all information about node_name, travel_distance, total_distance, and path


flag_algorithm = True
flag_step = True
path = "" # the path for shortest path or fewest path


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


#add all nodes from list_node to hashtable_node --> to look at quickly where a node is the list_node
# key of hashtable_node is the name of node, and the value is the tuple of (row, column) in the array (list_node)
for row in range (1, int(size_maze.split()[0]) + 1):
    for column in range (1, int(size_maze.split()[1]) + 1):
        name_node = list_node[row-1][column-1].get_name()
        hashtable_node[name_node] = (row-1, column-1)


#get position final_x and final_y of final node
final_row, final_column = hashtable_node['O']
final_x = list_node[final_row][final_column].get_x()
final_y = list_node[final_row][final_column].get_y()

################### FINISH PART I #############################################################


################### MAIN FUNCTION #############################################################


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
    if flag_step:
        title = "A* algorithm heuristics: straight-line\n" + "Step-by-Step: Yes\n" + "Starting node: " + first_name
        with open ("maze-sol.txt", "w") as file:
            file.write(title + "\n\n\n\n")
    else:
        title = "A* algorithm heuristics: straight-line\n" + "Step-by-Step: No\n" + "Starting node: " + first_name
        with open ("maze-sol.txt", "w") as file:
            file.write(title + "\n\n\n\n")

    distance_straight = a.distance_straight_to_final_node(first_name,final_x,final_y,hashtable_node, list_node)
    heapq.heappush(current_heap, (distance_straight, (first_name, 0, distance_straight, first_name)))
    hashtable_heap[first_name] = (first_name, 0 , distance_straight, first_name)
    path = a.shortest_path(current_heap,hashtable_node,hashtable_heap,list_node,final_x,final_y,'O',flag_step)
else:
    if flag_step:
        title = "A* algorithm heuristics: fewest-nodes\n" + "Step-by-Step: Yes\n" + "Starting node: " + first_name
        with open ("maze-sol.txt", "w") as file:
            file.write(title + "\n\n\n\n")
    else:
        title = "A* algorithm heuristics: fewest-nodes\n" + "Step-by-Step: No\n" + "Starting node: " + first_name
        with open ("maze-sol.txt", "w") as file:
            file.write(title + "\n\n\n\n")

    heapq.heappush(current_heap, (1, (first_name, 0, 1, first_name)))
    hashtable_heap[first_name] = (first_name, 0 , 1, first_name)
    path = a.fewest_node_path(current_heap,hashtable_node,hashtable_heap,list_node,final_x,final_y,'O',flag_step)



################# FINISH MAIN FUNCTION #######################################################################


################ VISUALIZATION ###############################################################################

graph_dict = {}

G = nx.DiGraph()

G.add_nodes_from(hashtable_node.keys())
for n, p in hashtable_node.items():
   G.nodes[n]['pos'] = p

    
graph_dict = a.graph_dict_node(hashtable_node, list_node)
add_edges = []
for i in graph_dict:
    list_name = graph_dict[i]
    for j in range (0, len(list_name)):
        add_edges.append((i, list_name[j]))

#Add all possible path from each node with its direction
G.add_edges_from(add_edges)
nx.draw(G, pos=hashtable_node, with_labels=True, font_size=12, node_size=4, edge_color = "g")


#The path for shortest path or fewest path
path_list = path.split("-")
add_edges_path = []

for i in range (0, len(path_list) - 1):
    add_edges_path.append((path_list[i],path_list[i+1]))

nx.draw_networkx_edges( G, pos = hashtable_node, edgelist = add_edges_path, width = 4,edge_color = "r")
    
plt.show()


################ FINISH VISUALIZATION ###################################################################


