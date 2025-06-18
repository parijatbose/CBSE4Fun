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