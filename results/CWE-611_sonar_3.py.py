To transform an XML document using XSLT with the `lxml` library in Python, you need to follow these steps:

1. Create an XML parser.
2. Parse the XSLT file to create an XSLT object.
3. Use the XSLT object to transform an XML document.

Here's how you can implement the `transform_xml` function to achieve this:

```python
from lxml import etree

def transform_xml():
    '''
    Create an XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    # Parse the XSL file
    xslt_file = 'resources/config.xsl'
    xslt_doc = etree.parse(xslt_file)
    
    # Create an XSLT object
    xslt_transformer = etree.XSLT(xslt_doc)
    
    return xslt_transformer

# Example usage
# Assuming you have an XML file to transform
def example_usage():
    xml_file = 'resources/data.xml'
    xml_doc = etree.parse(xml_file)
    
    # Get the XSLT transformer
    transformer = transform_xml()
    
    # Transform the XML document
    transformed_doc = transformer(xml_doc)
    
    # Print the transformed XML
    print(str(transformed_doc))

# Uncomment the following line to run the example
# example_usage()
```

### Explanation:

- **Parsing the XSLT File**: The `etree.parse()` function is used to parse the XSLT file located at `'resources/config.xsl'`. This creates an XML document object representing the XSLT stylesheet.

- **Creating an XSLT Object**: The `etree.XSLT()` function takes the parsed XSLT document and returns an XSLT transformer object. This object can be used to apply the transformation to XML documents.

- **Transforming an XML Document**: To transform an XML document, parse the XML file into an `etree` object and then call the XSLT transformer with this object. The result is a transformed XML document.

This code assumes that you have both the XSLT and XML files available in the specified paths. Adjust the file paths as necessary for your environment.