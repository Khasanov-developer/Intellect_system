
class EdgeContainer:
    
    def __init__(self):
        self.__edgeList = []

    def get_list(self):
        return self.__edgeList

    def add_edge(self, edgeObj):
        self.__edgeList.append(edgeObj)

    def get_edge_set_by_source(self, sourceValue):
        edge_set = list()
        for edge in self.__edgeList:
            if edge.get_source().get_value() == sourceValue.lower().strip():
                edge_set.append(edge)
        return edge_set

    def get_edge_set_by_target(self, targetValue):
        edge_set = list()
        for edge in self.__edgeList:
            if edge.get_target().get_value() == targetValue.lower().strip():
                edge_set.append(edge)
        return edge_set


class Edge:
    def __init__(self, connectionType, sourceNode = None, targetNode = None):
        self.__source = sourceNode
        self.__target = targetNode
        self.__connectionType = connectionType
    
    def get_source(self):
        return self.__source
    
    def get_target(self):
        return self.__target
    
    def get_connectionType(self):
        return self.__connectionType
    
class Node:
    def __init__(self, type, value):
        self.__type = type
        self.__value = value
        
    def get_type(self):
        return self.__type
    
    def get_value(self):
        return self.__value

