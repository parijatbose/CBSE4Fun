import math
from typing import Dict, Any

def solve_bpt(params: Dict[str, Any]) -> str:
    """
    Apply Basic Proportionality Theorem (Thales Theorem).
    """
    try:
        problem_type = params.get("type", "find_segment")
        segments = params.get("segments", [])
        
        if len(segments) < 4:
            return "❌ Need all 4 segments (AD, DB, AE, EC) to verify if DE || BC"
        
        AD, DB, AE, EC = segments[:4]
        
        # Calculate ratios
        ratio1 = AD / DB
        ratio2 = AE / EC
        difference = abs(ratio1 - ratio2)
        is_parallel = difference < 0.001
        
        result = f"""
✅ **Converse of BPT - Verify Parallel Lines:**

Given segments in triangle ABC:
• AD = {AD} cm
• DB = {DB} cm
• AE = {AE} cm
• EC = {EC} cm

📝 **Checking if DE || BC:**

**Converse of BPT:** If AD/DB = AE/EC, then DE || BC

**1. Calculate ratios:**
   • AD/DB = {AD}/{DB} = {ratio1:.4f}
   • AE/EC = {AE}/{EC} = {ratio2:.4f}

**2. Compare ratios:**
   • Difference = |{ratio1:.4f} - {ratio2:.4f}| = {difference:.6f}
   • Are ratios equal? {'YES ✓' if is_parallel else 'NO ✗'}

💡 **Conclusion:**
{'✅ DE IS PARALLEL to BC' if is_parallel else '❌ DE is NOT PARALLEL to BC'}
{f'The ratios are equal, so by converse of BPT, DE || BC' if is_parallel else f'The ratios are not equal, so DE is not parallel to BC'}

**Additional Info:**
• AB = AD + DB = {AD + DB} cm
• AC = AE + EC = {AE + EC} cm
• Ratio AD/AB = {AD/(AD+DB):.3f}
• Ratio AE/AC = {AE/(AE+EC):.3f}
"""
        
        return result

    except Exception as e:
        return f"❌ Error applying BPT: {str(e)}"

def find_ratio_bpt(params: Dict[str, Any]) -> str:
    """
    Find ratios using BPT.
    """
    known_ratio = params.get("known_ratio", 0)
    find_type = params.get("find_type", "segments")
    
    if known_ratio <= 0:
        return "❌ Need a valid ratio to work with"
    
    result = f"""
✅ **BPT - Working with Ratios:**

Given: DE || BC and one ratio = {known_ratio}

📝 **Using BPT Properties:**

**If AD/DB = {known_ratio}, then:**
1. AE/EC = {known_ratio} (by BPT)
2. AD/AB = AD/(AD+DB) = {known_ratio}/{known_ratio + 1} = {known_ratio/(known_ratio + 1):.3f}
3. AE/AC = AE/(AE+EC) = {known_ratio}/{known_ratio + 1} = {known_ratio/(known_ratio + 1):.3f}
4. DE/BC = AD/AB = {known_ratio/(known_ratio + 1):.3f}

**Example with concrete numbers:**
If AD = {known_ratio * 5} cm, then:
• DB = {5} cm
• AE = {known_ratio * 6} cm (if AC = {(known_ratio + 1) * 6} cm)
• EC = {6} cm

💡 **Key Relationships:**
• The ratios AD/DB and AE/EC are always equal when DE || BC
• The ratio DE/BC equals AD/AB (or AE/AC)
• These ratios help find unknown segments
"""
    
    return result

def explain_bpt_with_example() -> str:
    """
    Explain BPT with a worked example.
    """
    result = """
✅ **Basic Proportionality Theorem (Thales Theorem) Explained:**

📐 **Statement:**
If a line is drawn parallel to one side of a triangle intersecting the other two sides, then it divides the two sides proportionally.

**In Triangle ABC with DE || BC:**
• D lies on AB
• E lies on AC
• Then: AD/DB = AE/EC

📝 **Worked Example:**

Given: Triangle ABC with DE || BC
• AD = 6 cm
• DB = 4 cm
• AE = 9 cm
• Find EC

**Solution:**
1. Apply BPT: AD/DB = AE/EC
2. Substitute: 6/4 = 9/EC
3. Cross-multiply: 6 × EC = 4 × 9
4. 6 × EC = 36
5. EC = 36/6 = 6 cm

**Verification:**
• AD/DB = 6/4 = 1.5
• AE/EC = 9/6 = 1.5 ✓

💡 **Applications:**
1. Finding unknown segments
2. Proving lines are parallel
3. Dividing line segments in given ratio
4. Similar triangle problems

**Converse of BPT:**
If AD/DB = AE/EC, then DE || BC

**Important Ratios:**
• AD/AB = AE/AC = DE/BC
• DB/AB = EC/AC
• AD/DB = AE/EC
"""
    
    return result

def find_segment_bpt(params: Dict[str, Any]) -> str:
    """
    Find missing segment using BPT.
    """
    segments = params.get("segments", [])
    
    if len(segments) < 3:
        return "❌ Need at least 3 known segments to find the fourth"
    
    # BPT: If DE || BC, then AD/DB = AE/EC
    # Segments order: AD, DB, AE, EC
    if len(segments) == 4 and 0 in segments:
        # Find which segment is missing
        if segments[0] == 0:  # AD missing
            AD = (segments[1] * segments[2]) / segments[3]
            missing = "AD"
            value = AD
            formula = f"AD = (DB × AE) / EC = ({segments[1]} × {segments[2]}) / {segments[3]}"
        elif segments[1] == 0:  # DB missing
            DB = (segments[0] * segments[3]) / segments[2]
            missing = "DB"
            value = DB
            formula = f"DB = (AD × EC) / AE = ({segments[0]} × {segments[3]}) / {segments[2]}"
        elif segments[2] == 0:  # AE missing
            AE = (segments[0] * segments[3]) / segments[1]
            missing = "AE"
            value = AE
            formula = f"AE = (AD × EC) / DB = ({segments[0]} × {segments[3]}) / {segments[1]}"
        else:  # EC missing
            EC = (segments[1] * segments[2]) / segments[0]
            missing = "EC"
            value = EC
            formula = f"EC = (DB × AE) / AD = ({segments[1]} × {segments[2]}) / {segments[0]}"
    else:
        # Use first 3 to find 4th
        AD, DB, AE = segments[:3]
        EC = (DB * AE) / AD
        missing = "EC"
        value = EC
        formula = f"EC = (DB × AE) / AD = ({DB} × {AE}) / {AD}"
    
    result = f"""
✅ **Basic Proportionality Theorem (BPT) Solution:**

Given: In triangle ABC with DE || BC
• AD = {segments[0] if segments[0] != 0 else '?'} cm
• DB = {segments[1] if len(segments) > 1 and segments[1] != 0 else '?'} cm
• AE = {segments[2] if len(segments) > 2 and segments[2] != 0 else '?'} cm
• EC = {segments[3] if len(segments) > 3 and segments[3] != 0 else '?'} cm

📝 **Finding {missing}:**

**BPT States:** If DE || BC, then AD/DB = AE/EC

**Cross-multiplication:**
AD × EC = DB × AE

**Solving for {missing}:**
{formula}
{missing} = {value:.2f} cm

💡 **Verification:**
• Ratio 1: AD/DB = {segments[0] if segments[0] != 0 else value}/{segments[1] if segments[1] != 0 else value} = {(segments[0] if segments[0] != 0 else value)/(segments[1] if segments[1] != 0 else value):.3f}
• Ratio 2: AE/EC = {segments[2] if segments[2] != 0 else value}/{segments[3] if segments[3] != 0 else value} = {(segments[2] if segments[2] != 0 else value)/(segments[3] if segments[3] != 0 else value):.3f}
• Ratios are equal ✓
"""
    
    return result

def verify_parallel_bpt(params: Dict[str, Any]) -> str:
    """
    Verify if a line is parallel using converse of BPT.
    """
    segments = params.get("segments", [])
    
    if problem_type == "find_segment":
        return find_segment_bpt(params)
    elif problem_type == "verify_parallel":
        return verify_parallel_bpt(params)
    elif problem_type == "find_ratio":
        return find_ratio_bpt(params)
    else:
        return explain_bpt_with_example()