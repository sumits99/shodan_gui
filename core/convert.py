import os
import subprocess

def generate_ui_file(ui_file, output_py_file):
    # Run pyuic6 to generate the Python file from the .ui file
    subprocess.run(['pyuic6', '-o', output_py_file, ui_file], check=True)
    print(f"Generated {output_py_file} from {ui_file}")

def add_resource_import(output_py_file, resource_import_statement="import resource_rc"):
    # Read the generated Python file
    with open(output_py_file, 'r') as file:
        lines = file.readlines()

    # Check if the import statement is already present
    import_present = any(resource_import_statement in line for line in lines)

    if not import_present:
        # Find the position to insert the import statement
        for i, line in enumerate(lines):
            if line.startswith('from PyQt6'):
                insert_position = i + 1
                break

        # Insert the import statement
        lines.insert(insert_position, f"{resource_import_statement}\n")

        # Write the modified lines back to the file
        with open(output_py_file, 'w') as file:
            file.writelines(lines)
        
        print(f"Added {resource_import_statement} to {output_py_file}")
    else:
        print(f"{resource_import_statement} already present in {output_py_file}")

def main():
    ui_file = 'path/to/your/sidebar.ui'
    output_py_file = 'path/to/your/sidebar_ui.py'
    
    # Generate the UI Python file
    generate_ui_file(ui_file, output_py_file)

    # Add the resource import statement if not present
    add_resource_import(output_py_file)

if __name__ == "__main__":
    main()
