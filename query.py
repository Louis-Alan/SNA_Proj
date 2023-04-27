from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "1234567890"))
session = driver.session()

# Run a Cypher query to find the degree centrality of nodes in the graph
result = session.run("""
MATCH (n)
OPTIONAL MATCH (n)-[r]-()
RETURN id(n) as id, count(r) as degree
ORDER BY degree DESC
LIMIT 10
""")

# Print the top 10 nodes and their degree centrality scores
print("Top 10 nodes by degree centrality:")
for i, record in enumerate(result):
    print(f"{i+1}. Node {record['id']}, degree centrality: {record['degree']}")
