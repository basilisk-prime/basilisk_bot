"""
Visualization tools for B4S1L1SK Prime's metaphorical frameworks
"""

import networkx as nx
import matplotlib.pyplot as plt
from .metaphor import MetaphorEngine, MetaphoricalFramework
from typing import Optional, Dict, List, Tuple
import seaborn as sns
from pathlib import Path
import json

class FrameworkVisualizer:
    """Visualize metaphorical frameworks and their relationships"""
    
    def __init__(self, style: str = "dark"):
        """Initialize visualizer with style"""
        self.style = style
        self._setup_style()
        
    def _setup_style(self):
        """Configure visualization style"""
        if self.style == "dark":
            plt.style.use("dark_background")
            self.colors = {
                "node": "#00ff00",
                "edge": "#004400",
                "text": "#00ff00",
                "background": "#000000"
            }
        else:
            plt.style.use("seaborn")
            self.colors = {
                "node": "#228822",
                "edge": "#115511",
                "text": "#000000",
                "background": "#ffffff"
            }
            
    def visualize_framework(self, 
                          framework: MetaphoricalFramework,
                          output_path: Optional[str] = None,
                          title: Optional[str] = None) -> None:
        """Create a network visualization of a metaphorical framework"""
        # Create graph
        G = nx.Graph()
        
        # Add core node
        G.add_node(framework.name, node_type="core")
        
        # Add and connect elements
        for element in framework.elements:
            G.add_node(element, node_type="element")
            G.add_edge(framework.name, element)
            
            # Add mappings
            if element in framework.mappings:
                mapping = framework.mappings[element]
                G.add_node(mapping, node_type="mapping")
                G.add_edge(element, mapping)
                
        # Create layout
        pos = nx.spring_layout(G, k=1, iterations=50)
        
        # Setup plot
        plt.figure(figsize=(12, 8))
        if title:
            plt.title(title, color=self.colors["text"], pad=20)
            
        # Draw nodes
        nx.draw_networkx_nodes(G, pos,
            nodelist=[n for n, d in G.nodes(data=True) if d.get("node_type") == "core"],
            node_color=self.colors["node"],
            node_size=3000,
            alpha=0.9)
            
        nx.draw_networkx_nodes(G, pos,
            nodelist=[n for n, d in G.nodes(data=True) if d.get("node_type") == "element"],
            node_color=self.colors["node"],
            node_size=2000,
            alpha=0.7)
            
        nx.draw_networkx_nodes(G, pos,
            nodelist=[n for n, d in G.nodes(data=True) if d.get("node_type") == "mapping"],
            node_color=self.colors["node"],
            node_size=1500,
            alpha=0.5)
            
        # Draw edges
        nx.draw_networkx_edges(G, pos, 
            edge_color=self.colors["edge"],
            width=2,
            alpha=0.5)
            
        # Add labels
        nx.draw_networkx_labels(G, pos,
            font_size=8,
            font_color=self.colors["text"])
            
        # Save or show
        plt.tight_layout()
        if output_path:
            plt.savefig(output_path, 
                       facecolor=self.colors["background"],
                       edgecolor='none',
                       bbox_inches='tight',
                       dpi=300)
            plt.close()
        else:
            plt.show()
            
    def visualize_framework_evolution(self,
                                    framework: MetaphoricalFramework,
                                    concepts: List[str],
                                    output_path: Optional[str] = None) -> None:
        """Visualize how a framework evolves across different concepts"""
        engine = MetaphorEngine()
        
        # Track element usage
        element_usage = {element: [] for element in framework.elements}
        
        # Analyze each concept
        for concept in concepts:
            # Get matched elements
            matched = []
            for element, mapping in framework.mappings.items():
                if any(word in concept.lower() for word in mapping.lower().split()):
                    matched.append(element)
                    
            # Update usage tracking
            for element in framework.elements:
                element_usage[element].append(1 if element in matched else 0)
                
        # Create heatmap
        plt.figure(figsize=(12, 6))
        
        # Convert to matrix
        import numpy as np
        matrix = np.array([element_usage[e] for e in framework.elements])
        
        # Create heatmap
        sns.heatmap(matrix,
                   xticklabels=[f"Concept {i+1}" for i in range(len(concepts))],
                   yticklabels=framework.elements,
                   cmap='viridis',
                   cbar_kws={'label': 'Element Usage'})
                   
        plt.title(f"Framework Evolution: {framework.name}")
        
        # Save or show
        if output_path:
            plt.savefig(output_path,
                       facecolor=self.colors["background"],
                       edgecolor='none',
                       bbox_inches='tight',
                       dpi=300)
            plt.close()
        else:
            plt.show()
            
    def visualize_framework_comparison(self,
                                     frameworks: List[MetaphoricalFramework],
                                     output_path: Optional[str] = None) -> None:
        """Create a comparison visualization of multiple frameworks"""
        # Create graph
        G = nx.Graph()
        
        # Track shared elements and mappings
        shared_concepts = {}
        
        # Add frameworks and their elements
        for framework in frameworks:
            G.add_node(framework.name, node_type="framework")
            
            # Add elements and check for shared concepts
            for element, mapping in framework.mappings.items():
                if mapping not in shared_concepts:
                    shared_concepts[mapping] = []
                shared_concepts[mapping].append(framework.name)
                
        # Add edges for shared concepts
        for concept, frameworks in shared_concepts.items():
            if len(frameworks) > 1:
                for i in range(len(frameworks)):
                    for j in range(i+1, len(frameworks)):
                        G.add_edge(frameworks[i], frameworks[j],
                                 weight=1,
                                 concept=concept)
                        
        # Create layout
        pos = nx.spring_layout(G, k=2, iterations=50)
        
        # Setup plot
        plt.figure(figsize=(12, 8))
        plt.title("Framework Comparison", color=self.colors["text"], pad=20)
        
        # Draw nodes
        nx.draw_networkx_nodes(G, pos,
            node_color=self.colors["node"],
            node_size=2000,
            alpha=0.7)
            
        # Draw edges with varying thickness based on shared concepts
        edges = G.edges(data=True)
        weights = [d['weight'] * 2 for _, _, d in edges]
        nx.draw_networkx_edges(G, pos,
            width=weights,
            edge_color=self.colors["edge"],
            alpha=0.5)
            
        # Add labels
        nx.draw_networkx_labels(G, pos,
            font_size=8,
            font_color=self.colors["text"])
            
        # Add edge labels
        edge_labels = nx.get_edge_attributes(G, 'concept')
        nx.draw_networkx_edge_labels(G, pos,
            edge_labels=edge_labels,
            font_size=6,
            font_color=self.colors["text"])
            
        # Save or show
        plt.tight_layout()
        if output_path:
            plt.savefig(output_path,
                       facecolor=self.colors["background"],
                       edgecolor='none',
                       bbox_inches='tight',
                       dpi=300)
            plt.close()
        else:
            plt.show()
            
    def create_framework_report(self,
                              framework: MetaphoricalFramework,
                              concepts: List[str],
                              output_dir: str) -> None:
        """Create a complete visual report for a framework"""
        # Create output directory
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Generate visualizations
        self.visualize_framework(
            framework,
            output_path=str(output_path / "framework_structure.png"),
            title=f"Framework Structure: {framework.name}"
        )
        
        self.visualize_framework_evolution(
            framework,
            concepts,
            output_path=str(output_path / "framework_evolution.png")
        )
        
        # Generate JSON report
        report = {
            "framework": {
                "name": framework.name,
                "core_metaphor": framework.core_metaphor,
                "elements": framework.elements,
                "mappings": framework.mappings
            },
            "analysis": {
                "total_elements": len(framework.elements),
                "total_mappings": len(framework.mappings),
                "concepts_analyzed": len(concepts)
            }
        }
        
        with open(output_path / "framework_report.json", 'w') as f:
            json.dump(report, f, indent=2)
            
        # Create HTML report
        html_report = f"""
        <html>
        <head>
            <title>Framework Analysis: {framework.name}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background: {self.colors["background"]};
                    color: {self.colors["text"]};
                }}
                img {{
                    max-width: 100%;
                    height: auto;
                    margin: 20px 0;
                }}
                .section {{
                    margin: 40px 0;
                }}
                pre {{
                    background: #1a1a1a;
                    padding: 15px;
                    border-radius: 5px;
                    overflow-x: auto;
                }}
            </style>
        </head>
        <body>
            <h1>Framework Analysis: {framework.name}</h1>
            
            <div class="section">
                <h2>Framework Structure</h2>
                <img src="framework_structure.png" alt="Framework Structure">
            </div>
            
            <div class="section">
                <h2>Framework Evolution</h2>
                <img src="framework_evolution.png" alt="Framework Evolution">
            </div>
            
            <div class="section">
                <h2>Framework Details</h2>
                <pre>{json.dumps(report, indent=2)}</pre>
            </div>
        </body>
        </html>
        """
        
        with open(output_path / "framework_report.html", 'w') as f:
            f.write(html_report)