#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════
  CHALLENGE: Create Your Own Variables
  Episode 3 - Variables & Data Types
  CodeToAGI with Mahaz Abbasi
═══════════════════════════════════════════════════════════════════════════

  INSTRUCTIONS:
  ------------
  Create 4 variables about yourself:
  
  • your_name      - as a string (text)
  • your_age       - as an integer (whole number)
  • your_city      - as a string (text)
  • learning_python - as a boolean (True or False)
  
  Then print all 4 variables to see what's stored inside them.

  HOW TO RUN:
  -----------
  python my_variables.py
"""

# ============================================================================
# CREATE YOUR 4 VARIABLES
# ============================================================================

# String - text data (always in quotes)
your_name = "Mahaz Abbasi"

# Integer - whole number (no quotes, no decimal point)
your_age = 32

# String - text data (always in quotes)
your_city = "Islamabad"

# Boolean - True or False (capital T and capital F, no quotes)
learning_python = True

# ============================================================================
# PRINT ALL VARIABLES
# ============================================================================

print("--- My Profile ---")
print(your_name)
print(your_age)
print(your_city)
print(learning_python)


"""
═══════════════════════════════════════════════════════════════════════════
  EXPECTED OUTPUT:
  ═══════════════════════════════════════════════════════════════════════════
  
  --- My Profile ---
  Mahaz Abbasi
  32
  Islamabad
  True

  ═══════════════════════════════════════════════════════════════════════════
  
  YOUR TURN - Replace with your own information:
  ═══════════════════════════════════════════════════════════════════════════
  
  your_name = "Your Name Here"
  your_age = YOUR_AGE_HERE
  your_city = "Your City Here"
  learning_python = True

  ═══════════════════════════════════════════════════════════════════════════
  
  DATA TYPES REVIEW:
  ═══════════════════════════════════════════════════════════════════════════
  
  • str (string)     - Text. Anything in quotes.      Example: "Hello"
  • int (integer)    - Whole numbers. No decimal.     Example: 42
  • float            - Decimal numbers.               Example: 3.14
  • bool (boolean)   - True or False.                 Example: True
  
  ═══════════════════════════════════════════════════════════════════════════
  
  VARIABLE NAMING RULES:
  ═══════════════════════════════════════════════════════════════════════════
  
  ✓ Letters, numbers, and underscores only
  ✓ Cannot start with a number
  ✓ No spaces or hyphens
  ✓ Cannot use Python keywords (if, for, while, class, etc.)
  ✓ Use snake_case (lowercase with underscores)
  
  ═══════════════════════════════════════════════════════════════════════════
  
  CHECK YOUR VARIABLE TYPES:
  ═══════════════════════════════════════════════════════════════════════════
  
  Uncomment these lines to check what type each variable is:
  
  # print(type(your_name))
  # print(type(your_age))
  # print(type(your_city))
  # print(type(learning_python))
  
  Happy Coding! - Mahaz Abbasi | @CodeToAGI
═══════════════════════════════════════════════════════════════════════════
"""
