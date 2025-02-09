from python_to_mermaid import MermaidDiagram

# Create a new diagram
diagram = MermaidDiagram()

# Add nodes with text labels
diagram.add_node("A")  # Simple node
diagram.add_node("B[With Text]")  # Node with text label
diagram.add_node('C["Multi-line\nText"]')  # Node with multi-line text

# Add some edges to connect them
diagram.add_edge("A", "B")
diagram.add_edge("B", "C")

# Print the diagram
print(str(diagram))

# Save to markdown file
with open("examples/node_with_text.md", "w") as f:
    f.write("# Node with Text Example\n\n")
    f.write("```python\n")
    f.write(
        """from python_to_mermaid import MermaidDiagram

diagram = MermaidDiagram()
diagram.add_node("A")
diagram.add_node("B[With Text]") 
diagram.add_node('C["Multi-line\\nText"]')
diagram.add_edge("A", "B")
diagram.add_edge("B", "C")
"""
    )
    f.write("```\n\n")
    f.write("```mermaid\n")
    f.write(str(diagram))
    f.write("\n```")

"""
The above code generates:

flowchart TD
    A
    B[With Text]
    C["Multi-line
Text"]
    A --> B
    B --> C
"""
