def normalize_level(level: str) -> str:
    """
    Normalize the log level by removing extra spaces and converting to uppercase.
    
    Args:
        level (str): The log level string to normalize.
    
    Returns:
        str: The normalized log level.
    """
    return level.strip().upper()

def validate_and_normalize(parsed) -> tuple | None:
    """
    Validate and normalize a parsed log entry.
    
    Args:
        parsed: A tuple containing (timestamp, level, service, message).
    
    Returns:
        tuple: The validated and normalized log entry, or None if invalid.
    """
    if not isinstance(parsed, tuple) or len(parsed) != 4:
        return None
    
    timestamp, level, service, message = parsed
    
    # Normalize the level
    level = normalize_level(level)
    
    # Check if level is allowed
    allowed = {"INFO", "WARN", "ERROR"}
    if level not in allowed:
        return None
    
    # Strip spaces from service and message
    service = service.strip()
    message = message.strip()
    
    # Check if service and message are not empty
    if not service or not message:
        return None
    
    # Return the clean tuple
    return (timestamp, level, service, message)