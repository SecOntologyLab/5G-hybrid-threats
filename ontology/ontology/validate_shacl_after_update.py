import os
from rdflib import Graph
from pyshacl import validate

# Paths to the corrected ontology and SHACL shapes files
# ontology_file = r"C://Users/andre/5G-hybrid-threats/ontology/ontology/ontology.ttl"  # Update with actual path
# shapes_file = r"C://Users/andre/5G-hybrid-threats/ontology/ontology/shapes_after_update.ttl"       # Update of impactLevel with absolute path

# ontology_file = "ontology.ttl"  # File is in the same directory
# shapes_file = "shapes.ttl"      # File is in the same directory

# Use standard absolute paths
script_dir = os.path.dirname(os.path.abspath(__file__))
ontology_file = os.path.join(script_dir, "ontology.ttl")
shapes_file = os.path.join(script_dir, "shapes_after_update.ttl")

# Print paths for debugging
print("Ontology file path:", ontology_file)
print("SHACL shapes file path:", shapes_file)

# Load the ontology and SHACL shapes
data_graph = Graph()
data_graph.parse(ontology_file, format="turtle")

shapes_graph = Graph()
shapes_graph.parse(shapes_file, format="turtle")

# Perform SHACL validation
print("Running SHACL validation...")
conforms, results_graph, results_text = validate(
    data_graph,
    shacl_graph=shapes_graph,
    inference="rdfs",  # You can also use "owlrl" if ontology has OWL constructs
    debug=True
)

# Print results
print("SHACL Validation Results:")
print(results_text)

# Save validation results to a file (optional)
with open("shacl_validation_results.ttl", "wb") as results_file:  # Open in binary mode
    results_graph.serialize(destination=results_file, format="turtle")

print("Validation complete. Results saved to 'shacl_validation_results.ttl'.")
