import os


PAGE_SIZE = os.getenv('PAGE_SIZE')
PAGE_SIZE = int(PAGE_SIZE) if PAGE_SIZE is not None else 5