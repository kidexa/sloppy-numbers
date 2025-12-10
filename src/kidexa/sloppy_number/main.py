import re

def parse(text):
    """
    Parses a messy string into a float or int.
    Handles 'k', 'm', 'b', commas, and currency symbols.
    """
    if isinstance(text, (int, float)):
        return text
        
    if not text:
        return None

    # Lowercase for easier handling of k/m/b
    clean_text = text.lower().strip()
    
    # extensive multiplier logic
    multiplier = 1
    if 'k' in clean_text:
        multiplier = 1_000
    elif 'm' in clean_text:
        multiplier = 1_000_000
    elif 'b' in clean_text:
        multiplier = 1_000_000_000

    # Remove commas to avoid issues with float conversion
    text_no_commas = clean_text.replace(',', '')

    # Find the first number-like pattern in the string
    # This regex handles integers and floats, including leading decimals like .5
    matches = re.findall(r'(\d+\.?\d*|\.?\d+)', text_no_commas)
    
    if not matches:
        return None
    
    amount_str = matches[0]
    
    try:
        val = float(amount_str) * multiplier
        
        # Return int if it's a whole number, else float
        if val.is_integer():
            return int(val)
        return val
    except ValueError:
        return None