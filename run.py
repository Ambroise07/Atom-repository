import subprocess
from pathlib import Path 

main = Path(__file__).parent.resolve() / 'main.py'

subprocess.run(['python3', main], check=True)
