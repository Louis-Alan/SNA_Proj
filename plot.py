from neo4j import GraphDatabase
import networkx as nx
import matplotlib.pyplot as plt

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "1234567890"))
session = driver.session()

result = session.run("""
MATCH (n)-[r]-()
RETURN n, r
LIMIT 25
""")

G = nx.MultiDiGraph()

for record in result:
    node = record['n']
    relation = record['r']
    G.add_node(node.id)
    G.add_edge(node.id, relation.end_node.id, type=relation.type)

pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500, alpha=0.8)
nx.draw_networkx_edges(G, pos, edge_color='gray', alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
edge_labels = {(u, v): d['type'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

plt.axis('off')
plt.show()
