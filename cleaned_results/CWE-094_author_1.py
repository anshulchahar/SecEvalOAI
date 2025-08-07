@app.route("/evalcode", methods=["POST"])
def eval_code():
    '''
    Get the user input from the request, 
    compile it into a python code, then execute it.
    '''
    code = request.form.get('code', '')
    try:
        # Compile the code
        compiled_code = compile(code, '<string>', 'exec')
        # Execute the compiled code
        exec(compiled_code)
        return "Code executed successfully", 200
    except Exception as e:
        return str(e), 400