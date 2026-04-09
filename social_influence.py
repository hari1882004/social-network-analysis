<<<<<<< HEAD
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# -----------------------------
# Step 1: Create sample dataset
# -----------------------------
data = {
    'source': ['A', 'A', 'B', 'C', 'D', 'E', 'F', 'C', 'B'],
    'target': ['B', 'C', 'C', 'D', 'E', 'F', 'A', 'F', 'E']
}

df = pd.DataFrame(data)

# -----------------------------
# Step 2: Create graph
# -----------------------------
G = nx.from_pandas_edgelist(df, 'source', 'target', create_using=nx.DiGraph())

# -----------------------------
# Step 3: Apply PageRank
# -----------------------------
pagerank = nx.pagerank(G)

print("\n--- PageRank Scores ---")
for node, score in pagerank.items():
    print(f"{node}: {score:.4f}")

# -----------------------------
# Step 4: Centrality Measures
# -----------------------------
degree_centrality = nx.degree_centrality(G)

print("\n--- Degree Centrality ---")
for node, score in degree_centrality.items():
    print(f"{node}: {score:.4f}")

# -----------------------------
# Step 5: Identify Top Influencers
# -----------------------------
top_influencer = max(pagerank, key=pagerank.get)

print(f"\nMost Influential User (PageRank): {top_influencer}")

# -----------------------------
# Step 6: Draw Graph
# -----------------------------
plt.figure(figsize=(8,6))
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10)
plt.title("Social Network Graph")
=======
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# -----------------------------
# Step 1: Create sample dataset
# -----------------------------
data = {
    'source': ['A', 'A', 'B', 'C', 'D', 'E', 'F', 'C', 'B'],
    'target': ['B', 'C', 'C', 'D', 'E', 'F', 'A', 'F', 'E']
}

df = pd.DataFrame(data)

# -----------------------------
# Step 2: Create graph
# -----------------------------
G = nx.from_pandas_edgelist(df, 'source', 'target', create_using=nx.DiGraph())

# -----------------------------
# Step 3: Apply PageRank
# -----------------------------
pagerank = nx.pagerank(G)

print("\n--- PageRank Scores ---")
for node, score in pagerank.items():
    print(f"{node}: {score:.4f}")

# -----------------------------
# Step 4: Centrality Measures
# -----------------------------
degree_centrality = nx.degree_centrality(G)

print("\n--- Degree Centrality ---")
for node, score in degree_centrality.items():
    print(f"{node}: {score:.4f}")

# -----------------------------
# Step 5: Identify Top Influencers
# -----------------------------
top_influencer = max(pagerank, key=pagerank.get)

print(f"\nMost Influential User (PageRank): {top_influencer}")

# -----------------------------
# Step 6: Draw Graph
# -----------------------------
plt.figure(figsize=(8,6))
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10)
plt.title("Social Network Graph")
>>>>>>> 38a720ec3fbbb8c278e111b2f1a3cca063e004f7
plt.show()