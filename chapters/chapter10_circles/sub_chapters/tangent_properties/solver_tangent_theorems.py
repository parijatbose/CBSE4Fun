def prove_tangent_theorem(params: dict) -> str:
    """
    Prove tangent-related theorems based on theorem type.
    
    Args:
        params: Dictionary containing:
            - theorem_type: 'perpendicular', 'equal_tangents', or 'general'
    
    Returns:
        str: Formatted theorem proof
    """
    theorem_type = params.get('theorem_type', 'general')
    
    if theorem_type == 'perpendicular':
        return prove_theorem_10_1()
    elif theorem_type == 'equal_tangents':
        return prove_theorem_10_2()
    else:
        return get_general_theorems()

def prove_theorem_10_1() -> str:
    """
    Prove Theorem 10.1: Tangent perpendicular to radius
    """
    return """
# 📖 CBSE Theorem 10.1 Proof

## **Statement**
The tangent at any point of a circle is perpendicular to the radius through the point of contact.

## **Given**
- Circle with center O
- Point P on the circle  
- Tangent line l at point P
- Radius OP

## **To Prove**
l ⊥ OP (tangent is perpendicular to radius)

## **Proof by Contradiction**

**Step 1:** Assume tangent l is NOT perpendicular to radius OP.

**Step 2:** If l is not perpendicular to OP, then we can drop a perpendicular from O to line l, meeting l at point Q.

**Step 3:** Since OQ ⊥ l and Q ≠ P (as l is not perpendicular to OP):
- In right triangle OQP: OQ < OP (perpendicular is shortest distance)

**Step 4:** This means Q is inside the circle (as OQ < radius).

**Step 5:** But then line l passes through:
- Point Q (inside the circle)
- Point P (on the circle)
- Points beyond P (outside the circle)

**Step 6:** This means l intersects the circle at more than one point, contradicting the definition of a tangent.

**Step 7:** Therefore, our assumption is wrong, and l must be perpendicular to OP.

## **Alternative Proof (Direct)**

**Step 1:** Take any point X on tangent l (X ≠ P).

**Step 2:** Since l is tangent, X lies outside the circle.
- Therefore: OX > OP (radius)

**Step 3:** In triangle OPX:
- OX > OP means ∠OPX < 90° would make OX smaller
- But OX must be > OP for all points X on l
- This is only possible if ∠OPX = 90°

## **Conclusion** ✅
The tangent at any point of a circle is perpendicular to the radius through the point of contact.

## **Applications**
- Construction of tangents
- Solving circle geometry problems
- Finding angles in tangent-related figures
"""

def prove_theorem_10_2() -> str:
    """
    Prove Theorem 10.2: Equal tangent lengths from external point
    """
    return """
# 📖 CBSE Theorem 10.2 Proof

## **Statement**
The lengths of tangents drawn from an external point to a circle are equal.

## **Given**
- Circle with center O
- External point P
- Two tangents PA and PB from P to circle
- A and B are points of contact

## **To Prove**
PA = PB (tangent lengths are equal)

## **Proof**

**Step 1:** Consider triangles △OAP and △OBP

**Step 2:** In △OAP and △OBP:
- OA = OB (both are radii of the same circle)
- ∠OAP = ∠OBP = 90° (tangent ⊥ radius, by Theorem 10.1)
- OP = OP (common side)

**Step 3:** By RHS (Right angle-Hypotenuse-Side) congruence:
- △OAP ≅ △OBP

**Step 4:** Since triangles are congruent:
- Corresponding sides are equal
- Therefore: **PA = PB**

## **Alternative Proof using Coordinate Geometry**

**Step 1:** Let circle have center O(0,0) and radius r
- External point P(h,k) where h² + k² > r²

**Step 2:** For any tangent from P to circle:
- Length = √[h² + k² - r²] (using tangent length formula)

**Step 3:** Since the formula gives same result for all tangents from P:
- All tangent lengths from P are equal

## **Conclusion** ✅
The lengths of tangents drawn from an external point to a circle are equal.

## **Applications**
- Calculating tangent lengths
- Solving quadrilateral problems involving circles
- Finding angles in circle geometry
"""

def get_general_theorems() -> str:
    """
    Return overview of circle tangent theorems
    """
    return """
# 📚 Circle Tangent Theorems Overview

## **Theorem 10.1: Tangent ⊥ Radius**
- The tangent at any point of a circle is perpendicular to the radius through the point of contact.
- Key application: Construction and angle calculations

## **Theorem 10.2: Equal Tangents**
- The lengths of tangents drawn from an external point to a circle are equal.
- Key application: Solving for unknown lengths

## **Additional Important Results**

### **1. Number of Tangents**
- From a point inside circle: 0 tangents
- From a point on circle: 1 tangent
- From a point outside circle: 2 tangents

### **2. Angle Between Tangents**
- If two tangents from external point P make angle θ:
- sin(θ/2) = r/d, where r = radius, d = distance from P to center

### **3. Power of a Point**
- For external point P and tangent PT: PT² = PA × PB
- Where PAB is any secant through P

### **4. Common Tangents**
- Two circles can have 0, 1, 2, 3, or 4 common tangents
- Depends on relative positions of circles

## **Problem-Solving Strategy**
1. Identify given information
2. Draw clear diagram
3. Apply relevant theorem
4. Use congruence or similarity if needed
5. Verify answer makes geometric sense

## **Common Question Types**
- Prove tangent theorems
- Calculate tangent lengths
- Find angles involving tangents
- Construct tangents
- Solve real-world applications
"""
