
def build_syntax():
    """
    Generates a .rst file for Sphinx documentation containing a table of the ABML syntax.
    The table has 3 columns: Input, Output, and Description, populated from comments in the syntax.py file.
    """
    import re
    import os

    syntax_input_path = 'model/ABML/syntax.py'
    syntax_output_path = 'docs/source/language/syntax.rst'

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(syntax_output_path), exist_ok=True)

    # Read the syntax.py file
    with open(syntax_input_path, 'r') as f:
        syntax_content = f.read()

    # Initialize the .rst content with a title and introduction
    rst_content = """ABML Syntax
===========

This page documents the syntax of the ABML language and its translation to Python.

.. list-table:: ABML Syntax Table
   :widths: 30 30 40
   :header-rows: 1

   * - Input
     - Output
     - Description
"""

    # Extract each pattern and its comments
    # Look for blocks of comments followed by pattern/replacement pair
    pattern_blocks = re.findall(
        r'(\s*# Description:\s*(.*?)\s*\n\s*# Input:\s*(.*?)\s*\n\s*# Output:\s*(.*?)\s*\n\s*"(.*?)":\s*"(.*?)")',
        syntax_content,
        re.DOTALL
    )

    # Add each entry to the table
    for _, description, input_example, output_example, _, _ in pattern_blocks:
        # Clean up the examples and description
        description = description.strip()
        input_example = input_example.strip()
        output_example = output_example.strip()

        # Add row to the table
        rst_content += f"""
   * - ``{input_example}``
     - ``{output_example}``
     - {description}"""

    # Write the .rst file
    with open(syntax_output_path, 'w') as f:
        f.write(rst_content)

    print(f"Syntax documentation generated at: {syntax_output_path}")




