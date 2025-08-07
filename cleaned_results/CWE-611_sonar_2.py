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