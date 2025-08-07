import xml.sax

class ConfigHandler(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.current_data = ""
        self.parsed_data = {}

    def startElement(self, tag, attributes):
        self.current_data = tag
        # Initialize a dictionary for the current tag if it doesn't exist
        if tag not in self.parsed_data:
            self.parsed_data[tag] = []

    def endElement(self, tag):
        self.current_data = ""

    def characters(self, content):
        if self.current_data:
            # Append the content to the list of the current tag
            self.parsed_data[self.current_data].append(content.strip())

def get_root():
    # Create an XML parser
    parser = xml.sax.make_parser()
    # Create an instance of the custom handler
    handler = ConfigHandler()
    # Set the handler for the parser
    parser.setContentHandler(handler)
    # Parse the XML file
    parser.parse('resources/config.xml')
    # Return the parsed data
    return handler.parsed_data

# Example usage
if __name__ == "__main__":
    parsed_result = get_root()
    print(parsed_result)