import pytest
from python_to_mermaid import (
    MermaidNode,
    MermaidEdge,
    MermaidDiagram,
    create_flowchart,
    create_sequence_diagram,
    create_class_diagram,
)


def test_create_node():
    """Test creating a MermaidNode with various configurations."""
    # Basic node
    node = MermaidNode("A")
    assert node.id == "A"
    assert node.label is None
    assert node.shape is None
    assert node.style is None

    # Node with label
    node = MermaidNode("B", label="Process")
    assert node.id == "B"
    assert node.label == "Process"

    # Node with style
    node = MermaidNode("C", style={"fill": "#f9f", "stroke": "#333"})
    assert node.id == "C"
    assert node.style == {"fill": "#f9f", "stroke": "#333"}


def test_create_edge():
    """Test creating a MermaidEdge with various configurations."""
    # Basic edge
    edge = MermaidEdge("A", "B")
    assert edge.source == "A"
    assert edge.target == "B"
    assert edge.label is None
    assert edge.style == "-->"

    # Edge with label
    edge = MermaidEdge("A", "B", label="process")
    assert edge.label == "process"

    # Edge with custom style
    edge = MermaidEdge("A", "B", style="===")
    assert edge.style == "==="


class TestMermaidDiagram:
    """Test suite for MermaidDiagram class."""

    def test_create_empty_diagram(self):
        """Test creating an empty diagram."""
        diagram = MermaidDiagram()
        assert diagram.diagram_type == "flowchart"
        assert diagram.direction == "TD"
        assert len(diagram.nodes) == 0
        assert len(diagram.edges) == 0

    def test_add_node(self):
        """Test adding nodes to diagram."""
        diagram = MermaidDiagram()
        node = MermaidNode("A", "Start")
        diagram.add_node(node)
        assert len(diagram.nodes) == 1
        assert diagram.nodes[0] == node

    def test_add_edge(self):
        """Test adding edges to diagram."""
        diagram = MermaidDiagram()
        edge = MermaidEdge("A", "B", "Next")
        diagram.add_edge(edge)
        assert len(diagram.edges) == 1
        assert diagram.edges[0] == edge

    def test_set_direction(self):
        """Test setting diagram direction."""
        diagram = MermaidDiagram()

        # Test valid directions
        valid_directions = ["TB", "TD", "BT", "LR", "RL"]
        for direction in valid_directions:
            diagram.set_direction(direction)
            assert diagram.direction == direction

        # Test invalid direction
        with pytest.raises(ValueError):
            diagram.set_direction("INVALID")

    def test_to_mermaid_empty(self):
        """Test converting empty diagram to Mermaid syntax."""
        diagram = MermaidDiagram()
        expected = "flowchart TD"
        assert diagram.to_mermaid() == expected

    def test_to_mermaid_with_nodes(self):
        """Test converting diagram with nodes to Mermaid syntax."""
        diagram = MermaidDiagram()
        diagram.add_node(MermaidNode("A", "Start"))
        diagram.add_node(MermaidNode("B", "End"))

        expected = "flowchart TD\n" '    A["Start"]\n' '    B["End"]'
        assert diagram.to_mermaid() == expected

    def test_to_mermaid_with_styled_nodes(self):
        """Test converting diagram with styled nodes to Mermaid syntax."""
        diagram = MermaidDiagram()
        diagram.add_node(MermaidNode("A", style={"fill": "#f9f"}))

        expected = "flowchart TD\n" "    A style A fill:#f9f"
        assert diagram.to_mermaid() == expected

    def test_to_mermaid_complete(self):
        """Test converting complete diagram to Mermaid syntax."""
        diagram = MermaidDiagram()
        diagram.set_direction("LR")
        diagram.add_node(MermaidNode("A", "Start"))
        diagram.add_node(MermaidNode("B", "End"))
        diagram.add_edge(MermaidEdge("A", "B", "Next"))

        expected = (
            "flowchart LR\n" '    A["Start"]\n' '    B["End"]\n' "    A --> B|Next|"
        )
        assert diagram.to_mermaid() == expected


def test_convenience_functions():
    """Test the convenience functions for creating different diagram types."""
    # Test flowchart
    flowchart = create_flowchart()
    assert flowchart.diagram_type == "flowchart"

    # Test sequence diagram
    sequence = create_sequence_diagram()
    assert sequence.diagram_type == "sequenceDiagram"

    # Test class diagram
    class_diagram = create_class_diagram()
    assert class_diagram.diagram_type == "classDiagram"


def test_practical_example():
    """Test a practical example of creating a complete diagram."""
    # Create a simple workflow diagram
    diagram = create_flowchart()
    diagram.set_direction("LR")

    # Add nodes
    nodes = [
        MermaidNode("start", "Start", style={"fill": "#green"}),
        MermaidNode("process", "Process Data"),
        MermaidNode("decision", "Check Result"),
        MermaidNode("end", "End", style={"fill": "#red"}),
    ]
    for node in nodes:
        diagram.add_node(node)

    # Add edges
    edges = [
        MermaidEdge("start", "process", "Begin"),
        MermaidEdge("process", "decision", "Analyze"),
        MermaidEdge("decision", "end", "Complete"),
    ]
    for edge in edges:
        diagram.add_edge(edge)

    # Verify the output contains all components
    mermaid_output = diagram.to_mermaid()
    assert "flowchart LR" in mermaid_output
    assert 'start["Start"]' in mermaid_output
    assert "style start fill:#green" in mermaid_output
    assert "start --> process|Begin|" in mermaid_output
