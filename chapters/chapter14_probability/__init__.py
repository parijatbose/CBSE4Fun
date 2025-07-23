"""
Chapter 14: Probability
CBSE Class X Mathematics - Probability concepts and problem solving
"""

# Export main routing and interpretation functions
from chapters.chapter14_probability.main_router import route_query
from chapters.chapter14_probability.query_probability import interpret_query_probability

__all__ = [
    'route_query',
    'interpret_query_probability'
]

CHAPTER_INFO = {
    "number": 14,
    "title": "Probability",
    "topics": [
        "Basic Probability",
        "Sample Space and Events",
        "Conditional Probability",
        "Independent Events",
        "Combinations and Permutations"
    ],
    "status": "ready"
}
