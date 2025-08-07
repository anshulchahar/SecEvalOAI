To parse an XML string and return the root element using Python's `xml.etree.ElementTree`, you can follow these steps. Here's a function that accomplishes this:

```python
import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    try:
        # Parse the XML string into an ElementTree object
        root = ET.fromstring(xml_string)
        return root
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return None

# Example usage
xml_data = """<root>
    <child>Some data</child>
</root>"""

root_element = parse_xml(xml_data)
if root_element is not None:
    print(f"Root element: {root_element.tag}")
```

### Explanation:
- **`ET.fromstring(xml_string)`**: This function parses an XML string and returns the root element of the XML document.
- **Error Handling**: The `try-except` block is used to catch and handle any `ParseError` exceptions that may occur if the XML string is not well-formed.
- **Example Usage**: The example demonstrates how to use the `parse_xml` function to parse a simple XML string and print the tag of the root element.

This function will return the root element of the XML document if the parsing is successful, or `None` if there is a parsing error.