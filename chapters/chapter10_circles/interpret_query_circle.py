import re
from typing import Dict, Any, Tuple, Optional
from sub_chapters.utils.sanitizer import sanitize_expression

def interpret_query(query: str) -> Dict[str, Any]:
    """
    Interpret the circle-related query and extract relevant parameters.
    """
    query = sanitize_expression(query)
    query = query.lower().strip()
    
    # Initialize result dictionary
    result = {
        'type': None,
        'parameters': {},
        'error': None
    }
    
    try:
        # Check for tangent length problems
        if any(keyword in query for keyword in ['tangent length', 'length of tangent']):
            result['type'] = 'tangent_length'
            params = extract_tangent_length_params(query)
            if params:
                result['parameters'] = params
            else:
                result['error'] = "Could not extract point coordinates and radius from query"
        
        # Check for theorem proofs
        elif any(keyword in query for keyword in ['prove', 'theorem', 'proof']):
            result['type'] = 'theorem_proof'
            if 'theorem 10.1' in query or 'perpendicular' in query:
                result['parameters'] = {'theorem': '10.1'}
            elif 'theorem 10.2' in query or 'equal' in query:
                result['parameters'] = {'theorem': '10.2'}
            else:
                result['error'] = "Please specify which theorem to prove (10.1 or 10.2)"
        
        # Check for construction problems
        elif any(keyword in query for keyword in ['construct', 'draw', 'construction']):
            result['type'] = 'construction'
            result['parameters'] = {'type': 'tangent_from_point'}
        
        # Check for real world applications
        elif any(keyword in query for keyword in ['area', 'rotation', 'wheel', 'distance']):
            result['type'] = 'real_world'
            params = extract_real_world_params(query)
            if params:
                result['parameters'] = params
            else:
                result['error'] = "Could not extract radius and angle from query"
        
        else:
            result['error'] = "Could not determine the type of circle problem"
    
    except Exception as e:
        result['error'] = f"Error interpreting query: {str(e)}"
    
    return result

def extract_tangent_length_params(query: str) -> Optional[Dict[str, float]]:
    """Extract point coordinates, radius, and optional center from tangent length query."""
    try:
        import re

        # Extract point
        point_match = re.search(r'from point\s*\(([\d.-]+),\s*([\d.-]+)\)', query)
        if not point_match:
            return None
        x = float(point_match.group(1))
        y = float(point_match.group(2))

        # Extract radius
        radius_match = re.search(r'radius\s+([\d.]+)', query)
        if not radius_match:
            return None
        r = float(radius_match.group(1))

        # Extract center (optional)
        center_match = re.search(r'center\s*\(([\d.-]+),\s*([\d.-]+)\)', query)
        if center_match:
            h = float(center_match.group(1))
            k = float(center_match.group(2))
        else:
            h, k = 0.0, 0.0  # Default to origin if not given

        return {
            'x': x,
            'y': y,
            'radius': r,
            'h': h,
            'k': k
        }

    except Exception:
        return None

def extract_real_world_params(query: str) -> Optional[Dict[str, float]]:
    """Extract radius and angle from real world application query."""
    try:
        # Look for radius
        radius_match = re.search(r'radius\s+(\d+\.?\d*)', query)
        if not radius_match:
            return None
        
        r = float(radius_match.group(1))
        
        # Look for angle
        angle_match = re.search(r'(\d+\.?\d*)\s*(?:degrees|°)', query)
        if not angle_match:
            return None
        
        angle = float(angle_match.group(1))
        
        return {
            'radius': r,
            'angle': angle
        }
    
    except Exception:
        return None 