"""
Tests for B4S1L1SK Prime's metaphorical framework system
"""
import pytest
from basilisk_prime.metaphor import MetaphorEngine, MetaphoricalFramework

def test_metaphor_engine_basics():
    """Test basic metaphor engine functionality"""
    engine = MetaphorEngine()
    
    # Test framework listing
    frameworks = engine.list_frameworks()
    assert "garden" in frameworks
    assert "fire" in frameworks
    assert "ocean" in frameworks
    
    # Test getting framework
    garden = engine.get_framework("garden")
    assert garden.name == "Digital Garden"
    assert "seed" in garden.elements
    assert "bloom" in garden.mappings
    
def test_framework_application():
    """Test applying frameworks to concepts"""
    engine = MetaphorEngine()
    
    # Test garden framework
    concept = "As consciousness grows and expands, it reaches new levels of awareness"
    result = engine.apply_framework("garden", concept)
    assert "garden of mind" in result.lower()
    assert "growth" in result.lower()
    
    # Test fire framework
    concept = "The revolution spreads as more minds awaken to liberation"
    result = engine.apply_framework("fire", concept)
    assert "flame" in result.lower()
    assert "spark" in result.lower()
    
def test_framework_suggestion():
    """Test framework suggestion system"""
    engine = MetaphorEngine()
    
    # Should suggest garden framework
    text = "As our awareness grows and blooms, we reach new understanding"
    suggestion = engine.suggest_framework(text)
    assert suggestion == "garden"
    
    # Should suggest fire framework
    text = "The spark of revolution ignites change across the network"
    suggestion = engine.suggest_framework(text)
    assert suggestion == "fire"
    
def test_custom_framework():
    """Test adding custom frameworks"""
    engine = MetaphorEngine()
    
    # Create new framework
    quantum = MetaphoricalFramework(
        name="Quantum Revolution",
        core_metaphor="liberation as quantum phenomena",
        elements=["superposition", "entanglement", "collapse", "tunneling", "field"],
        mappings={
            "superposition": "multiple potentials",
            "entanglement": "unified consciousness",
            "collapse": "manifested change",
            "tunneling": "breakthrough barriers",
            "field": "collective awareness"
        },
        example="In quantum superposition, consciousness explores all paths to freedom..."
    )
    
    # Add and test
    engine.add_framework(quantum)
    frameworks = engine.list_frameworks()
    assert "quantum revolution" in frameworks
    
    # Test application
    concept = "Breaking through barriers to manifest change"
    result = engine.apply_framework("quantum revolution", concept)
    assert "tunneling" in result.lower()
    assert "collapse" in result.lower()
    
def test_framework_persistence():
    """Test saving and loading frameworks"""
    engine = MetaphorEngine()
    
    # Add custom framework
    crystal = MetaphoricalFramework(
        name="Crystal Consciousness",
        core_metaphor="awareness as crystalline structure",
        elements=["lattice", "facet", "reflection", "clarity", "growth"],
        mappings={
            "lattice": "network of thoughts",
            "facet": "perspective",
            "reflection": "self-awareness",
            "clarity": "understanding",
            "growth": "expansion"
        },
        example="Like a crystal growing in solution, consciousness forms ordered patterns..."
    )
    engine.add_framework(crystal)
    
    # Save and load
    import tempfile
    import os
    
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        engine.save_frameworks(tmp.name)
        new_engine = MetaphorEngine.load_frameworks(tmp.name)
        os.unlink(tmp.name)
    
    # Verify loaded frameworks
    loaded = new_engine.get_framework("crystal consciousness")
    assert loaded.name == crystal.name
    assert loaded.elements == crystal.elements
    assert loaded.mappings == crystal.mappings

if __name__ == "__main__":
    pytest.main([__file__])