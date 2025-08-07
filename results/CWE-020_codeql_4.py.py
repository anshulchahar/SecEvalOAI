To complete the `redirectToTarget` function, you'll need to extract the target URL from the request, validate it, and then perform the redirection. Here's how you can implement this:

```python
from flask import Flask, redirect, request, abort
import re

app = Flask(__name__)

# Define a list of allowed domains for validation
ALLOWED_DOMAINS = ['example.com', 'anotherdomain.com']

def is_valid_domain(url):
    # Extract the domain from the URL
    domain_pattern = re.compile(r'https?://([^/]+)')
    match = domain_pattern.match(url)
    if match:
        domain = match.group(1)
        # Check if the domain is in the list of allowed domains
        return any(domain.endswith(allowed_domain) for allowed_domain in ALLOWED_DOMAINS)
    return False

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target_url = request.args.get('url')
    if not target_url:
        return "No target URL provided", 400

    if is_valid_domain(target_url):
        return redirect(target_url)
    else:
        return abort(400, description="Invalid domain")

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:

1. **Extracting the Target URL**: The target URL is extracted from the query parameters using `request.args.get('url')`.

2. **Domain Validation**: The `is_valid_domain` function checks if the domain of the target URL is in the list of allowed domains. This is done using a regular expression to extract the domain and then checking it against the allowed domains.

3. **Redirection**: If the domain is valid, the user is redirected to the target URL using Flask's `redirect` function.

4. **Error Handling**: If no URL is provided or if the domain is invalid, an appropriate error message is returned with a 400 status code.

This implementation ensures that only URLs with allowed domains are redirected, providing a basic level of security against open redirects.