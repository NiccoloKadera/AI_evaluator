import json
import os
import re
from model.ABML.syntax import ABML_SYNTAX, ABML_TO_MERMAID

class ABML_translation:


    def __init__(self):

        # Loading syntax file
        self.syntax = ABML_SYNTAX

    def translate_to_py(self, abml_code):
        py_code = abml_code
        
        # Applicazione di tutte le regole di traduzione dal dizionario syntax
        for pattern, replacement_template in self.syntax.items():
            if "\\1" in replacement_template:  # Se il template usa riferimenti ai gruppi catturati
                # Compila il pattern come espressione regolare
                regex_pattern = re.compile(pattern)
                
                
                # Cerca corrispondenze nel codice
                match = regex_pattern.search(py_code)                
                if match:
                    # Sostituisci con il template, mantenendo i gruppi catturati
                    groups = match.groups()
                    result = replacement_template
                    for i, group in enumerate(groups):
                        result = result.replace(f"\\{i+1}", group)
                    
                    # Sostituisci l'intera corrispondenza con il risultato
                    py_code = py_code.replace(match.group(0), result)
            else:
                # Per sostituzioni letterali semplici
                py_code = py_code.replace(pattern, replacement_template)
                
        return py_code
    
    def translate_to_mermaid(self, abml_code):        
        
        
        mermaid_code = ''

        for pattern, replacement_template in ABML_TO_MERMAID.items():
            if "\\1" in replacement_template:  # Se il template usa riferimenti ai gruppi catturati
                # Compila il pattern come espressione regolare
                regex_pattern = re.compile(pattern)

                # Cerca corrispondenze nel codice
                match = regex_pattern.search(abml_code)                
                if match:
                    # Sostituisci con il template, mantenendo i gruppi catturati
                    groups = match.groups()
                    result = replacement_template
                    for i, group in enumerate(groups):
                        result = result.replace(f"\\{i+1}", group)

                    # Sostituisci l'intera corrispondenza con il risultato
                    mermaid_code = result
            else:
                # Per sostituzioni letterali semplici
                mermaid_code = mermaid_code.replace(pattern, replacement_template)
        
        return mermaid_code



if __name__ == "__main__":
    translator = ABML_translation()

    # Test con il vecchio esempio
    abml_code1 = '(a ? b) -> c'
    py_code1 = translator.translate_to_py(abml_code1)
    print(f"Test 1: {abml_code1} -> {py_code1}")
    
    # Test con il nuovo esempio
    abml_code2 = '(a.c_level > b) -> a.infected = True'
    py_code2 = translator.translate_to_py(abml_code2)
    print(f"Test 2: {abml_code2} -> {py_code2}")