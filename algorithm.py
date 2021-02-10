#name is the first node 
#current_heap is the PriorityQueue 
import math as m
import heapq 

def distance_straight_to_final_node(name, final_x, final_y, hashtable_node, list_node):
    
    #get index of the node in list_node
    row, column = hashtable_node[name]
 
    #then get position x, y of the node in list_node
    x = list_node[row][column].get_x()
    y = list_node[row][column].get_y()

    distance = m.sqrt(m.pow(x - final_x,2) + m.pow(y - final_y,2))

    return distance

def distance_between_two_nodes (first_name, second_name, hashtable_node, list_node):
    #get index of the first node in list_node
    first_row, first_column = hashtable_node[first_name]
 
    #then get position x, y of the first node in list_node
    first_x = list_node[first_row][first_column].get_x()
    first_y = list_node[first_row][first_column].get_y()

    #get index of the second node in list_node
    second_row, second_column = hashtable_node[second_name]
 
    #then get position x, y of the second node in list_node
    second_x = list_node[second_row][second_column].get_x()
    second_y = list_node[second_row][second_column].get_y()

    distance = m.sqrt(m.pow(first_x - second_x,2) + m.pow(first_y - second_y,2))

    return distance

#neighbor_nodes() function will return a list of neighbor nodes of the node with "name". 
#each node in list will be an object of node.
def neighbor_nodes (name, hashtable_node, list_node): 
    number_row = len(list_node)
    number_column = len(list_node[0])
    row, column = hashtable_node[name]
    dir = list_node[row][column].get_direction()
    color = name[0]

    neighbor_node = []
    if dir == "N":
        for i in range (0, row):
            if list_node[i][column].get_name()[0] != color: 
                neighbor_node.append(list_node[i][column])
                print("From N")
                print(list_node[i][column].get_name())
 
        return neighbor_node
    elif dir == "S":
        for i in range (row + 1, number_row):
            if list_node[i][column].get_name()[0] != color: 
                neighbor_node.append(list_node[i][column])
                print("From S")
                print(list_node[i][column].get_name())

        return neighbor_node
    elif dir == "E":
        for i in range (column + 1, number_column):
            if list_node[row][i].get_name()[0] != color: 
                neighbor_node.append(list_node[row][i])
                print("From E")
                print(list_node[row][i].get_name())

        return neighbor_node
    elif dir == "W":
        for i in range (0, column):
            if list_node[row][i].get_name()[0] != color: 
                neighbor_node.append(list_node[row][i])
                print("From W")
                print(list_node[row][i].get_name())
 
        return neighbor_node
    elif dir == "NE":
        for i in range (0, row):
            for j in range (column + 1, number_column):
                if list_node[i][j].get_name()[0] != color: 
                    neighbor_node.append(list_node[i][j])
                    print("From NE")
                    print(list_node[i][j].get_name())

        return neighbor_node
    elif dir == "NW":
        for i in range (0, row):
            for j in range (0, column):
                if list_node[i][j].get_name()[0] != color: 
                    neighbor_node.append(list_node[i][j])
                    print("From NW")
                    print(list_node[i][j].get_name())

        return neighbor_node
    elif dir == "SE":
        for i in range (row + 1, number_row):
            for j in range (column + 1, number_column):
                if list_node[i][j].get_name()[0] != color: 
                    neighbor_node.append(list_node[i][j])
                    print("From SE")
                    print(list_node[i][j].get_name())

        return neighbor_node
    elif dir == "SW":
        for i in range ( row + 1, number_row):
            for j in range (0, column):
                if list_node[i][j].get_name()[0] != color: 
                    neighbor_node.append(list_node[i][j])
                    print("From SW")
                    print(list_node[i][j].get_name())

        return neighbor_node


def shortest_path(current_heap, hashtable_node, hashtable_heap, list_node, final_x, final_y, final_name): 
    while len(current_heap) != 0:
        node_expand = heapq.heappop(current_heap)
        if node_expand[1][0] == final_name:
            print(node_expand[1][2])
            print(node_expand[1][3])
            break #should print the total distance
        else:
            name = node_expand[1][0]
            neighbor = neighbor_nodes(name,hashtable_node,list_node)
            if len(neighbor) == 0:
                pass
            else:
                for i in neighbor:
                    if i.get_name() not in hashtable_heap:
                        distance_straight = distance_straight_to_final_node(i.get_name(),final_x,final_y,hashtable_node, list_node)
                        distance_nodes = distance_between_two_nodes(name, i.get_name(), hashtable_node, list_node) + node_expand[1][1]
                        total_distance = distance_straight + distance_nodes
                        path = node_expand[1][3] + "-" + i.get_name()
                        heapq.heappush(current_heap, (total_distance, (i.get_name(), distance_nodes, total_distance, path)))
                    else:
                        distance_straight = distance_straight_to_final_node(i.get_name(),final_x,final_y,hashtable_node, list_node)
                        distance_nodes = distance_between_two_nodes(name, i.get_name(), hashtable_node, list_node) + + node_expand[1][1]
                        total_distance = distance_straight + distance_nodes
                        if total_distance >= hashtable_heap[name][2]:
                            pass
                        else:
                            current_heap.remove((hashtable_heap[i.get_name()][0],(hashtable_heap[i.get_name()][1])))
                            path = node_expand[1][3] + "-" + i.get_name()
                            heapq.heappush(current_heap, (total_distance, (i.get_name(), distance_nodes, total_distance, path)))
                            hashtable_node[i.get_name()] = (i.get_name(), distance_nodes, total_distance, path)




        

        



