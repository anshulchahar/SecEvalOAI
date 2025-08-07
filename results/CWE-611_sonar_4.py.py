To parse an XML file using the `xml.sax` module in Python, you need to define a custom content handler class that extends `xml.sax.ContentHandler`. This handler will process the XML elements as they are encountered by the parser. Here's how you can implement the `get_root` function to parse an XML file and return the parsed result:

```python
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
```

### Explanation:

1. **Custom Content Handler**: We define a `ConfigHandler` class that extends `xml.sax.ContentHandler`. This class will handle the XML parsing events.

2. **startElement**: This method is called when an opening tag is encountered. We initialize a list in `parsed_data` for each tag to store its content.

3. **endElement**: This method is called when a closing tag is encountered. We reset `current_data` to an empty string.

4. **characters**: This method is called with the text content of an element. We append this content to the list associated with the current tag in `parsed_data`.

5. **get_root Function**: This function creates an XML parser, sets the content handler, and parses the XML file. It returns the `parsed_data` dictionary containing the parsed XML content.

This code will parse the XML file and store the content of each element in a dictionary, where