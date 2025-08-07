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