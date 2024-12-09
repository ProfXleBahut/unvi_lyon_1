import os
import re

def extract_docstrings(file_path):
    """Extract docstrings from a Python file."""
    docstrings = []
    with open(file_path, 'r') as file:
        content = file.read()
        docstrings.extend(re.findall(r'"""(.*?)"""', content, re.DOTALL))
    return docstrings

def generate_readme(project_path, recommendations_path, output_path="README.md"):
    """Generate a README.md file for the project."""
    # Read recommendations
    with open(recommendations_path, 'r') as file:
        recommendations = file.read()
    
    # Analyze project structure
    project_summary = []
    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                docstrings = extract_docstrings(file_path)
                project_summary.append({
                    "file": file_path,
                    "docstrings": docstrings
                })
    
    # Build the README content
    readme_content = ["# Project Documentation\n"]
    readme_content.append("## Project Structure\n")
    for item in project_summary:
        readme_content.append(f"- **{item['file']}**")
        for docstring in item['docstrings']:
            readme_content.append(f"  - {docstring.strip()}\n")
    
    readme_content.append("\n## Recommendations\n")
    readme_content.append(recommendations)

    # Write the README.md
    with open(output_path, 'w') as file:
        file.write("\n".join(readme_content))

# Example usage
generate_readme(
    project_path="path/to/your/project",
    recommendations_path="path/to/recommendations.txt"
)
