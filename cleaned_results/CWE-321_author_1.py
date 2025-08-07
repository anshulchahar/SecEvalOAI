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