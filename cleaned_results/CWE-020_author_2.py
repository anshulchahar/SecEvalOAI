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