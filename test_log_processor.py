#!/usr/bin/env python3
"""
Test script for log processing functions.
"""

from log_processor import normalize_level, validate_and_normalize

def test_normalize_level():
    """Test the normalize_level function."""
    print("Testing normalize_level:")
    
    test_cases = [
        (" warn ", "WARN"),
        ("error", "ERROR"),
        (" INFO ", "INFO"),
        ("debug", "DEBUG"),
        ("", ""),
    ]
    
    for input_val, expected in test_cases:
        result = normalize_level(input_val)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Input: '{input_val}' -> Output: '{result}' (Expected: '{expected}') [{status}]")

def test_validate_and_normalize():
    """Test the validate_and_normalize function."""
    print("\nTesting validate_and_normalize:")
    
    test_cases = [
        # Valid cases
        (("2026-02-05 08:11:20", " warn ", "db", "DB timeout"), ("2026-02-05 08:11:20", "WARN", "db", "DB timeout")),
        (("2026-02-05 08:11:21", "error", "auth", "Login failed"), ("2026-02-05 08:11:21", "ERROR", "auth", "Login failed")),
        
        # Invalid level
        (("2026-02-05 08:11:22", "debug", "api", "Request received"), None),
        
        # Empty service
        (("2026-02-05 08:11:23", "INFO", "", "Service started"), None),
        
        # Empty message (after strip)
        (("2026-02-05 08:11:24", "WARN", "disk", " "), None),
        
        # Additional test: all spaces service
        (("2026-02-05 08:11:25", "ERROR", "   ", "Some message"), None),
        
        # Additional test: valid with spaces in message
        (("2026-02-05 08:11:26", "INFO", "web", " Server started "), ("2026-02-05 08:11:26", "INFO", "web", "Server started")),
    ]
    
    for input_val, expected in test_cases:
        result = validate_and_normalize(input_val)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Input: {input_val}")
        print(f"  Output: {result} (Expected: {expected}) [{status}]")
        print()

if __name__ == "__main__":
    test_normalize_level()
    test_validate_and_normalize()