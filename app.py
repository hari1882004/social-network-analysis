from flask import Flask, render_template, jsonify
import networkx as nx
import pandas as pd
import json

app = Flask(__name__)

def run_analysis(edges=None):
    """Run the social network influence analysis."""
    if edges is None:
        # Default dataset
        data = {
            'source': ['A', 'A', 'B', 'C', 'D', 'E', 'F', 'C', 'B'],
            'target': ['B', 'C', 'C', 'D', 'E', 'F', 'A', 'F', 'E']
        }
    else:
        data = {'source': [e[0] for e in edges], 'target': [e[1] for e in edges]}

    df = pd.DataFrame(data)

    # Create directed graph
    G = nx.from_pandas_edgelist(df, 'source', 'target', create_using=nx.DiGraph())

    # PageRank
    pagerank = nx.pagerank(G)

    # Centrality measures
    degree_centrality = nx.degree_centrality(G)
    in_degree_centrality = nx.in_degree_centrality(G)
    out_degree_centrality = nx.out_degree_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)

    # Top influencer
    top_influencer = max(pagerank, key=pagerank.get)
    top_pagerank_score = pagerank[top_influencer]

    # Node metrics combined
    nodes_data = []
    for node in G.nodes():
        nodes_data.append({
            "id": node,
            "pagerank": round(pagerank.get(node, 0), 4),
            "degree": round(degree_centrality.get(node, 0), 4),
            "in_degree": round(in_degree_centrality.get(node, 0), 4),
            "out_degree": round(out_degree_centrality.get(node, 0), 4),
            "betweenness": round(betweenness_centrality.get(node, 0), 4),
            "is_top": node == top_influencer
        })

    # Sort by pagerank
    nodes_data.sort(key=lambda x: x["pagerank"], reverse=True)

    # Edges for graph
    edges_data = [{"source": u, "target": v} for u, v in G.edges()]

    # Stats
    stats = {
        "total_nodes": G.number_of_nodes(),
        "total_edges": G.number_of_edges(),
        "top_influencer": top_influencer,
        "top_pagerank_score": round(top_pagerank_score, 4),
        "graph_density": round(nx.density(G), 4),
        "is_strongly_connected": nx.is_strongly_connected(G),
        "strongly_connected_components": nx.number_strongly_connected_components(G),
        "weakly_connected_components": nx.number_weakly_connected_components(G),
    }

    return {
        "nodes": nodes_data,
        "edges": edges_data,
        "stats": stats
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/analysis")
def analysis():
    result = run_analysis()
    return jsonify(result)


@app.route("/api/custom-analysis", methods=["POST"])
def custom_analysis():
    from flask import request
    data = request.get_json()
    edges = data.get("edges", [])
    if not edges:
        return jsonify({"error": "No edges provided"}), 400
    try:
        result = run_analysis(edges)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
<<<<<<< HEAD
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
=======
    app.run(debug=True, port=5000)
>>>>>>> 38a720ec3fbbb8c278e111b2f1a3cca063e004f7
