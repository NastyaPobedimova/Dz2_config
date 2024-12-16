import os
import sys
import ast
import subprocess

def get_dependencies(py_file_path, dependencies=None, visited=None):
    if dependencies is None:
        dependencies = {}
    if visited is None:
        visited = set()

    # Read the Python file
    with open(py_file_path, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read())

    # Extract module name from filename
    module_name = os.path.splitext(os.path.basename(py_file_path))[0]
    
    # Track current module's dependencies
    dependencies[module_name] = []

    # Analyze imports
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                dep_name = alias.name.split('.')[0]  # Get top-level module name
                if dep_name not in dependencies[module_name] and dep_name != module_name:
                    dependencies[module_name].append(dep_name)
        
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                dep_name = node.module.split('.')[0]
                if dep_name not in dependencies[module_name] and dep_name != module_name:
                    dependencies[module_name].append(dep_name)

    return dependencies

def generate_plantuml_graph(dependencies):
    plantuml_code = "@startuml\n"
    plantuml_code += "skinparam defaultTextAlignment center\n"
    plantuml_code += "skinparam componentStyle uml2\n\n"

    for module, deps in dependencies.items():
        for dep in deps:
            plantuml_code += f'[{module}] --> [{dep}]\n'

    plantuml_code += "@enduml"
    return plantuml_code

def show_graph(image_path):
    if sys.platform == "win32":
        os.startfile(image_path)
    elif sys.platform == "darwin":
        subprocess.run(["open", image_path])
    else:
        subprocess.run(["xdg-open", image_path])

def visualize_dependencies(plantuml_path, py_file_path, output_png):
    dependencies = get_dependencies(py_file_path)
    plantuml_code = generate_plantuml_graph(dependencies)

    temp_puml = "dependency_graph.puml"
    
    with open(temp_puml, "w") as f:
        f.write(plantuml_code)

    try:
        result = subprocess.run(['java', '-jar', plantuml_path, temp_puml, '-o', os.path.dirname(output_png)], 
                              capture_output=True, 
                              text=True)
        
        if result.returncode != 0:
            print(f"Ошибка при генерации графа: {result.stderr}")
            sys.exit(1)

        generated_png = os.path.join(os.path.dirname(output_png), 'dependency_graph.png')
        os.rename(generated_png, output_png)
        os.remove(temp_puml)

        print(f"График сохранен в файл: {output_png}")

    except Exception as e:
        print(f"Ошибка: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Использование: {sys.argv[0]} <путь_к_plantuml.jar> <путь_к_python_файлу> <путь_к_png_файлу>")
        sys.exit(1)

    plantuml_path = sys.argv[1]
    py_file_path = sys.argv[2]
    output_png = sys.argv[3]

    visualize_dependencies(plantuml_path, py_file_path, output_png)
