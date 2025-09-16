from ABML_translation import ABML_translation

class ABML_Mermaid:

    def __init__(self):
        pass


    def convert_to_mermaid(self, abml_code):
        # Implement the conversion logic here
        mermaid_code = "flowchart TD\n  0[Start] --> 1\n"
        lines = abml_code.splitlines()
        cont = 1

        abml_tr = ABML_translation()

        for line in lines:
            mermaid_lines = abml_tr.translate_to_mermaid(line)
            mermaid_lines = mermaid_lines.replace('-:!stop!-', 'Stop')
            
            for i in range(1, 1000):
                line_replace = f'-:{i * "!"}-'
                if line_replace in mermaid_lines:
                    mermaid_lines = mermaid_lines.replace(line_replace, str(cont))
                    cont += 1                    
                else: break
            
            for mermaid_line in mermaid_lines.splitlines():
                mermaid_code += f"  {mermaid_line}\n"

        return mermaid_code

