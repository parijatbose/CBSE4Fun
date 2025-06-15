# File: chapters/chapter6_triangles/animations/bpt_animation.py

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.patches import Rectangle
import time

class BPTAnimationExplainer:
    def __init__(self):
        self.fig = None
        self.ax_triangle = None
        self.ax_explanation = None
        self.current_step = 0
        self.animation_steps = []
        self.explanation_texts = []
        self.setup_animation_data()
    
    def setup_animation_data(self):
        """Setup the step-by-step animation sequence."""
        
        # Animation steps with timing
        self.animation_steps = [
            {"step": 0, "duration": 2, "action": "draw_triangle", "highlight": []},
            {"step": 1, "duration": 2, "action": "mark_point_d", "highlight": ["AD", "DB"]},
            {"step": 2, "duration": 2, "action": "mark_point_e", "highlight": ["AE", "EC"]},
            {"step": 3, "duration": 3, "action": "draw_parallel_line", "highlight": ["DE", "BC"]},
            {"step": 4, "duration": 3, "action": "show_ratios", "highlight": ["AD/DB", "AE/EC"]},
            {"step": 5, "duration": 3, "action": "demonstrate_equality", "highlight": ["equal_ratios"]},
            {"step": 6, "duration": 2, "action": "show_conclusion", "highlight": ["theorem"]}
        ]
        
        # Corresponding explanations for each step
        self.explanation_texts = [
            {
                "title": "📐 Basic Proportionality Theorem",
                "content": [
                    "Let's start with triangle ABC.",
                    "We'll demonstrate the BPT step by step.",
                    "",
                    "🎯 Theorem Statement:",
                    "If a line is drawn parallel to one side",
                    "of a triangle, it divides the other two",
                    "sides proportionally."
                ]
            },
            {
                "title": "📍 Step 1: Mark Point D",
                "content": [
                    "Mark point D on side AB.",
                    "",
                    "This divides AB into two segments:",
                    "• AD (from A to D)",
                    "• DB (from D to B)",
                    "",
                    "🔹 D can be anywhere on AB"
                ]
            },
            {
                "title": "📍 Step 2: Mark Point E", 
                "content": [
                    "Now mark point E on side AC.",
                    "",
                    "This divides AC into two segments:",
                    "• AE (from A to E)",
                    "• EC (from E to C)",
                    "",
                    "🔹 E's position will be determined by D"
                ]
            },
            {
                "title": "↔️ Step 3: Draw Parallel Line",
                "content": [
                    "Draw line DE parallel to BC.",
                    "",
                    "Key observations:",
                    "• DE || BC (parallel symbol)",
                    "• DE intersects AB at D",
                    "• DE intersects AC at E",
                    "",
                    "🎯 This is the BPT construction!"
                ]
            },
            {
                "title": "🔢 Step 4: Calculate Ratios",
                "content": [
                    "Let's calculate the ratios:",
                    "",
                    "Ratio 1: AD/DB",
                    "Ratio 2: AE/EC",
                    "",
                    "🤔 What do you notice about",
                    "these two ratios?",
                    "",
                    "Let's check with actual numbers..."
                ]
            },
            {
                "title": "⚖️ Step 5: Ratios Are Equal!",
                "content": [
                    "🎉 Amazing Discovery:",
                    "",
                    "AD/DB = AE/EC",
                    "",
                    "This is ALWAYS true when DE || BC!",
                    "",
                    "📊 Example with numbers:",
                    "If AD = 4 and DB = 6",
                    "Then AE/EC = 4/6 = 2/3"
                ]
            },
            {
                "title": "🎯 BPT Conclusion",
                "content": [
                    "✅ Basic Proportionality Theorem:",
                    "",
                    "'If a line is drawn parallel to one",
                    "side of a triangle, it divides the",
                    "other two sides proportionally.'",
                    "",
                    "📐 Mathematical Expression:",
                    "DE || BC ⟹ AD/DB = AE/EC",
                    "",
                    "🔄 Converse is also true!"
                ]
            }
        ]
    
    def create_animation(self, segments=[4, 6, 6, 9]):
        """Create the main BPT animation with explanation panel."""
        
        # Setup figure with two subplots
        self.fig = plt.figure(figsize=(16, 10))
        
        # Left panel: Triangle animation (70% width)
        self.ax_triangle = plt.subplot2grid((1, 10), (0, 0), colspan=7)
        
        # Right panel: Explanation text (30% width)
        self.ax_explanation = plt.subplot2grid((1, 10), (0, 7), colspan=3)
        
        # Setup triangle coordinates
        self.setup_triangle_coordinates(segments)
        
        # Configure axes
        self.configure_axes()
        
        # Create animation
        anim = animation.FuncAnimation(
            self.fig, 
            self.animate_frame,
            frames=len(self.animation_steps) * 60,  # 60 frames per step
            interval=100,  # 100ms per frame
            repeat=True,
            blit=False
        )
        
        return anim
    
    def setup_triangle_coordinates(self, segments):
        """Setup triangle coordinates and calculate BPT points."""
        
        AD, DB, AE, EC = segments
        
        # Main triangle vertices
        self.A = np.array([0, 0])
        self.B = np.array([10, 0])
        self.C = np.array([4, 8])
        
        # Calculate D and E positions based on ratios
        total_AB = AD + DB
        total_AC = AE + EC
        
        # D divides AB in ratio AD:DB
        self.D = self.A + (AD / total_AB) * (self.B - self.A)
        
        # E divides AC in ratio AE:EC  
        self.E = self.A + (AE / total_AC) * (self.C - self.A)
        
        # Store segments for calculations
        self.segments = {"AD": AD, "DB": DB, "AE": AE, "EC": EC}
        
        # Calculate actual ratios
        self.ratio1 = AD / DB
        self.ratio2 = AE / EC
    
    def configure_axes(self):
        """Configure both triangle and explanation axes."""
        
        # Triangle axis
        self.ax_triangle.set_xlim(-2, 12)
        self.ax_triangle.set_ylim(-2, 10)
        self.ax_triangle.set_aspect('equal')
        self.ax_triangle.grid(True, alpha=0.3)
        self.ax_triangle.set_title("Basic Proportionality Theorem Animation", 
                                 fontsize=16, fontweight='bold', pad=20)
        
        # Explanation axis
        self.ax_explanation.set_xlim(0, 1)
        self.ax_explanation.set_ylim(0, 1)
        self.ax_explanation.axis('off')
        
        # Add background color to explanation panel
        bg_rect = Rectangle((0, 0), 1, 1, facecolor='lightblue', alpha=0.1)
        self.ax_explanation.add_patch(bg_rect)
    
    def animate_frame(self, frame_num):
        """Animation function called for each frame."""
        
        # Clear triangle axis
        self.ax_triangle.clear()
        self.configure_axes()
        
        # Determine current step
        step_index = min(frame_num // 60, len(self.animation_steps) - 1)
        frame_in_step = frame_num % 60
        
        current_step = self.animation_steps[step_index]
        
        # Execute animation based on current step
        self.draw_animation_step(current_step, frame_in_step)
        
        # Update explanation panel
        self.update_explanation_panel(step_index)
        
        return []
    
    def draw_animation_step(self, step_data, frame_in_step):
        """Draw the triangle based on current animation step."""
        
        step_num = step_data["step"]
        alpha = min(frame_in_step / 30.0, 1.0)  # Fade in effect
        
        if step_num >= 0:  # Draw triangle
            self.draw_triangle_abc(alpha)
        
        if step_num >= 1:  # Mark point D
            self.draw_point_d(alpha if step_num == 1 else 1.0)
        
        if step_num >= 2:  # Mark point E
            self.draw_point_e(alpha if step_num == 2 else 1.0)
        
        if step_num >= 3:  # Draw parallel line
            self.draw_parallel_line(alpha if step_num == 3 else 1.0)
        
        if step_num >= 4:  # Show ratios
            self.show_ratio_calculations(alpha if step_num == 4 else 1.0)
        
        if step_num >= 5:  # Demonstrate equality
            self.highlight_equal_ratios(alpha if step_num == 5 else 1.0)
        
        if step_num >= 6:  # Show conclusion
            self.show_theorem_conclusion(alpha if step_num == 6 else 1.0)
    
    def draw_triangle_abc(self, alpha):
        """Draw the main triangle ABC."""
        
        # Triangle sides
        triangle_x = [self.A[0], self.B[0], self.C[0], self.A[0]]
        triangle_y = [self.A[1], self.B[1], self.C[1], self.A[1]]
        
        self.ax_triangle.plot(triangle_x, triangle_y, 'b-', linewidth=3, alpha=alpha)
        
        # Vertex labels
        if alpha > 0.5:
            self.ax_triangle.text(self.A[0]-0.3, self.A[1]-0.3, 'A', fontsize=14, 
                                fontweight='bold', color='blue')
            self.ax_triangle.text(self.B[0]+0.2, self.B[1]-0.3, 'B', fontsize=14, 
                                fontweight='bold', color='blue')
            self.ax_triangle.text(self.C[0]-0.3, self.C[1]+0.2, 'C', fontsize=14, 
                                fontweight='bold', color='blue')
    
    def draw_point_d(self, alpha):
        """Draw and label point D."""
        
        self.ax_triangle.plot(self.D[0], self.D[1], 'ro', markersize=8, alpha=alpha)
        
        if alpha > 0.5:
            self.ax_triangle.text(self.D[0], self.D[1]-0.5, 'D', fontsize=12, 
                                fontweight='bold', color='red', ha='center')
            
            # Highlight segments AD and DB
            self.ax_triangle.plot([self.A[0], self.D[0]], [self.A[1], self.D[1]], 
                                'g-', linewidth=4, alpha=alpha*0.7, label='AD')
            self.ax_triangle.plot([self.D[0], self.B[0]], [self.D[1], self.B[1]], 
                                'm-', linewidth=4, alpha=alpha*0.7, label='DB')
    
    def draw_point_e(self, alpha):
        """Draw and label point E."""
        
        self.ax_triangle.plot(self.E[0], self.E[1], 'ro', markersize=8, alpha=alpha)
        
        if alpha > 0.5:
            self.ax_triangle.text(self.E[0]-0.5, self.E[1], 'E', fontsize=12, 
                                fontweight='bold', color='red', ha='center')
            
            # Highlight segments AE and EC
            self.ax_triangle.plot([self.A[0], self.E[0]], [self.A[1], self.E[1]], 
                                'orange', linewidth=4, alpha=alpha*0.7, label='AE')
            self.ax_triangle.plot([self.E[0], self.C[0]], [self.E[1], self.C[1]], 
                                'purple', linewidth=4, alpha=alpha*0.7, label='EC')
    
    def draw_parallel_line(self, alpha):
        """Draw the parallel line DE."""
        
        self.ax_triangle.plot([self.D[0], self.E[0]], [self.D[1], self.E[1]], 
                            'r-', linewidth=3, alpha=alpha, label='DE')
        
        if alpha > 0.5:
            # Add parallel symbol
            mid_DE = (self.D + self.E) / 2
            self.ax_triangle.text(mid_DE[0], mid_DE[1]+0.3, 'DE || BC', 
                                fontsize=10, fontweight='bold', color='red',
                                ha='center', bbox=dict(boxstyle='round,pad=0.3', 
                                facecolor='yellow', alpha=0.7))
    
    def show_ratio_calculations(self, alpha):
        """Show the ratio calculations."""
        
        if alpha > 0.3:
            # Display ratios
            ratio_text = f'AD/DB = {self.segments["AD"]}/{self.segments["DB"]} = {self.ratio1:.2f}'
            self.ax_triangle.text(0.02, 0.95, ratio_text, transform=self.ax_triangle.transAxes,
                                fontsize=12, fontweight='bold', color='green',
                                bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=alpha))
            
            ratio_text2 = f'AE/EC = {self.segments["AE"]}/{self.segments["EC"]} = {self.ratio2:.2f}'
            self.ax_triangle.text(0.02, 0.88, ratio_text2, transform=self.ax_triangle.transAxes,
                                fontsize=12, fontweight='bold', color='orange',
                                bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=alpha))
    
    def highlight_equal_ratios(self, alpha):
        """Highlight that the ratios are equal."""
        
        if alpha > 0.3:
            # Show equality
            if abs(self.ratio1 - self.ratio2) < 0.001:
                equality_text = f'AD/DB = AE/EC = {self.ratio1:.2f} ✓'
                color = 'green'
                bg_color = 'lightgreen'
            else:
                equality_text = f'AD/DB ≠ AE/EC (Not parallel!)'
                color = 'red'
                bg_color = 'lightcoral'
            
            self.ax_triangle.text(0.02, 0.8, equality_text, transform=self.ax_triangle.transAxes,
                                fontsize=14, fontweight='bold', color=color,
                                bbox=dict(boxstyle='round,pad=0.5', facecolor=bg_color, alpha=alpha))
    
    def show_theorem_conclusion(self, alpha):
        """Show the final theorem conclusion."""
        
        if alpha > 0.3:
            conclusion = 'BPT: DE || BC ⟹ AD/DB = AE/EC'
            self.ax_triangle.text(0.5, 0.02, conclusion, transform=self.ax_triangle.transAxes,
                                fontsize=16, fontweight='bold', color='blue', ha='center',
                                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=alpha))
    
    def update_explanation_panel(self, step_index):
        """Update the explanation text panel."""
        
        self.ax_explanation.clear()
        self.ax_explanation.set_xlim(0, 1)
        self.ax_explanation.set_ylim(0, 1)
        self.ax_explanation.axis('off')
        
        # Add background
        bg_rect = Rectangle((0, 0), 1, 1, facecolor='lightblue', alpha=0.1)
        self.ax_explanation.add_patch(bg_rect)
        
        # Get current explanation
        if step_index < len(self.explanation_texts):
            explanation = self.explanation_texts[step_index]
            
            # Title
            self.ax_explanation.text(0.5, 0.95, explanation["title"], 
                                   ha='center', va='top', fontsize=14, fontweight='bold',
                                   color='darkblue')
            
            # Content
            y_pos = 0.85
            for line in explanation["content"]:
                if line.startswith("🎯") or line.startswith("📊") or line.startswith("✅"):
                    # Special formatting for key points
                    self.ax_explanation.text(0.05, y_pos, line, ha='left', va='top', 
                                           fontsize=11, fontweight='bold', color='darkgreen')
                elif line.startswith("🔹") or line.startswith("🤔") or line.startswith("📐"):
                    # Secondary points
                    self.ax_explanation.text(0.05, y_pos, line, ha='left', va='top', 
                                           fontsize=10, color='darkblue')
                elif line == "":
                    # Empty line for spacing
                    pass
                else:
                    # Regular text
                    self.ax_explanation.text(0.05, y_pos, line, ha='left', va='top', 
                                           fontsize=10, color='black')
                y_pos -= 0.08
    
    def save_animation(self, filename="bpt_animation.gif"):
        """Save the animation as GIF."""
        anim = self.create_animation()
        anim.save(filename, writer='pillow', fps=10)
        return filename

# Usage function for Streamlit integration
def create_bpt_animation_for_streamlit(segments=[4, 6, 6, 9]):
    """Create BPT animation for Streamlit display."""
    
    animator = BPTAnimationExplainer()
    
    # Create static frames for Streamlit (since Streamlit doesn't support live animation)
    frames = []
    
    # Generate key frames
    for step in range(len(animator.animation_steps)):
        fig = plt.figure(figsize=(16, 10))
        
        # Setup same layout
        ax_triangle = plt.subplot2grid((1, 10), (0, 0), colspan=7)
        ax_explanation = plt.subplot2grid((1, 10), (0, 7), colspan=3)
        
        animator.ax_triangle = ax_triangle
        animator.ax_explanation = ax_explanation
        animator.setup_triangle_coordinates(segments)
        animator.configure_axes()
        
        # Draw this step
        step_data = animator.animation_steps[step]
        animator.draw_animation_step(step_data, 59)  # Full alpha
        animator.update_explanation_panel(step)
        
        frames.append(fig)
        plt.close()
    
    return frames

# Interactive BPT demonstration
def interactive_bpt_demo():
    """Create interactive BPT demonstration with sliders."""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Will be implemented with matplotlib widgets
    # This allows real-time manipulation of point D position
    # and shows how ratios change dynamically
    
    pass

if __name__ == "__main__":
    # Test the animation
    animator = BPTAnimationExplainer()
    anim = animator.create_animation([4, 6, 6, 9])
    plt.show()