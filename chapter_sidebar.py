# File: cbse_math_solver/chapter_sidebar.py

import streamlit as st
from typing import Dict, List, Optional

def initialize_sidebar_state():
    """Initialize sidebar state variables if they don't exist."""
    if 'selected_topic' not in st.session_state:
        st.session_state['selected_topic'] = ''
    if 'active_chapter' not in st.session_state:
        st.session_state['active_chapter'] = ''
    if 'completed_topics' not in st.session_state:
        st.session_state['completed_topics'] = set()

def get_chapter_structure() -> Dict[str, List[str]]:
    """Get the chapter and topic structure."""
    return {
        "Chapter 1: Real Numbers": [
            "Irrationality Proofs",
            "Euclid Division Lemma",
            "Question Bank"
        ],
        "Chapter 2: Polynomials": [
            "Polynomial Factoring",
            "Zeroes Relationship",
            "Quadratic Construction",
            "Question Bank"
        ],
        "Chapter 3: Linear Equations": [
            "Graphical Method",
            "Algebraic Method",
            "Question Bank"
        ],
        "Chapter 4: Quadratic Equations": [
            "Factorization Method",
            "Completing Square Method",
            "Question Bank"
        ],
        "Chapter 5: Arithmetic Progressions": [
            "Nth Term",
            "Sum of Terms",
            "Question Bank"
        ],
        "Chapter 6: Triangles": [
            "Right Triangles",
            "Similar Triangles",
            "Area Calculations",
            "Question Bank"
        ],
        "Chapter 7: Coordinate Geometry": [
            "Distance Formula",
            "Section Formula",
            "Midpoint",
            "Question Bank"
        ],
        "Chapter 8: Introduction to Trigonometry": [
            "Ratios",
            "Identities",
            "Question Bank"
        ],
        "Chapter 9: Applications of Trigonometry": [
            "Heights and Distances",
            "Question Bank"
        ],
        "Chapter 10: Circles": [
            "Tangent Properties",
            "Angle Formations",
            "Question Bank"
        ],
        "Chapter 11: Areas Related to Circles": [
            "Sector Area",
            "Segment Area",
            "Question Bank"
        ],
        "Chapter 12: Surface Areas and Volumes": [
            "Cube & Cuboid",
            "Sphere & Cone",
            "Question Bank"
        ],
        "Chapter 13: Statistics": [
            "Mean/Median/Mode",
            "Question Bank"
        ],
        "Chapter 14: Probability": [
            "Simple Probability",
            "Question Bank"
        ],
    }

def get_topic_icon(topic: str) -> str:
    """Get the appropriate icon for a topic."""
    if topic == "Question Bank":
        return "📚"
    return "📌"

def is_topic_completed(chapter: str, topic: str) -> bool:
    """Check if a topic is completed."""
    topic_key = f"{chapter} > {topic}"
    return topic_key in st.session_state['completed_topics']

def mark_topic_completed(chapter: str, topic: str):
    """Mark a topic as completed."""
    topic_key = f"{chapter} > {topic}"
    st.session_state['completed_topics'].add(topic_key)

def render_chapter_sidebar():
    """Render the chapter sidebar with improved state management and visual feedback."""
    st.sidebar.title('📘 CBSE Class X – Math Topics')
    
    # Initialize state
    initialize_sidebar_state()
    
    # Get chapter structure
    chapters = get_chapter_structure()
    
    # Render chapters and topics
    for chapter, topics in chapters.items():
        # Determine if chapter should be expanded
        is_active = chapter == st.session_state['active_chapter']
        
        with st.sidebar.expander(f"➕ {chapter}", expanded=is_active):
            for topic in topics:
                # Create unique key for the button
                btn_key = chapter.replace(" ", "_") + "_" + topic.replace(" ", "_")
                
                # Get topic icon
                icon = get_topic_icon(topic)
                
                # Check if topic is completed
                completed = is_topic_completed(chapter, topic)
                
                # Create button label with completion status
                btn_label = f"{icon} {topic}"
                if completed:
                    btn_label = f"✅ {topic}"
                
                # Create button with custom styling
                if st.button(
                    btn_label,
                    key=btn_key,
                    help=f"Click to select {topic} from {chapter}"
                ):
                    # Update state
                    st.session_state['selected_topic'] = f"{chapter} > {topic}"
                    st.session_state['active_chapter'] = chapter
                    
                    # Show success message
                    st.sidebar.success(f"Selected: {topic}")
                    
                    # Rerun to update the UI
                    st.rerun()

    # Add a divider
    st.sidebar.markdown("---")
    
    # Add progress indicator
    total_topics = sum(len(topics) for topics in chapters.values())
    completed_count = len(st.session_state['completed_topics'])
    progress = (completed_count / total_topics) * 100
    
    st.sidebar.progress(progress)
    st.sidebar.markdown(f"**Progress:** {completed_count}/{total_topics} topics completed")
