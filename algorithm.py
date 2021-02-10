#name is the first node 
#current_heap is the PriorityQueue 
import math as m
import heapq 

def distance_straight_to_final_node(name, final_x, final_y, hashtable_list, list_node):
    
    #get index of the node in list_node
    row, column = hashtable_list[name]
 
    #then get position x, y of the node in list_node
    x = list_node[row][column].get_x()
    y = list_node[row][column].get_y()

    distance = m.sqrt(m.pow(x - final_x,2) + m.pow(y - final_y,2))

    return distance

def distance_between_two_nodes (first_name, second_name, hashtable_list, list_node):
    #get index of the first node in list_node
    first_row, first_column = hashtable_list[first_name]
 
    #then get position x, y of the first node in list_node
    first_x = list_node[first_row][first_column].get_x()
    first_y = list_node[first_row][first_column].get_y()

    #get index of the second node in list_node
    second_row, second_column = hashtable_list[second_name]
 
    #then get position x, y of the second node in list_node
    second_x = list_node[second_row][second_column].get_x()
    second_y = list_node[second_row][second_column].get_y()

    distance = m.sqrt(m.pow(first_x - second_x,2) + m.pow(first_y - second_y,2))

    return distance

def neighbor_nodes (name, hashtable_list, list_node):
    number_row = len(list_node)
    number_column = len(list_node[0])
    row, column = hashtable_list[name]
    dir = list_node[row][column].get_direction()
    color = name[0]

    neighbor_node = []
    if dir == "N":
        for i in range (0, row):
            if list_node[i][column].get_name()[0] != color: 
                neighbor_node.append(list_node[i][column])
        '''
        row -= 1
        while row >= 0:
            if list_node[row][column].get_name()[0] != color: 
                neighbor_node.append(list_node[row][column])
            row -= 1   
        '''   
        return neighbor_node
    elif dir == "S":
        for i in range (row + 1, number_row):
            if list_node[i][column].get_name()[0] != color: 
                neighbor_node.append(list_node[i][column])
        '''
        row += 1
        while row < number_row:
            if list_node[row][column].get_name()[0] != color: 
                neighbor_node.append(list_node[row][column])
            row += 1
        '''
        return neighbor_node
    elif dir == "E":
        for i in range (column + 1, number_column):
            if list_node[row][i].get_name()[0] != color: 
                neighbor_node.append(list_node[row][i])
        '''
        column += 1
        while column < number_column:
            if list_node[row][column].get_name()[0] != color: 
                neighbor_node.append(list_node[row][column])
            column += 1
        '''
        return neighbor_node
    elif dir == "W":
        for i in range (0, column):
            if list_node[row][i].get_name()[0] != color: 
                neighbor_node.append(list_node[row][i])
        '''
        column -= 1
        while column >= 0:
            if list_node[row][column].get_name()[0] != color: 
                neighbor_node.append(list_node[row][column])
            column -= 1
        '''
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


def shortest_path(name, current_heap, hashtable_list, hashtable_heap, list_node, final_x, final_y, final_name): 
    while len(current_heap) != 0:
        node_expand = heapq.heappop(current_heap)
        if node_expand[1][0] == final_name:
            break
        else:

        


