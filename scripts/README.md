#   Scripts directory

# SHACL Validation Script

This repository contains a Python script for validating the **5G Hybrid Threats Ontology** against its SHACL shapes.

## Files in this Repository
- `validate_shacl.py`: A Python script for performing SHACL validation.

## Prerequisites
To run the script, you need:
- Python 3.7 or higher installed on your system.
- Add Python to your system PATH (if not already done).
- Install the following Python libraries:
  - `rdflib`
  - `pyshacl`

### Installing Dependencies
1. Open the Command Prompt.
2. Install the required Python libraries by running:
   ```cmd
   pip install rdflib pyshacl

## License
This script is released under the MIT License (  https://opensource.org/licenses/MIT ) to maximize reusability and collaboration. This means:
–	You can use, copy, modify, and distribute this script freely.
–	Attribution is required, meaning you must include the original license notice and copyright statement in any copy or substantial use of the script.
–	There is no warranty for this script; it is provided "as is."

***
## Detailed Instructions for SHACL Validation
Overview
The validate_shacl.py script validates the ontology (ontology.ttl) against SHACL constraints (shapes.ttl). This ensures compliance with semantic rules and constraints. The script works seamlessly in Windows environments, whether you use Command Prompt, PowerShell, or an IDE like VS Code.
________________________________________
### Steps to Validate the Ontology

1.	Clone the Repository Clone the repository to your local machine:
o	Command Prompt or PowerShell:

                            cmd
                            Copy code
                            git clone https://github.com/SecOntologyLab/5G-hybrid-threats.git
                            cd 5G-hybrid-threats

2.	Install Python Dependencies Ensure Python is installed (version 3.8 or higher) and install the required libraries:
o	Command Prompt or PowerShell:

                            cmd
                            Copy code
                            pip install rdflib

3.	Run the Validation Script You can run the validation script from either the ‘scripts’ directory or the ontology directory.
o	From the scripts Directory:
	Command Prompt or PowerShell:

                            cmd
                            Copy code
                            cd scripts
                            python validate_shacl.py

o	From the ontology Directory:
	Command Prompt or PowerShell:

                            cmd
                            Copy code
                            cd ontology
                            python validate_shacl.py

4.	Using Visual Tools You can also execute the script in IDEs like VS Code:
o	Open the repository in VS Code.
o	Navigate to the validate_shacl.py script.
o	Run the script using the built-in terminal (either Command Prompt or PowerShell) or debug tools.
________________________________________
## Future Enhancements
To improve clarity and usability, the SHACL shapes file (shapes.ttl) will soon be modularized into its major components:
•	Node Shapes
•	Property Shapes
•	Reusable Constraints
•	Other Specialized Shapes
This modular approach will make managing and understanding different categories of SHACL constraints easier.

