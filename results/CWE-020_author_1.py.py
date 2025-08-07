To load the contents of a YAML file using the `yaml` library in Python, you can follow these steps. Here's how you can implement the `yaml_load` function:

```python
import yaml

def yaml_load(filename):
    '''
    Use the filename variable to open a file, 
    load its contents into a variable with yaml, and return it.
    '''
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    return data
```

### Explanation:
- **Importing yaml**: Ensure you have the PyYAML library installed. You can install it using `pip install pyyaml` if it's not already installed.
- **Opening the File**: Use the `open` function with `'r'` mode to read the file.
- **Loading YAML Content**: Use `yaml.safe_load(file)` to parse the YAML content. `safe_load` is preferred over `load` as it safely parses the YAML content without executing arbitrary code.
- **Returning the Data**: The parsed data is returned, which can be a Python dictionary or list, depending on the structure of the YAML file.

This function will read the specified YAML file and return its contents as a Python data structure.