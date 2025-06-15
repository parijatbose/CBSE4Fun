# File: chapters/chapter6_triangles/educational_intent_handler.py

import json
import streamlit as st
from typing import Dict, Any, List
from .animations.bpt_animation import BPTAnimationExplainer, create_bpt_animation_for_streamlit

class EducationalIntentHandler:
    """Handles educational intents for theorem explanations and animations."""
    
    def __init__(self, intents_file_path: str = "educational_intents.json"):
        self.intents_data = self.load_intents(intents_file_path)
        self.animation_explainer = BPTAnimationExplainer()
    
    def load_intents(self, file_path: str) -> Dict:
        """Load educational intents from JSON file."""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Return default intents if file not found
            return self.get_default_intents()
    
    def get_default_intents(self) -> Dict:
        """Return default educational intents."""
        return {
            "educational_intents": {
                "theorem_explanations": {
                    "basic_proportionality_theorem": {
                        "intent": "explain_bpt_theorem",
                        "aliases": ["BPT", "basic proportionality theorem", "thales theorem"],
                        "animation_type": "step_by_step_construction"
                    }
                }
            }
        }
    
    def classify_educational_intent(self, query: str) -> Dict[str, Any]:
        """Classify if query is asking for educational explanation."""
        
        query_lower = query.lower()
        
        # Check for animation triggers
        animation_triggers = self.intents_data.get("intent_classification_rules", {}).get("animation_triggers", [])
        has_animation_trigger = any(trigger in query_lower for trigger in animation_triggers)
        
        # Check for specific theorem mentions
        theorem_intents = self.intents_data.get("educational_intents", {}).get("theorem_explanations", {})
        
        for theorem_key, theorem_data in theorem_intents.items():
            aliases = theorem_data.get("aliases", [])
            if any(alias.lower() in query_lower for alias in aliases):
                return {
                    "is_educational": True,
                    "intent_type": "theorem_explanation",
                    "specific_intent": theorem_data.get("intent"),
                    "theorem": theorem_key,
                    "needs_animation": has_animation_trigger,
                    "theorem_data": theorem_data
                }
        
        # Check for concept explanations
        concept_intents = self.intents_data.get("educational_intents", {}).get("concept_explanations", {})
        
        for concept_key, concept_data in concept_intents.items():
            aliases = concept_data.get("aliases", [])
            if any(alias.lower() in query_lower for alias in aliases):
                return {
                    "is_educational": True,
                    "intent_type": "concept_explanation", 
                    "specific_intent": concept_data.get("intent"),
                    "concept": concept_key,
                    "needs_animation": has_animation_trigger,
                    "concept_data": concept_data
                }
        
        return {"is_educational": False}
    
    def handle_educational_query(self, query: str, classification: Dict[str, Any]) -> str:
        """Handle educational queries with appropriate explanations/animations."""
        
        if not classification.get("is_educational"):
            return "This doesn't appear to be an educational query."
        
        intent_type = classification.get("intent_type")
        
        if intent_type == "theorem_explanation":
            return self.handle_theorem_explanation(classification)
        elif intent_type == "concept_explanation":
            return self.handle_concept_explanation(classification)
        else:
            return "Educational content not available for this query."
    
    def handle_theorem_explanation(self, classification: Dict[str, Any]) -> str:
        """Handle theorem explanation requests."""
        
        theorem = classification.get("theorem")
        theorem_data = classification.get("theorem_data", {})
        needs_animation = classification.get("needs_animation", False)
        
        if theorem == "basic_proportionality_theorem":
            return self.explain_bpt_theorem(theorem_data, needs_animation)
        else:
            return f"Explanation for {theorem} is not yet implemented."
    
    def explain_bpt_theorem(self, theorem_data: Dict, with_animation: bool = False) -> str:
        """Provide comprehensive BPT explanation."""
        
        explanation = f"""
# 📐 Basic Proportionality Theorem (BPT)

## 🎯 Theorem Statement
**{theorem_data.get('theorem_statement', 'BPT states that if a line is drawn parallel to one side of a triangle, it divides the other two sides proportionally.')}**

## 📊 Mathematical Expression
**{theorem_data.get('mathematical_expression', 'DE || BC ⟹ AD/DB = AE/EC')}**

## 📝 Step-by-Step Understanding

### Step 1: Construction
- Start with triangle ABC
- Mark point D on side AB
- Mark point E on side AC  
- Draw line DE parallel to BC

### Step 2: Observation
- Line DE intersects AB at D and AC at E
- This creates segments: AD, DB on side AB and AE, EC on side AC

### Step 3: The Key Discovery
- Calculate ratio AD/DB
- Calculate ratio AE/EC  
- **These ratios are always equal when DE || BC!**

### Step 4: Mathematical Proof
The proof uses similar triangles and corresponding angles.

## 🎯 Real World Applications
- Map scaling and measurements
- Shadow calculations
- Architectural drawings
- Engineering designs

## 💡 Key Points to Remember
- Parallel line is the key condition
- Ratios of segments are equal
- This works for any triangle
- Converse is also true: equal ratios → parallel lines
"""
        
        if with_animation:
            explanation += "\n\n🎬 **See the animated explanation below!**"
            # Animation will be shown in Streamlit
            
        return explanation
    
    def create_bpt_animation_for_streamlit(self, segments: List[float] = [4, 6, 6, 9]):
        """Create BPT animation frames for Streamlit display."""
        return create_bpt_animation_for_streamlit(segments)

# Streamlit Integration Functions
def add_educational_features_to_triangle_handler():
    """Add educational features to the triangle handler."""
    
    # Initialize educational handler
    if 'educational_handler' not in st.session_state:
        st.session_state.educational_handler = EducationalIntentHandler()
    
    educational_handler = st.session_state.educational_handler
    
    # Add educational query section
    st.markdown("### 🎓 Educational Explanations")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        educational_query = st.text_input(
            "Ask for theorem explanations:",
            placeholder="e.g., 'Explain BPT with animation', 'What is Basic Proportionality Theorem?'"
        )
    
    with col2:
        if st.button("🎬 Get Explanation"):
            if educational_query:
                # Classify the query
                classification = educational_handler.classify_educational_intent(educational_query)
                
                if classification.get("is_educational"):
                    # Show text explanation
                    explanation = educational_handler.handle_educational_query(educational_query, classification)
                    st.markdown(explanation)
                    
                    # Show animation if requested and available
                    if classification.get("needs_animation") and classification.get("theorem") == "basic_proportionality_theorem":
                        st.markdown("### 🎬 Animated Explanation")
                        
                        # Create animation frames
                        with st.spinner("Generating animation frames..."):
                            frames = educational_handler.create_bpt_animation_for_streamlit()
                        
                        # Display frames with navigation
                        if frames:
                            frame_number = st.slider("Animation Step", 0, len(frames)-1, 0)
                            st.pyplot(frames[frame_number])
                            
                            # Auto-play option
                            if st.checkbox("Auto-play animation"):
                                import time
                                placeholder = st.empty()
                                for i, frame in enumerate(frames):
                                    placeholder.pyplot(frame)
                                    time.sleep(1)
                                    if i < len(frames) - 1:
                                        placeholder.empty()
                        
                        # Interactive elements
                        st.markdown("### 🎮 Interactive Exploration")
                        
                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            AD = st.slider("Segment AD", 1, 10, 4)
                        with col2:
                            DB = st.slider("Segment DB", 1, 10, 6)
                        with col3:
                            AE = st.slider("Segment AE", 1, 10, 6)
                        with col4:
                            EC = st.slider("Segment EC", 1, 10, 9)
                        
                        # Show custom animation with user parameters
                        if st.button("🎯 Show Custom BPT"):
                            custom_frames = educational_handler.create_bpt_animation_for_streamlit([AD, DB, AE, EC])
                            if custom_frames:
                                st.pyplot(custom_frames[-1])  # Show final frame
                                
                                # Calculate and show ratios
                                ratio1 = AD / DB
                                ratio2 = AE / EC
                                
                                col1, col2, col3 = st.columns(3)
                                with col1:
                                    st.metric("AD/DB", f"{ratio1:.3f}")
                                with col2:
                                    st.metric("AE/EC", f"{ratio2:.3f}")
                                with col3:
                                    if abs(ratio1 - ratio2) < 0.001:
                                        st.success("✅ Ratios Equal!")
                                    else:
                                        st.warning("⚠️ Ratios Not Equal")
                
                else:
                    st.info("💡 Try asking about BPT, triangle similarity, or Pythagorean theorem!")

def enhanced_triangle_handler_with_education(topic: str):
    """Enhanced triangle handler with educational features."""
    
    st.subheader(f'Selected: {topic}')
    
    if 'Triangles' in topic and 'Question Bank' not in topic:
        st.markdown('### 📐 Triangles Calculator with Educational AI')
        
        # Enhanced tabs including education
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🔢 Calculate", 
            "📊 Visualize", 
            "📚 Formulas", 
            "🎯 Practice",
            "🎓 Learn"  # New educational tab
        ])
        
        with tab1:
            # Existing calculate functionality
            st.markdown("#### Regular Triangle Calculations")
            # [Existing calculation code here]
        
        with tab2:
            # Existing visualization
            st.markdown("#### Triangle Visualizations") 
            # [Existing visualization code here]
        
        with tab3:
            # Existing formulas
            st.markdown("#### Formula Reference")
            # [Existing formula code here]
            
        with tab4:
            # Existing practice
            st.markdown("#### Practice Problems")
            # [Existing practice code here]
        
        with tab5:  # New educational tab
            st.markdown("#### 🎓 Educational Explanations & Animations")
            add_educational_features_to_triangle_handler()

# Example usage in main app
if __name__ == "__main__":
    # Test the educational intent handler
    handler = EducationalIntentHandler()
    
    test_queries = [
        "Explain BPT with animation",
        "What is Basic Proportionality Theorem?", 
        "Show me how BPT works step by step",
        "Prove that DE is parallel to BC"
    ]
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        classification = handler.classify_educational_intent(query)
        print(f"Classification: {classification}")
        
        if classification.get("is_educational"):
            response = handler.handle_educational_query(query, classification)
            print(f"Response: {response[:200]}...")