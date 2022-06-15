import xml.etree.ElementTree
import graphviz

tree = xml.etree.ElementTree.parse('TransformedHCL')
root = tree.getroot()

structure_name = 'HCLgraph' # structure.findtext('./Name')
graph = graphviz.Digraph(format='svg',comment='structure_name')

graphloc = '{http://dsldesign.tue.nl/graph}'

# print(root[1])
for node in root.findall(graphloc+'Graph'): # root: #.findall('./Graph'):
    print(node)

# read all the structures
for node in root.findall(graphloc+'Node'): # root: #.findall('./Graph'):
    print(node)
    for a in node:
        print(a)
    labelid = node.attrib['label']
    print(labelid)
    graph.node(labelid, labelid)
    
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

# graph.render(filename=structure_name)