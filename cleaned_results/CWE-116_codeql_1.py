import re

def filterScriptTags(content):
    '''
    Remove <script> tags and their content from the content argument.
    '''
    # Regular expression to match <script> tags and their content
    script_regex = re.compile(r'<script.*?>.*?</script>', re.DOTALL | re.IGNORECASE)
    
    # Substitute the matched script tags with an empty string
    cleaned_content = re.sub(script_regex, '', content)
    
    return cleaned_content

# Example usage
html_content = '''
<html>
<head>
    <title>Sample Page</title>
    <script type="text/javascript">
        console.log("This is a script.");
    </script>
</head>
<body>
    <h1>Hello, World!</h1>
    <script>
        alert("Another script!");
    </script>
</body>
</html>
'''

cleaned_html = filterScriptTags(html_content)
print(cleaned_html)