To parse an XML file using `lxml` and return the root element, you can follow these steps. Here's how you can implement the `get_root` function:

```python
from lxml import etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file and return the root.
    '''
    # Create an XML parser
    parser = etree.XMLParser()

    # Parse the XML file and get the root element
    tree = etree.parse('resources/config.xml', parser)
    root = tree.getroot()

    return root
```

### Explanation:
1. **XMLParser**: We create an instance of `etree.XMLParser()`. This parser can be customized with various options, but the default settings are usually sufficient for most cases.

2. **Parsing the XML File**: We use `etree.parse()` to read and parse the XML file. This function takes the file path and the parser as arguments and returns an `ElementTree` object.

3. **Getting the Root Element**: The `getroot()` method of the `ElementTree` object returns the root element of the XML document.

Make sure that the file path `'resources/config.xml'` is correct relative to where your script is running. If the file is not found, or if there are parsing errors, `lxml` will raise an exception, so you might want to add error handling depending on your use case.