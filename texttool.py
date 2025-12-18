#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def process_line(line, operation):
    text = line.strip()
    
    if operation == "upper":
        return text.upper()
    elif operation == "lower":
        return text.lower()
    elif operation == "count-words":
        return str(len(text.split()))
    elif operation == "length":
        return str(len(text))
    elif operation == "prefix":
        return text[:10]
    else:
        return f"Unknown operation: {operation}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python texttool.py <operation>")
        print("Operations: upper, lower, count-words, length, prefix")
        sys.exit(1)
    
    operation = sys.argv[1]
    
    for line in sys.stdin:
        result = process_line(line, operation)
        print(result)

if __name__ == "__main__":
    main()
