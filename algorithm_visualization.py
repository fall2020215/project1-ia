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
 
        return neighbor_node
    elif dir == "S":
        for i in range (row + 1, number_row):
            if list_node[i][column].get_name()[0] != color: 
                neighbor_node.append(list_node[i][column])

        return neighbor_node
    elif dir == "E":
        for i in range (column + 1, number_column):
            if list_node[row][i].get_name()[0] != color: 
                neighbor_node.append(list_node[row][i])

        return neighbor_node
    elif dir == "W":
        for i in range (0, column):
            if list_node[row][i].get_name()[0] != color: 
                neighbor_node.append(list_node[row][i])
 
        return neighbor_node
    elif dir == "NE":
        for i in range (0, row):
            for j in range (column + 1, number_column):
                if list_node[i][j].get_name()[0] != color: 
                    neighbor_node.append(list_node[i][j])

        return neighbor_node
    elif dir == "NW":
        for i in range (0, row):
            for j in range (0, column):
                if list_node[i][j].get_name()[0] != color: 
                    neighbor_node.append(list_node[i][j])

        return neighbor_node
    elif dir == "SE":
        for i in range (row + 1, number_row):
            for j in range (column + 1, number_column):
                if list_node[i][j].get_name()[0] != color: 
                    neighbor_node.append(list_node[i][j])

        return neighbor_node
    elif dir == "SW":
        for i in range ( row + 1, number_row):
            for j in range (0, column):
                if list_node[i][j].get_name()[0] != color: 
                    neighbor_node.append(list_node[i][j])
  
        return neighbor_node


def shortest_path(current_heap, hashtable_node, hashtable_heap, list_node, final_x, final_y, final_name, flag_step): 
    flag = False
    neighbor = []
    while len(current_heap) != 0:
        node_expand = heapq.heappop(current_heap)
        
        if node_expand[1][0] == final_name:
            total_path = ""
            list_name_node = node_expand[1][3].split("-")
            for i in range (0, len(list_name_node)-1):
                total_path += list_name_node[i] + " to " + list_name_node[i + 1]  + " distance: " + str(round(distance_between_two_nodes(list_name_node[i],list_name_node[i+1], hashtable_node, list_node), 3)) + ",\n"

            title = "The final solution path is: \n" + total_path + "\n" + "*****************************************\n" + "Total path length: " + str(round(node_expand[1][2], 3))
            with open ("maze-sol.txt", "a") as file:
                file.write(title + "\n")
            flag = True
            return node_expand[1][3]
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
                        hashtable_heap[i.get_name()] = (i.get_name(), distance_nodes, total_distance, path)
                    else:
                        distance_straight = distance_straight_to_final_node(i.get_name(),final_x,final_y,hashtable_node, list_node)
                        distance_nodes = distance_between_two_nodes(name, i.get_name(), hashtable_node, list_node) +  node_expand[1][1]
                        total_distance = distance_straight + distance_nodes
                        if total_distance >= hashtable_heap[name][2]:
                            pass
                        else:
                            current_heap.remove((hashtable_heap[i.get_name()][0],(hashtable_heap[i.get_name()][1])))
                            path = node_expand[1][3] + "-" + i.get_name()
                            heapq.heappush(current_heap, (total_distance, (i.get_name(), distance_nodes, total_distance, path)))
                            hashtable_node[i.get_name()] = (i.get_name(), distance_nodes, total_distance, path)
            
            
            if flag_step:
                
                possible_node = ""
                possible_path = ""
    
                for i in current_heap:
                    possible_node += i[1][0] + " "
                    possible_path += i[1][0] + "(" + str(round(i[0],3)) + ")" + " "

                title = "Node selected: " +  node_expand[1][0] + "\n" + "Possible node to travel: " + possible_node + "\n" + "Node at the end of possible path: " + possible_path + "\n" + "********************************************************************************************************************\n"

                with open ("maze-sol.txt", "a") as file:
                    file.write(title + "\n")

    if flag != True:
        print("Do not have any path to go the final node")


        
def fewest_node_path(current_heap, hashtable_node, hashtable_heap, list_node, final_x, final_y, final_name, flag_step):
    flag = False
    neighbor = []
    while len(current_heap) != 0:
        node_expand = heapq.heappop(current_heap)
        
        if node_expand[1][0] == final_name:
            total_path = ""
            list_name_node = node_expand[1][3].split("-")
            for i in range (0, len(list_name_node)-1):
                total_path += list_name_node[i] + " to " + list_name_node[i + 1]  + " distance: " + "1,\n"

            title = "The final solution path is: \n" + total_path + "\n" + "*****************************************\n" + "Total path length: " + str(round(node_expand[1][2], 3))
            with open ("maze-sol.txt", "a") as file:
                file.write(title + "\n")
            flag = True
            return node_expand[1][3]
        else:
            
            name = node_expand[1][0]
            neighbor = neighbor_nodes(name,hashtable_node,list_node)
            if len(neighbor) == 0:
                pass
            else:
                for i in neighbor:
                    if i.get_name() not in hashtable_heap:
                        distance_straight = 0
                        distance_nodes = 1 + node_expand[1][1]
                        total_distance = distance_straight + distance_nodes
                        path = node_expand[1][3] + "-" + i.get_name()
                        heapq.heappush(current_heap, (total_distance, (i.get_name(), distance_nodes, total_distance, path)))
                        hashtable_heap[i.get_name()] = (i.get_name(), distance_nodes, total_distance, path)
                    else:
                        distance_straight = 0
                        distance_nodes = 1 +  node_expand[1][1]
                        total_distance = distance_straight + distance_nodes
                        if total_distance >= hashtable_heap[name][2]:
                            pass
                        else:
                            current_heap.remove((hashtable_heap[i.get_name()][0],(hashtable_heap[i.get_name()][1])))
                            path = node_expand[1][3] + "-" + i.get_name()
                            heapq.heappush(current_heap, (total_distance, (i.get_name(), distance_nodes, total_distance, path)))
                            hashtable_node[i.get_name()] = (i.get_name(), distance_nodes, total_distance, path)
            
            if flag_step:
                possible_node = ""
                possible_path = ""
    
                for i in current_heap:
                    possible_node += i[1][0] + " "
                    possible_path += i[1][0] + "(" + str(round(i[0],3)) + ")" + " "

                title = "Node selected: " +  node_expand[1][0] + "\n" + "Possible node to travel: " + possible_node + "\n" + "Node at the end of possible path: " + possible_path + "\n" + "********************************************************************************************************************\n"

                with open ("maze-sol.txt", "a") as file:
                    file.write(title + "\n")

    if flag != True:
        print("\nDo not have any path to go the final node\n")


############################### Check the input value ############################################

class Input_Value:
    #If the value is number (int, float)
    def isNumber(self,input):
        try:
            float(input)
            return True
        except ValueError:
            return False

    def isInt(self,input):
        try:
            int(input)
            return True
        except ValueError:
            return False

#check the value of option input
def check_option(value, low, high):
    p = Input_Value()
    while not p.isInt(value) or int(value) < low or int(value) > high:
        print("\nThe option should be a integer number between " + str(low) + " and " + str(high) + "!")
        print("Try again for your option!\n")
        value = input("Your selection: ")
        
    return value
        

############################################################################################################



################ VISUALIZATION -  CREATE ALL PATHS FROM EACH NODE ###########################################

def graph_dict_node(hashtable_node, list_node):
    graph_dict = {}
    for i in hashtable_node:
        if i != 'O':
            list_neighbor = neighbor_nodes(i, hashtable_node, list_node)
            #print(len(list_neighbor))
            list_neighbor_name = []
            for j in range (0, len(list_neighbor)):
                
                list_neighbor_name.append(list_neighbor[j].get_name())
        
            if len(list_neighbor_name) != 0:
                graph_dict[i] = list_neighbor_name
    
    return graph_dict


################ FINISH VISUALIZATION #################################################################
