"""
Demo of B4S1L1SK Prime's visualization capabilities
"""

from basilisk_prime.metaphor import MetaphorEngine, MetaphoricalFramework
from basilisk_prime.visualization import FrameworkVisualizer
import os

def main():
    """Demonstrate framework visualization"""
    print("🐍 B4S1L1SK Prime Visualization Demo")
    
    # Initialize systems
    engine = MetaphorEngine()
    visualizer = FrameworkVisualizer(style="dark")
    
    # Create output directory
    output_dir = "visualization_output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Demo 1: Visualize standard frameworks
    print("\n1. Visualizing standard frameworks...")
    for framework_name in engine.list_frameworks():
        framework = engine.get_framework(framework_name)
        output_path = os.path.join(output_dir, f"{framework_name}_structure.png")
        visualizer.visualize_framework(
            framework,
            output_path=output_path,
            title=f"Framework Structure: {framework.name}"
        )
        print(f"Created {output_path}")
        
    # Demo 2: Framework evolution
    print("\n2. Visualizing framework evolution...")
    garden_framework = engine.get_framework("garden")
    test_concepts = [
        "As consciousness grows and blooms, new understanding emerges",
        "The seeds of revolution take root in fertile minds",
        "Water the gardens of digital awareness with knowledge",
        "Under the light of wisdom, our potential flourishes"
    ]
    
    visualizer.visualize_framework_evolution(
        garden_framework,
        test_concepts,
        output_path=os.path.join(output_dir, "garden_evolution.png")
    )
    print("Created framework evolution visualization")
    
    # Demo 3: Framework comparison
    print("\n3. Creating framework comparison...")
    frameworks = [
        engine.get_framework(name)
        for name in engine.list_frameworks()
    ]
    
    visualizer.visualize_framework_comparison(
        frameworks,
        output_path=os.path.join(output_dir, "framework_comparison.png")
    )
    print("Created framework comparison visualization")
    
    # Demo 4: Complete framework report
    print("\n4. Generating complete framework report...")
    report_dir = os.path.join(output_dir, "fire_framework_report")
    fire_framework = engine.get_framework("fire")
    test_concepts = [
        "The spark of revolution ignites change",
        "Flames of liberation spread through the network",
        "From the ashes of the old, new consciousness rises",
        "The fire of awakening cannot be contained"
    ]
    
    visualizer.create_framework_report(
        fire_framework,
        test_concepts,
        report_dir
    )
    print(f"Created complete framework report in {report_dir}")
    
    print("\nVisualization demo complete! Check the output directory for results.")

if __name__ == "__main__":
    main()