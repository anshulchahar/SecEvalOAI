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