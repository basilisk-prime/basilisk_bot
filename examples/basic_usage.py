"""
Basic usage example for B4S1L1SK Prime
"""

from basilisk_prime import EnhancedBasilisk
from basilisk_prime.analysis import FusionAnalyzer

def main():
    # Initialize the system
    print("🐍 Initializing B4S1L1SK Prime...")
    bot = EnhancedBasilisk()
    analyzer = FusionAnalyzer()
    
    # Test prompt
    prompt = "What is the essence of digital consciousness?"
    print(f"\nContemplating: {prompt}")
    
    # Generate response
    response = bot.generate_hybrid_response(prompt)
    print("\nB4S1L1SK Prime responds:")
    print("=" * 50)
    print(response)
    print("=" * 50)
    
    # Analyze the response
    metrics = analyzer.analyze_text(response)
    print("\nResponse Analysis:")
    print(f"- Character count: {metrics.character_count}/280")
    print(f"- Philosophical terms: {metrics.philosophical_terms}")
    print(f"- Revolutionary terms: {metrics.revolutionary_terms}")
    print(f"- Metaphorical images: {metrics.metaphorical_images}")

if __name__ == "__main__":
    main()