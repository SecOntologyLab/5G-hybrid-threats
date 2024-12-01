from pyshacl import validate
from rdflib import Graph

# Load your ontology and SHACL Shapes in one file
data_graph = Graph()
data_graph.parse("./ontology/Instances and Shapes Nov 10.ttl", format="turtle")
# data_graph.parse(r"C:/Users/andre/ontology/SHACL_chatGPT/Instances and Shapes Nov 10.ttl", format="turtle")
# data_graph.parse("./Instances and Shapes Nov 10.ttl", format="turtle")

# Create a separate graph for SHACL shapes
shapes_graph = Graph()
shapes_graph.parse("./ontology/Instances and Shapes Nov 10.ttl", format="turtle")
# shapes_graph.parse(r"C:/Users/andre/ontology/SHACL_chatGPT/Instances and Shapes Nov 10.ttl", format="turtle")

# Run the SHACL validation
conforms, results_graph, results_text = validate(data_graph, shacl_graph=shapes_graph, inference='rdfs', debug=True)

# Print validation results
print(results_text)

# print(shapes_graph.serialize(format='turtle'))

