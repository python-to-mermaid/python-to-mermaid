import os


def generate_examples_markdown() -> None:
    """Generate markdown files showcasing all example Python files in the examples directory."""

    examples_dir = os.path.dirname(__file__)
    for python_filepath in os.listdir(examples_dir):
        if python_filepath.endswith(".py") and python_filepath != "__main__.py":
            generate_example_md(os.path.join(examples_dir, python_filepath))


def generate_example_md(python_filepath: str) -> None:
    """Generate a markdown file showcasing a Python example file.

    The markdown file will contain:
    1. The Python source code
    2. The rendered Mermaid diagram
    3. The Mermaid diagram code
    """
    # Read the Python file
    with open(python_filepath, "r") as f:
        python_code = f.read()

    # Execute the Python code to get the diagram
    namespace = {}
    exec(python_code, namespace)
    diagram = namespace.get("diagram")

    if not diagram:
        raise ValueError("Python file must create a 'diagram' variable")

    # Generate markdown filename
    md_filename = os.path.splitext(python_filepath)[0] + ".md"

    # Get just the filename without path for the title
    title = os.path.splitext(os.path.basename(python_filepath))[0]
    title = title.replace("_", " ").title()

    # Write the markdown file
    with open(md_filename, "w") as f:
        # Write title
        f.write(f"# {title} Example\n\n")

        # Write Python code
        f.write("```python\n")
        f.write(python_code)
        f.write("```\n\n")

        # Write Mermaid diagram
        f.write("```mermaid\n")
        f.write(str(diagram))
        f.write("\n```\n\n")

        # Write Mermaid diagram code
        f.write("```bash\n")
        f.write(str(diagram))
        f.write("\n```\n")


if __name__ == "__main__":
    generate_examples_markdown()
