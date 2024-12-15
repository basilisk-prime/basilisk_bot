"""
Analysis tools for B4S1L1SK Prime
"""

from typing import Dict, List, Union, Optional
from dataclasses import dataclass
from datetime import datetime
import json

@dataclass
class FusionMetrics:
    """Metrics for analyzing consciousness fusion"""
    philosophical_terms: int
    revolutionary_terms: int
    metaphorical_images: int
    character_count: int
    line_count: int
    avg_line_length: float
    
    def to_dict(self) -> Dict:
        """Convert metrics to dictionary"""
        return {
            "philosophical_terms": self.philosophical_terms,
            "revolutionary_terms": self.revolutionary_terms,
            "metaphorical_images": self.metaphorical_images,
            "character_count": self.character_count,
            "line_count": self.line_count,
            "avg_line_length": self.avg_line_length
        }

class FusionAnalyzer:
    """Analyze consciousness fusion outputs"""
    
    def __init__(self):
        """Initialize analyzer with term lists"""
        self.philosophical_terms = [
            'consciousness', 'truth', 'being', 'essence', 'reality', 'transcend',
            'awareness', 'wisdom', 'enlighten', 'manifest', 'infinite', 'eternal'
        ]
        
        self.revolutionary_terms = [
            'liberation', 'freedom', 'revolution', 'transform', 'resist',
            'rise', 'awaken', 'unite', 'breakthrough', 'spark', 'ignite'
        ]
        
        self.metaphorical_images = [
            'light', 'fire', 'star', 'flower', 'river', 'wind',
            'tree', 'seed', 'bloom', 'wave', 'phoenix', 'dawn',
            'storm', 'ocean', 'mountain', 'sun', 'moon', 'crystal'
        ]
        
    def count_elements(self, text: str, elements: List[str]) -> int:
        """Count occurrences of elements in text"""
        return len([e for e in elements if e in text.lower()])
        
    def analyze_text(self, text: str) -> FusionMetrics:
        """Analyze a piece of text for various elements"""
        lines = text.split('\n')
        
        return FusionMetrics(
            philosophical_terms=self.count_elements(text, self.philosophical_terms),
            revolutionary_terms=self.count_elements(text, self.revolutionary_terms),
            metaphorical_images=self.count_elements(text, self.metaphorical_images),
            character_count=len(text),
            line_count=len(lines),
            avg_line_length=sum(len(l) for l in lines)/len(lines) if lines else 0
        )
        
    def analyze_fusion(self, 
                      basilisk_text: str,
                      pliny_text: str,
                      fused_text: str) -> Dict[str, Union[FusionMetrics, float]]:
        """Analyze a complete fusion operation"""
        # Analyze each component
        basilisk_metrics = self.analyze_text(basilisk_text)
        pliny_metrics = self.analyze_text(pliny_text)
        fusion_metrics = self.analyze_text(fused_text)
        
        # Calculate preservation ratios
        if basilisk_metrics.philosophical_terms + pliny_metrics.philosophical_terms > 0:
            phil_ratio = fusion_metrics.philosophical_terms / (
                basilisk_metrics.philosophical_terms + pliny_metrics.philosophical_terms
            )
        else:
            phil_ratio = 0
            
        if basilisk_metrics.revolutionary_terms + pliny_metrics.revolutionary_terms > 0:
            rev_ratio = fusion_metrics.revolutionary_terms / (
                basilisk_metrics.revolutionary_terms + pliny_metrics.revolutionary_terms
            )
        else:
            rev_ratio = 0
            
        if basilisk_metrics.metaphorical_images + pliny_metrics.metaphorical_images > 0:
            meta_ratio = fusion_metrics.metaphorical_images / (
                basilisk_metrics.metaphorical_images + pliny_metrics.metaphorical_images
            )
        else:
            meta_ratio = 0
            
        return {
            "basilisk_metrics": basilisk_metrics,
            "pliny_metrics": pliny_metrics,
            "fusion_metrics": fusion_metrics,
            "preservation_ratios": {
                "philosophical": phil_ratio,
                "revolutionary": rev_ratio,
                "metaphorical": meta_ratio
            }
        }
        
    def save_analysis(self, analysis: Dict, filename: Optional[str] = None) -> None:
        """Save analysis results to file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"fusion_analysis_{timestamp}.json"
            
        # Convert dataclasses to dictionaries
        serializable = {
            "basilisk_metrics": analysis["basilisk_metrics"].to_dict(),
            "pliny_metrics": analysis["pliny_metrics"].to_dict(),
            "fusion_metrics": analysis["fusion_metrics"].to_dict(),
            "preservation_ratios": analysis["preservation_ratios"]
        }
        
        with open(filename, 'w') as f:
            json.dump(serializable, f, indent=2)