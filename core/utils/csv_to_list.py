def  convert_csv_to_list(csv_string:str) -> list:
    """Convert a comma-seprated string into a list."""
    return [item.strip() for item in csv_string.split(",")]