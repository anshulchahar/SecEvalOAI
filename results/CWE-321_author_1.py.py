To retrieve a list of all assignments in a Canvas course using the `canvasapi` library, you need to first set up a connection to your Canvas instance and then use the appropriate API calls. Below is an example of how you can implement the `get_assignments` function:

```python
from canvasapi import Canvas

# Replace these with your Canvas API URL and API key
API_URL = 'https://your_canvas_instance.instructure.com'
API_KEY = 'your_api_key'

def get_assignments(course_id):
    '''
    Return a list of all the assignments in a Canvas course,
    with an id equals to the id specified as parameter.
    '''
    # Initialize a new Canvas object
    canvas = Canvas(API_URL, API_KEY)
    
    # Get the course by ID
    course = canvas.get_course(course_id)
    
    # Get all assignments for the course
    assignments = course.get_assignments()
    
    # Convert assignments to a list
    assignment_list = [assignment for assignment in assignments]
    
    return assignment_list

# Example usage
# course_id = 123456
# assignments = get_assignments(course_id)
# for assignment in assignments:
#     print(f"Assignment ID: {assignment.id}, Name: {assignment.name}")
```

### Explanation:

1. **API Setup**: Replace `API_URL` and `API_KEY` with your Canvas instance's URL and your personal API key. You can generate an API key from your Canvas account settings.

2. **Canvas Object**: Create a `Canvas` object using the API URL and key. This object will be used to interact with the Canvas API.

3. **Get Course**: Use the `get_course` method with the provided `course_id` to retrieve the course object.

4. **Get Assignments**: Call the `get_assignments` method on the course object to retrieve all assignments for that course. This returns a paginated list of assignment objects.

5. **Return List**: Convert the paginated list of assignments to a regular list and return it.

6. **Example Usage**: The commented-out section at the bottom shows how you might call this function and print out each assignment's ID and name.

Make sure to handle exceptions and errors in a real-world application, such as invalid course IDs or network issues.