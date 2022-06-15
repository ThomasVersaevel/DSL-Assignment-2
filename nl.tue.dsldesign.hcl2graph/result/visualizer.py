import xml.etree.ElementTree as ET
import graphviz

import os
# os.environ["PATH"] += os.pathsep +'C:/Users/Merel/anaconda3/Lib/site-packages/graphviz/'

# print(os.getcwd())
# filename = 'D:/GitHub/DSL-Assignment-2/nl.tue.dsldesign.hcl2graph/result/TransformedHCL'
filename = 'TransformedHCL'

if not os.path.exists(filename):
    print('ERROR : This path does not exist !!')

with open(filename, 'rb') as file:
    tree = ET.parse(file)
root = tree.getroot()

structure_name = 'HCLgraph' # structure.findtext('./Name')
graph = graphviz.Digraph(format='svg',comment='structure_name', node_attr={'shape': 'box'})


i = 0

# read all the structures
for node in root.findall('nodes'): # root: #.findall('./Graph'):
    label = node.attrib['label']
    nodeId = "//@nodes.{}".format(i)
    # n = Node(node.attrib['label'], i)
    # nodelist.append(n)
    
    if 'shape' in node.attrib:
        graph.node(nodeId, label, shape='oval')
    graph.node(nodeId, label)
    
    i += 1
        
    for edge in node:
        target = edge.attrib['target']
        if 'style' in edge.attrib:
            graph.edge(nodeId, target, style='dashed')
        else: graph.edge(nodeId, target)
    
    
    # read the nodes of the structure
    # for node in structure.findall('.//Nodes/Node'):
    #     node_element_id = node.findtext('./ElementID')
    #     # find the name
    #     element_name = root.findtext(".//Elements/Element[ID='{}']/Name".format(node_element_id))
    #     graph.node(node_element_id, element_name)
    #
    # # read the links
    # for link in structure.findall('.//Links/Link'):
    #     id_1 = link.findtext('./LHS')
    #     id_2 = link.findtext('./RHS')
    #     description = link.findtext('./Description')
    #     direction = link.findtext('./Direction')
    #     graph.edge(id_1, id_2, label=description)
    #     if direction=='Double':
    #         graph.edge(id_2, id_1, label=description)

graph.render(filename=structure_name, view=True)