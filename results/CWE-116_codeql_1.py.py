To remove `<script>` tags from a given string, you can use regular expressions with the `re` module in Python. Here's a function that accomplishes this:

```python
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
```

### Explanation:
- The regular expression `r'<script.*?>.*?</script>'` is used to match `<script>` tags and their contents. 
  - `<script.*?>` matches the opening `<script>` tag with any attributes.
  - `.*?` matches any content inside the script tags, non-greedily.
  - `</script>` matches the closing `</script>` tag.
- The `re.DOTALL` flag allows the `.` to match newline characters, ensuring that multi-line scripts are captured.
- The `re.IGNORECASE` flag makes the matching case-insensitive, so it will match `<SCRIPT>`, `<script>`, etc.
- `re.sub()` is used to replace the matched script tags and their content with an empty string, effectively removing them from the input content.