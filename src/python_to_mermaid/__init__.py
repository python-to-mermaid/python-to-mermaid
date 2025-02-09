"""
python-to-mermaid
================

A Python package that allows users to generate Mermaid diagrams using Python code.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass

__version__ = "0.1.0"


@dataclass
class MermaidNode:
    """Represents a node in a Mermaid diagram."""

    id: str
    label: Optional[str] = None
    shape: Optional[str] = None
    style: Optional[Dict[str, str]] = None


@dataclass
class MermaidEdge:
    """Represents an edge/connection between nodes in a Mermaid diagram."""

    source: str
    target: str
    label: Optional[str] = None
    style: Optional[str] = "---"


class MermaidDiagram:
    """Main class for creating Mermaid diagrams."""

    def __init__(self, diagram_type: str = "flowchart"):
        self.diagram_type = diagram_type
        self.nodes: List[MermaidNode] = []
        self.edges: List[MermaidEdge] = []
        self.direction = "TD"  # Top to Down by default

    def add_node(self, node: MermaidNode) -> "MermaidDiagram":
        """Add a node to the diagram."""
        self.nodes.append(node)
        return self

    def add_edge(self, edge: MermaidEdge) -> "MermaidDiagram":
        """Add an edge to the diagram."""
        self.edges.append(edge)
        return self

    def set_direction(self, direction: str) -> "MermaidDiagram":
        """Set the diagram direction (TB, BT, LR, or RL)."""
        valid_directions = ["TB", "TD", "BT", "LR", "RL"]
        if direction not in valid_directions:
            raise ValueError(f"Direction must be one of {valid_directions}")
        self.direction = direction
        return self

    def to_mermaid(self) -> str:
        """Convert the diagram to Mermaid syntax."""
        lines = [f"{self.diagram_type} {self.direction}"]

        # Add nodes
        for node in self.nodes:
            node_str = f"    {node.id}"
            if node.label:
                node_str += f'["{node.label}"]'
            if node.style:
                style_str = ", ".join(f"{k}:{v}" for k, v in node.style.items())
                node_str += f" style {node.id} {style_str}"
            lines.append(node_str)

        # Add edges
        for edge in self.edges:
            edge_str = f"    {edge.source} {edge.style} {edge.target}"
            if edge.label:
                edge_str += f"|{edge.label}|"
            lines.append(edge_str)

        return "\n".join(lines)


# Convenience functions
def create_flowchart() -> MermaidDiagram:
    """Create a new flowchart diagram."""
    return MermaidDiagram("flowchart")


def create_sequence_diagram() -> MermaidDiagram:
    """Create a new sequence diagram."""
    return MermaidDiagram("sequenceDiagram")


def create_class_diagram() -> MermaidDiagram:
    """Create a new class diagram."""
    return MermaidDiagram("classDiagram")


# Export main components
__all__ = [
    "MermaidNode",
    "MermaidEdge",
    "MermaidDiagram",
    "create_flowchart",
    "create_sequence_diagram",
    "create_class_diagram",
]
