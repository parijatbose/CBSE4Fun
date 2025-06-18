def construct_tangent(params: dict) -> str:
    """
    Provide construction steps for tangents based on construction type.
    
    Args:
        params: Dictionary containing:
            - construction_type: 'external_point', 'given_point', or 'general'
    
    Returns:
        str: Formatted construction steps
    """
    construction_type = params.get('construction_type', 'external_point')
    
    if construction_type == 'external_point':
        return construct_tangent_from_external_point()
    elif construction_type == 'given_point':
        return construct_tangent_at_given_point()
    else:
        return construct_general_tangent()

def construct_tangent_from_external_point() -> str:
    """
    Construction: Tangent from external point
    """
    return """
✏️ **Construction: Tangent from External Point**

📝 **Given:** Circle with center O and external point P

**Required:** Construct tangents from P to the circle

**Steps:**

**Step 1:** Join P and O with a straight line.

**Step 2:** Find the midpoint M of line segment PO.
- Place compass at P with opening more than half of PO
- Draw arcs above and below PO
- With same opening, place compass at O and draw intersecting arcs
- Join the intersection points to get perpendicular bisector
- This intersects PO at midpoint M

**Step 3:** With M as center and MO as radius, draw a circle.
- This circle will pass through both O and P
- This is because MO = MP (M is midpoint)

**Step 4:** Let this new circle intersect the original circle at points A and B.

**Step 5:** Join PA and PB using a ruler.
- PA and PB are the required tangents from P to the circle.

**Verification:**
- ∠PAO = ∠PBO = 90° (angles in semicircle)
- Therefore PA ⊥ OA and PB ⊥ OB
- Since OA and OB are radii, PA and PB are tangents by definition

**Why this works:**
- Points A and B lie on circle with diameter PO
- ∠PAO and ∠PBO are angles in semicircle = 90°
- Since OA and OB are radii, PA and PB are perpendicular to radii at points of contact
- By Theorem 10.1, PA and PB are tangents

🎯 **Result:** Two tangents PA and PB from external point P to the circle.

💡 **Note:** 
- From any external point, exactly two tangents can be drawn to a circle
- These tangents are equal in length (PA = PB) by Theorem 10.2
"""

def construct_tangent_at_given_point() -> str:
    """
    Construction: Tangent at given point on circle
    """
    return """
✏️ **Construction: Tangent at Given Point on Circle**

📝 **Given:** Circle with center O and point P on the circle

**Required:** Construct tangent at point P

**Method 1: Using Perpendicular**

**Step 1:** Join O and P to draw radius OP.

**Step 2:** At point P, construct a perpendicular to OP.
- Place compass at P with convenient radius
- Draw arc cutting OP at Q
- With Q as center and same radius, draw arc
- With increased radius, draw intersecting arcs from P and Q
- Join P to intersection point and extend

**Step 3:** Extend this perpendicular line on both sides of P.
- This line is the required tangent at point P

**Method 2: Using Set Square**

**Step 1:** Join O and P to draw radius OP.

**Step 2:** Place set square with right angle at P such that one arm lies along OP.

**Step 3:** Draw line along the other arm of set square.
- This line is the required tangent.

**Verification:**
- The constructed line is perpendicular to radius OP at P
- By Theorem 10.1, this line is tangent to the circle
- The tangent touches the circle only at point P

🎯 **Result:** Tangent line at point P on the circle.

💡 **Note:** 
- At any point on a circle, exactly one tangent can be drawn
- The tangent is always perpendicular to the radius at that point
"""

def construct_general_tangent() -> str:
    """
    General tangent construction methods and applications
    """
    return """
✏️ **General Tangent Construction Methods**

## **1. Direct Common Tangents to Two Circles**

**Steps:**
1. Join centers O₁ and O₂
2. Draw circle on O₁O₂ as diameter
3. From O₁, draw circle with radius (r₁ - r₂)
4. Find intersection points
5. Extend to get tangent points
6. Draw parallel tangents

## **2. Transverse Common Tangents**

**Steps:**
1. Join centers O₁ and O₂
2. Draw circle on O₁O₂ as diameter
3. From O₁, draw circle with radius (r₁ + r₂)
4. Find intersection points
5. Join and extend to get tangents

## **3. Tangent Parallel to Given Line**

**Steps:**
1. Draw perpendicular from center to given line
2. Mark points on circle where perpendicular meets
3. Draw lines through these points parallel to given line
4. These are the required tangents

## **4. Tangent at Given Angle**

**Steps:**
1. Draw radius at required angle from horizontal
2. Construct perpendicular at endpoint
3. This gives tangent at specified angle

## **Tools Required:**
- Compass (for arcs and circles)
- Ruler (for straight lines)
- Set squares (for perpendiculars)
- Protractor (for specific angles)

## **Key Properties Used:**
1. Tangent ⊥ radius at point of contact
2. Angle in semicircle = 90°
3. Equal tangents from external point
4. Tangent as limiting position of secant

## **Common Mistakes to Avoid:**
- Not making perpendicular exactly at point of contact
- Drawing tangent that cuts the circle
- Incorrect positioning of compass
- Not extending tangent sufficiently

## **Applications:**
- Engineering design (cam profiles, gears)
- Road construction (curves and transitions)
- Architecture (arches and domes)
- Optics (reflection and refraction)
"""

