# Graph model

The graph model is implemented in `api/graph_api`.
It is independent of Django and can be used by the platform and plugins.

## Classes

- `GraphElement` stores an element ID and attributes, and provides
  methods for reading the ID and managing attributes.
- `Node` inherits the shared behavior from `GraphElement`.
- `Edge` extends `GraphElement` with source and target node IDs.
- `Graph` manages nodes and edges and defines whether the graph
  is directed or undirected.

Nodes and edges are stored in dictionaries indexed by their IDs.
An edge references its endpoints by node ID.

## Attributes

Attribute names are strings. Supported value types are `int`, `float`,
`str` and `datetime.date`.

Values are stored in their original Python types, without conversion
to strings. `set_attribute` validates names and values and raises
`TypeError` for unsupported types.

`get_attributes` returns a shallow copy of the attribute dictionary.
This is sufficient because all supported value types are immutable.

## Graph rules

- Node IDs are unique among nodes within a graph.
- Edge IDs are unique among edges within a graph.
- Both endpoint nodes must exist before an edge can be added.
- Isolated nodes, disconnected components, cycles and self-loops
  are allowed.
- Parallel edges are not allowed.
- In directed graphs, A → B and B → A are distinct edges.
- In undirected graphs, A — B and B — A represent the same edge.
- A node can be removed only after all its incident edges are removed.
- Removing an edge does not remove its endpoint nodes.
- Graph direction is selected at creation and exposed through
  the read-only `directed` property.


## Public API

Graph provides methods for adding, retrieving and removing nodes
and edges, and retrieving their collections.

Node and Edge inherit methods for reading their IDs and managing
attributes from GraphElement. Edge also exposes its endpoint IDs.

Graph direction is available through the `directed` property.