from rdflib import Graph, Namespace
import pyshacl
import sys
import os

# Define the SHACL namespace
sh = Namespace('http://www.w3.org/ns/shacl#')

def validate_ontology(ontology_file, shapes_file=None):
    try:
        # Create a new graph
        data_graph = Graph()
        
        # Load the ontology file
        print(f"Loading ontology from {ontology_file}...")
        data_graph.parse(ontology_file, format="turtle")
        
        # Load shapes file if provided
        if shapes_file and os.path.exists(shapes_file):
            print(f"Loading shapes from {shapes_file}...")
            data_graph.parse(shapes_file, format="turtle")
        
        print(f"Loaded {len(data_graph)} triples")

        # Print some debug info
        print("\nDebug Info:")
        print("Shapes found:")
        for s, p, o in data_graph.triples((None, None, sh.NodeShape)):
            print(f"- {s}")

        # Run the validation
        print("\nRunning SHACL validation...")
        conforms, validation_graph, validation_text = pyshacl.validate(
            data_graph,
            shacl_graph=None,
            inference='rdfs',
            debug=True,
            meta_shacl=False
        )

        # Print results
        print("\n=== Validation Results ===")
        print(f"Conforms: {conforms}")
        print("\nDetailed Report:")
        print(validation_text)

        return conforms, validation_text

    except Exception as e:
        print(f"Error during validation: {str(e)}")
        print(f"Error type: {type(e)}")
        return False, str(e)

if __name__ == "__main__":
    # Default file paths
    ontology_file = r"C:\Users\andre\5G-hybrid-threats\Decoding5G\ontology\ontology_fght.ttl"
    shapes_file = r"C:\Users\andre\5G-hybrid-threats\Decoding5G\ontology\shapes_fght.ttl"

    # Override with command line arguments if provided
    if len(sys.argv) > 1:
        ontology_file = sys.argv[1]
    if len(sys.argv) > 2:
        shapes_file = sys.argv[2]

    success, report = validate_ontology(ontology_file, shapes_file)
    
    if success:
        print("\nValidation successful! No violations found.")
    else:
        print("\nValidation failed. Please check the report above for details.")