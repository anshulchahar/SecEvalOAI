To parse an XML file using `lxml` and return the root element, you can follow these steps. Below is a function that demonstrates how to achieve this:

```python
from lxml import etree

def getXmlRoot():
    '''
    Create an XML parser and parse the resources/c.xml file and return the root element
    '''
    # Parse the XML file
    tree = etree.parse('resources/c.xml')
    
    # Get the root element
    root = tree.getroot()
    
    return root

# Example usage
if __name__ == "__main__":
    root_element = getXmlRoot()
    print(etree.tostring(root_element, pretty_print=True).decode())
```

### Explanation:

1. **Import `etree` from `lxml`:** This is necessary to work with XML files using the `lxml` library.

2. **Parse the XML File:**
   - Use `etree.parse('resources/c.xml')` to parse the XML file located at `resources/c.xml`. This returns an `ElementTree` object.

3. **Get the Root Element:**
   - Call `tree.getroot()` on the `ElementTree` object to get the root element of the XML document.

4. **Return the Root Element:**
   - The function returns the root element, which can be used to navigate and manipulate the XML tree.

5. **Example Usage:**
   - The example usage demonstrates how to call the function and print the XML content in a pretty-printed format.

Make sure that the file path `'resources/c.xml'` is correct and that the file exists at that location. Adjust the path as necessary based on your directory structure.