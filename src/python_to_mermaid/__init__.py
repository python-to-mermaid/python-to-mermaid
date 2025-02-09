"""
python-to-mermaid
================

A Python package that allows users to generate Mermaid diagrams using Python code.
"""

from typing import Dict, List, Optional, Union, Tuple
from dataclasses import dataclass
import importlib.metadata

__version__ = importlib.metadata.version("python-to-mermaid")


@dataclass
class MermaidNode:
    """Represents a node in a Mermaid diagram."""

    id: str
    label: Optional[str] = None
    shape: Optional[Union[str, Tuple[str, str]]] = None
    style: Optional[Dict[str, str]] = None


@dataclass
class MermaidEdge:
    """Represents an edge/connection between nodes in a Mermaid diagram."""

    source: str
    target: str
    label: Optional[str] = None
    style: Optional[str] = "-->"


class MermaidDiagram:
    """Main class for creating Mermaid diagrams."""

    # Map friendly shape names to Mermaid syntax
    SHAPE_MAP = {
        # Basic shapes
        "default": ["", ""],
        "round": ["(", ")"],
        "stadium": ["([", "])"],
        "subroutine": ["[[", "]]"],
        "cylindrical": ["[(", ")]"],
        "circle": ["((", "))"],
        "asymmetric": [">", "]"],
        "rhombus": ["{", "}"],
        "hexagon": ["{{", "}}"],
        "parallelogram": ["[/", "/]"],
        "parallelogram_alt": ["[\\", "\\]"],
        "trapezoid": ["[/", "\\]"],
        "trapezoid_alt": ["[\\", "/]"],
        "double_circle": ["(((", ")))"],
        # Alternative names for shapes
        "rounded": ["(", ")"],
        "diamond": ["{", "}"],
        "database": ["[(", ")]"],
    }

    def __init__(self, diagram_type: str = "flowchart"):
        self.diagram_type = diagram_type
        self.nodes: List[MermaidNode] = []
        self.edges: List[MermaidEdge] = []
        self.direction = "TD"  # Top to Down by default
        self.handled_shapes_mermaid_syntax = [
            "".join(self.SHAPE_MAP[shape]) for shape in self.SHAPE_MAP
        ]

    def add_node(
        self,
        node: Union[str, MermaidNode],
        shape: Optional[Union[str, Tuple[str, str]]] = None,
        label: Optional[str] = None,
    ) -> "MermaidDiagram":
        """Add a node to the diagram.

        Args:
            node: Either a string ID for a simple node, or a MermaidNode instance
            shape: Optional shape for the node. Can be either:
                  - A friendly name like 'circle', 'diamond'
                  - A tuple of (start, end) characters like ('((', '))')
            label: Optional label for the node. If not provided, will use the node ID as label.
        """
        if isinstance(node, str):
            label = label if label is not None else node
            node = MermaidNode(id=node, label=label, shape=shape)

        if node.shape:
            if isinstance(node.shape, tuple):
                start, end = node.shape
            else:
                if node.shape not in self.SHAPE_MAP:
                    raise ValueError(f"Invalid shape: {node.shape}")
                start, end = self.SHAPE_MAP[node.shape]

            node_str = f"{start}{node.label or ''}{end}"
            if node_str not in self.handled_shapes_mermaid_syntax:
                self.handled_shapes_mermaid_syntax.append(node_str)

        self.nodes.append(node)
        return self

    def add_edge(
        self,
        source: Union[str, MermaidEdge],
        target: Optional[str] = None,
        label: Optional[str] = None,
        style: Optional[str] = "-->",
    ) -> "MermaidDiagram":
        """Add an edge to the diagram.

        Args:
            source: Either a string source node ID or a MermaidEdge instance
            target: Target node ID if source is a string
            label: Optional edge label if source is a string
            style: Optional edge style if source is a string
        """
        if isinstance(source, str):
            if target is None:
                raise ValueError("target must be provided when source is a string")
            edge = MermaidEdge(source=source, target=target, label=label, style=style)
        else:
            edge = source
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
            if node.shape:
                if isinstance(node.shape, tuple):
                    start, end = node.shape
                else:
                    start, end = self.SHAPE_MAP[node.shape]
                node_str += f"{start}{node.label or ''}{end}"
            elif node.label:
                node_str += f'["{node.label}"]'

            if node.style:
                style_str = ",".join(f"{k}:{v}" for k, v in node.style.items())
                node_str += f" style {node.id} {style_str}"
            lines.append(node_str)

        # Add edges
        for edge in self.edges:
            edge_str = f"    {edge.source} {edge.style} {edge.target}"
            if edge.label:
                edge_str += f"|{edge.label}|"
            lines.append(edge_str)

        return "\n".join(lines)

    def __str__(self) -> str:
        return self.to_mermaid()


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
