
ABML_SYNTAX = {
    # Description: This is the If statement.
    # Input: (a > b) -> c
    # Output: if a > b: c
    "\\((.*?)\\)\\s*->\\s*(.*)": "if \\1: \\2",

    # Description: Assignment a = b -> a = b
    # Input: a = b
    # Output: a = b
    "(.*?)\\s*->\\s*(.*)": "\\1 = \\2",
    
    # Description: This is the While loop.
    # Input: while(a < 10) -> c
    # Output: while a < 10: c
    "while\s*\((.*?)\)\s*->\s*(.*)": "while \1: \2",

    # Description: This is the For loop.
    # Input: for(i in range(5)) -> c
    # Output: for i in range(5): c
    "for\s*\((.*?)\s+in\s+(.*?)\)\s*->\s*(.*)": "for \1 in \2: \3",
}

ABML_TO_MERMAID = {
    # Description: Translation of the if statement.
    # Input: (a > b) -> c
    # Output: -:!-(a > b) --> |True| -:!!-[c] \n -:!- --> |False| -:!stop!-
    "\\((.*?)\\)\\s*->\\s*(.*)": "-:!-{\\1} -->|True| -:!!-[\"\\2\"]\n-:!- -->|False| -:!!!-",
}