import csv
import json
from volatility.renderers.basic import Renderer

__author__ = 'Gino Placella'

#The main class being refered in commands.py
class CSVRenderer(Renderer):

    #initializer function not needed
    def __init__(self):
        pass

    """Func: render_row

    params: self: the class name, node: node of Tree, accumulator: list of where values are going to be written

    This function returns the list containing the data of the nodes that were visited in the tree when
    running volatility
    """
    def render_row(self, node, accumulator):
        return accumulator + [node.values]

    """Func: render

    params: self: the class name, outfd: the out file being written to, data: tree storing values

    This function renders the data into a writable CSV format
    """
    def render(self, outfd, data):
        #json_input is set to be the values in the tree to be parsed
        json_input = {"columns": [column.name for column in data.columns], "rows": data.visit(None, self.render_row, [])}

        info = []   #empty list to be updated
        for i in range(0, len(json_input['rows'])): #creating empty lists inside the list to store values
            info.append([])
        for i in range(0, len(json_input['rows'])): #iterating through json list to append to list of lists
            temp = str(json_input['rows'][i])
            info[i].append(temp.split("RowStructure", 1)[1])
        writer = csv.writer(outfd, delimiter=",") #setting writer for CSV file
        writer.writerows(info) #writing the rows to csv file
