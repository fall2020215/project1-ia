'''
The class Node will store all information of a node. It includes name, direction, x and y coordinate, the its position in an array 2D
'''
class Node:
    def __init__(self, name, direction, x, y, row, column):
        self.__name =  name
        self.__direction = direction
        self.__x = x
        self.__y = y
        self.__row = row
        self.__column = column
    
    def get_name(self):
        return self.__name
    def get_direction(self):
        return self.__direction
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def get_row(self):
        return self.__row
    def get_column(self):
        return self.__column
    

    