"""
Logic Templates for CBSE Class 10 Chapter 9 - Circles
Contains JSON templates for different circle query types and examples
"""

# Import template loading utilities if needed
import os
import json

def load_template(template_name: str):
    """
    Load a specific logic template JSON file
    
    Args:
        template_name (str): Name of the template file (without .json extension)
    
    Returns:
        dict: Template data or None if file not found
    """
    template_path = os.path.join(os.path.dirname(__file__), f'{template_name}.json')
    if os.path.exists(template_path):
        with open(template_path, 'r') as f:
            return json.load(f)
    return None

def get_available_templates():
    """
    Get list of available template files
    
    Returns:
        list: List of available template names
    """
    template_dir = os.path.dirname(__file__)
    templates = []
    for file in os.listdir(template_dir):
        if file.endswith('.json'):
            templates.append(file[:-5])  # Remove .json extension
    return templates

# Available template types
TEMPLATE_TYPES = [
    'tangent_length',
    'theorem_proof', 
    'construction',
    'application'
]
