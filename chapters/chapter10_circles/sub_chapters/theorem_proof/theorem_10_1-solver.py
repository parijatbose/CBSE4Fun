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

## **Proof**

**Step 1:** Assume tangent l is NOT perpendicular to radius OP

**Step 2:** If l ⊥ OP, then there exists another line through P that is perpendicular to OP

**Step 3:** Let this perpendicular line be m, where m ⊥ OP

**Step 4:** Take any point Q on line l (Q ≠ P)
- Since l is tangent, Q lies outside the circle
- Therefore: OQ > OP

**Step 5:** Take any point R on line m (R ≠ P)  
- Since m ⊥ OP, by Pythagoras theorem in △OPR:
- OR² = OP² + PR²
- Since PR > 0, we get OR > OP

**Step 6:** This means both lines l and m have points outside the circle

**Step 7:** But a tangent can touch the circle at only ONE point

**Step 8:** This contradicts our assumption

**Therefore:** Our assumption is wrong, and l ⊥ OP

## **Conclusion** ✅
The tangent at any point of a circle is perpendicular to the radius through the point of contact.
"""