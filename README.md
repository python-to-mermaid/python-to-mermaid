# python-to-mermaid

Generate mermaid diagrams from python code.

## Installation

```bash
pip install python-to-mermaid
```

## Usage

```python
from python_to_mermaid import MermaidDiagram

diagram = MermaidDiagram()
diagram.add_node("A")
diagram.add_node("B")
diagram.add_edge("A", "B")

mermaid_diagram = str(diagram)
# flowchart TD
#     A
#     B
#     A --> B
```

```mermaid
flowchart TD
    A
    B
    A --> B
```

## Examples

See the [examples](examples) directory for more examples.

- [Node with Text](examples/node_with_text.md)

## Development

```bash
uv sync
```

## Testing

```bash
pytest tests/ -v
```

## Publishing

```bash
./publish.sh
```

```bash
chmod +x publish.sh
```
