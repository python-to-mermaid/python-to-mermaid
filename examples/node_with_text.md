# Node With Text Example

```python
from python_to_mermaid import MermaidDiagram

diagram = MermaidDiagram()

diagram.add_node("A")
diagram.add_node("B[With Text]")
diagram.add_node('C["Multi-line\nText"]')

diagram.add_edge("A", "B")
diagram.add_edge("B", "C")

result = str(diagram)
```

```mermaid
flowchart TD
    A["A"]
    B[With Text]["B[With Text]"]
    C["Multi-line
Text"]["C["Multi-line
Text"]"]
    A --> B
    B --> C
```

```bash
flowchart TD
    A["A"]
    B[With Text]["B[With Text]"]
    C["Multi-line
Text"]["C["Multi-line
Text"]"]
    A --> B
    B --> C
```
