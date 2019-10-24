from models import *
import json

class DB:

    __edgeContainer = EdgeContainer()

    @classmethod
    def __read_json(cls, fp):
        with open(fp, "r", encoding='utf-8') as read_file:
            data = json.load(read_file)
        for edge in data:
            source_type = data[edge][0].lower().strip()
            source_value = data[edge][1].lower().strip()
            target_type = data[edge][2].lower().strip()
            target_value = data[edge][3].lower().strip()
            connection_type = data[edge][4].lower().strip()
            sourceNode = Node(type=source_type, value=source_value)
            targetNode = Node(type=target_type, value=target_value)
            edge = Edge(connection_type, sourceNode=sourceNode, targetNode=targetNode)
            cls.__edgeContainer.add_edge(edge)

    @classmethod
    def get_edgeContainer(cls, fp):
        cls.__read_json(fp)
        return cls.__edgeContainer

if __name__ == '__main__':
    db = DB()
    container = db.get_edgeContainer('edgeCont.json')
