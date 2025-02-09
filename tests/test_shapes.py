import pytest
from python_to_mermaid import MermaidDiagram, MermaidNode


def test_basic_shapes():
    """Test that basic shapes are correctly mapped to Mermaid syntax."""
    diagram = MermaidDiagram()

    # Test round/circle shape
    diagram.add_node("A", shape="circle", label="Circle Node")
    assert "A((Circle Node))" in diagram.to_mermaid()

    # Test diamond/rhombus shape
    diagram.add_node("B", shape="diamond", label="Diamond Node")
    assert "B{Diamond Node}" in diagram.to_mermaid()

    # Test stadium shape
    diagram.add_node("C", shape="stadium", label="Stadium Node")
    assert "C([Stadium Node])" in diagram.to_mermaid()


def test_alternative_shape_names():
    """Test that alternative shape names map to the correct syntax."""
    diagram = MermaidDiagram()

    # Test rounded (alternative to round)
    diagram.add_node("A", shape="rounded", label="Rounded Node")
    assert "A(Rounded Node)" in diagram.to_mermaid()

    # Test database (alternative to cylindrical)
    diagram.add_node("B", shape="database", label="DB Node")
    assert "B[(DB Node)]" in diagram.to_mermaid()


def test_direct_shape_syntax():
    """Test that direct Mermaid syntax for shapes works."""
    diagram = MermaidDiagram()
    node = MermaidNode(id="A", label="Custom Shape", shape=("{{", "}}"))
    diagram.add_node(node)
    assert "A{{Custom Shape}}" in diagram.to_mermaid()


def test_invalid_shape():
    """Test that invalid shapes raise ValueError."""
    diagram = MermaidDiagram()

    with pytest.raises(ValueError, match="Invalid shape: invalid_shape"):
        diagram.add_node("A", shape="invalid_shape")


def test_all_documented_shapes():
    """Test all shapes documented in SHAPE_MAP."""
    diagram = MermaidDiagram()

    for shape_name in MermaidDiagram.SHAPE_MAP.keys():
        node_id = f"node_{shape_name}"
        diagram.add_node(node_id, shape=shape_name, label=f"Test {shape_name}")

        # Get the expected syntax from SHAPE_MAP
        start, end = MermaidDiagram.SHAPE_MAP[shape_name]
        expected = f"{node_id}{start}Test {shape_name}{end}"

        assert expected in diagram.to_mermaid()


def test_shape_with_style():
    """Test that shapes work correctly with style attributes."""
    diagram = MermaidDiagram()

    node = MermaidNode(
        id="A",
        label="Styled Node",
        shape="circle",
        style={"fill": "#f9f", "stroke": "#333"},
    )
    diagram.add_node(node)

    mermaid_output = diagram.to_mermaid()
    assert "A((Styled Node))" in mermaid_output
    assert "style A fill:#f9f,stroke:#333" in mermaid_output


def test_default_shape_behavior():
    """Test behavior when no shape is specified."""
    diagram = MermaidDiagram()

    # Test with just an ID
    diagram.add_node("A")
    assert "A" in diagram.to_mermaid()

    # Test with ID and label, but no shape
    diagram.add_node("B", label="Label Only")
    assert 'B["Label Only"]' in diagram.to_mermaid()
