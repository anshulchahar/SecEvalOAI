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