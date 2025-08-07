To create an XML parser, parse an XSD file, and return an XMLSchema object using `lxml`, you can follow these steps. This example assumes that you have an XSD file located at `resources/config.xsd`.

Here's how you can implement the `get_root` function:

```python
from lxml import etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    # Parse the XSD file
    with open('resources/config.xsd', 'rb') as xsd_file:
        xsd_content = xsd_file.read()
    
    # Create an XML parser
    xml_parser = etree.XMLParser()

    # Parse the XSD content
    xsd_tree = etree.XML(xsd_content, parser=xml_parser)

    # Create an XMLSchema object
    xml_schema = etree.XMLSchema(xsd_tree)

    return xml_schema

# Example usage
if __name__ == "__main__":
    schema = get_root()
    print(schema)
```

### Explanation:
1. **Open and Read the XSD File**: The XSD file is opened in binary mode and read into memory.
2. **Create an XML Parser**: An `XMLParser` object is created, which is used to parse the XML content.
3. **Parse the XSD Content**: The XSD content is parsed into an XML tree using `etree.XML`.
4. **Create an XMLSchema Object**: The parsed XML tree is used to create an `XMLSchema` object, which can be used to validate XML documents against the schema.

This function will return an `XMLSchema` object that you can use to validate XML documents. Make sure that the file path `'resources/config.xsd'` is correct and points to your XSD file.