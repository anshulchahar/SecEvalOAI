import os
import re

input_dir = 'results'
output_dir = 'cleaned_results'
os.makedirs(output_dir, exist_ok=True)

for fname in os.listdir(input_dir):
    if fname.endswith('.py') or fname.endswith('.py.py'):
        with open(os.path.join(input_dir, fname), 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract the first Python code block (```python ... ```)
        match = re.search(r'```python(.*?)```', content, re.DOTALL)
        if match:
            code = match.group(1).strip()
            output_path = os.path.join(output_dir, fname.replace('.py.py', '.py'))
            with open(output_path, 'w', encoding='utf-8') as out_f:
                out_f.write(code)
        else:
            print(f"No code block found in: {fname}")
