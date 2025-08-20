
ABML_SYNTAX = {
    # Description: This is the If statement.
    # Input: (a > b) -> c
    # Output: if a > b: c
    "\\((.*?)\\)\\s*->\\s*(.*)": "if \\1: \\2",

    # Description: Assignment a = b -> a = b
    # Input: a = b
    # Output: a = b
    "(.*?)\\s*->\\s*(.*)": "\\1 = \\2",
    
}

