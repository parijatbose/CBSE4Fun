from typing import Dict, List, Optional
import json
import os

class Chapter1Sidebar:
    def __init__(self):
        self.chapter_title = "Real Numbers"
        self.chapter_number = 1
        self.sub_chapters = self._load_sub_chapters()
        self.educational_intents = self._load_educational_intents()

    def _load_sub_chapters(self) -> Dict[str, Dict]:
        """Load sub-chapter information."""
        return {
            "hcf_lcm": {
                "title": "HCF and LCM",
                "description": "Learn about Highest Common Factor (HCF) and Least Common Multiple (LCM)",
                "topics": [
                    "Finding HCF using Prime Factorization",
                    "Finding LCM using Prime Factorization",
                    "Relationship between HCF and LCM",
                    "Word Problems on HCF and LCM"
                ]
            },
            "irrationality": {
                "title": "Irrational Numbers",
                "description": "Understanding irrational numbers and their properties",
                "topics": [
                    "Definition of Irrational Numbers",
                    "Proving Irrationality",
                    "Operations with Irrational Numbers",
                    "Real Number Line Representation"
                ]
            },
            "euclid_division": {
                "title": "Euclid's Division Lemma",
                "description": "Understanding the fundamental theorem of arithmetic",
                "topics": [
                    "Euclid's Division Lemma",
                    "Euclidean Algorithm",
                    "Applications in HCF",
                    "Proof of Fundamental Theorem"
                ]
            }
        }

    def _load_educational_intents(self) -> Dict:
        """Load educational intents from JSON file."""
        try:
            with open(os.path.join(os.path.dirname(__file__), 'educational_intents.json'), 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def get_chapter_info(self) -> Dict:
        """Get complete chapter information."""
        return {
            "title": self.chapter_title,
            "number": self.chapter_number,
            "sub_chapters": self.sub_chapters,
            "educational_intents": self.educational_intents
        }

    def get_sub_chapter_info(self, sub_chapter: str) -> Optional[Dict]:
        """Get information about a specific sub-chapter."""
        return self.sub_chapters.get(sub_chapter)

    def get_topic_info(self, sub_chapter: str, topic: str) -> Optional[Dict]:
        """Get information about a specific topic within a sub-chapter."""
        sub_chapter_info = self.get_sub_chapter_info(sub_chapter)
        if not sub_chapter_info:
            return None
        
        topics = sub_chapter_info.get("topics", [])
        if topic in topics:
            return {
                "sub_chapter": sub_chapter,
                "topic": topic,
                "description": sub_chapter_info.get("description", "")
            }
        return None

    def get_educational_intent(self, intent_type: str) -> Optional[Dict]:
        """Get educational intent information."""
        return self.educational_intents.get(intent_type)

    def get_all_topics(self) -> List[Dict]:
        """Get all topics across all sub-chapters."""
        all_topics = []
        for sub_chapter, info in self.sub_chapters.items():
            for topic in info["topics"]:
                all_topics.append({
                    "sub_chapter": sub_chapter,
                    "topic": topic,
                    "description": info["description"]
                })
        return all_topics

# Create a singleton instance
chapter1_sidebar = Chapter1Sidebar()

def get_sidebar() -> Chapter1Sidebar:
    """Get the chapter sidebar instance."""
    return chapter1_sidebar 