"""
Your task: For each of these function signatures, write a detailed user-level
description of what the function does, when you'd use it, and what problem
it solves. Don't implement them - focus on their purpose and use cases.
"""

def merge_sorted_lists(list1, list2):
    """
    Combines two already-sorted lists into a single sorted list.
    Useful when you have separate sorted datasets (like rankings or timestamps) 
    that need to be combined while maintaining order.

    Args:
        list1 (list): First sorted list
        list2 (list): Second sorted list

    Returns:
        list: A new sorted list combining elements from both inputs while 
        maintaining sorted order

    Example use case:
        Merging two sorted lists of customer orders by timestamp, or
        combining ranked player scores from different tournaments
    """
    pass

def group_by_frequency(items):
    """
    Takes a collection of items and creates groups based on how often each
    item appears. Used for finding popular items, identifying duplicates,
    or analyzing patterns in data.

    Args:
        items (list, tuple): Collection of items to analyze (e.g., product names,
        user actions, or any repeatable items)

    Returns:
        dict: Groups items by their frequency. Keys are frequencies (1 for items
        that appear once, 2 for items appearing twice, etc.), and values are
        lists of items with that frequency

    Example use case:
        Finding most common customer purchases, identifying frequently
        repeated words in text, or finding duplicate files in a directory
    """
    pass

def validate_document_structure(document):
    """
    Checks if a text document follows required formatting rules and structure
    before processing. Helps prevent errors by ensuring the document meets
    expected standards.

    Args:
        document (str): Path to the text file to validate

    Returns:
        bool: True if document structure is valid, False otherwise

    Example use case:
        Validating CSV files before importing data
        Checking if log files follow the correct format
        Ensuring configuration files have all required sections
    """
    pass



"""
User-level description:
You're building a class scheduling system. Each teacher has a schedule of classes
they teach. When a new teacher joins with similar qualifications, they should
get a modified version of an existing teacher's schedule.

The new schedule should:
- Keep the same class times and rooms
- Reset all student lists to empty
- Maintain the subject names
"""

original_schedule = {
    'period_1': {
        'subject': 'Math',
        'room': '101',
        'students': ['Alice', 'Bob', 'Charlie']
    },
    'period_2': {
        'subject': 'Physics',
        'room': '102',
        'students': ['David', 'Eve']
    }
}

# Your task: Create a function that makes a new schedule for another teacher
# based on the original schedule. Consider what type of copy you need.

# Since the list we need to change is nested, we need a deep copy because shallow copies keep the reference to the original inner lists
import copy

def change_schedule(original_schedule):
    """
    Creates a new teacher schedule based on an existing one.
    Maintains class times, rooms, and subjects but starts with empty student lists.
    
    Args:
        original_schedule (dict): The source teacher's schedule
    
    Returns:
        dict: A new schedule with empty student lists
    """
    new_schedule = copy.deepcopy(original_schedule)
    for period, info in new_schedule.items():
        info['students'].clear()
    return new_schedule

new_schedule = change_schedule(original_schedule)
print()
print(new_schedule)
print()
print(original_schedule)


"""
User-level description:
You're building a classroom grade tracker. Each class has multiple students,
and each student has multiple assignments. You need to find students who have
improved over time (their latest assignment score is higher than their first).

Data structure:
classroom = {
    'period_1': {
        'John': [75, 82, 90],
        'Maya': [95, 92, 88],
        'Alex': [80, 85, 85]
    },
    'period_2': {
        'Sarah': [70, 80, 85],
        'Tom': [85, 82, 80]
    }
}

Your task: Create a function that returns a list of tuples: (period, student_name)
for all students who showed improvement

[
    (period, student_name),
    (period, student_name),
    (period, student_name)
]

Algorithm:
- For each student, find the latest assignment score and subtract it from the first score
- Get the names and period of each student where the delta is positive 
"""

classroom = {
    'period_1': {
        'John': [75, 82, 90],
        'Maya': [95, 92, 88],
        'Alex': [80, 85, 85]
    },
    'period_2': {
        'Sarah': [70, 80, 85],
        'Tom': [85, 82, 80]
    }
}

# Using a loop
result = []
for period, students in classroom.items():
    for student, grades in students.items():
        improvement = grades[-1] - grades[0]
        if improvement > 0:
            result.append(tuple([period, student]))

# Using a comprehension
[tuple([period, student]) for period, students in classroom.items()
                          for student, grades in students.items()
                          if grades[-1] - grades[0] > 0
]


"""
User-level description:
You're analyzing customer data. Each customer has a list of past order amounts.
You need to identify which customers are "premium" customers (those whose average
order amount is above $100).

Given a list of customer data where each customer is represented as [name, [order_amounts]],
return a list of premium customer names.
"""

customers = [
    ["Alice", [120, 80, 140, 160]],
    ["Bob", [50, 60, 70, 80]],
    ["Carol", [200, 180, 160]],
    ["David", [90, 110, 70]]
]

# Your task: Use a list comprehension to create a list of premium customer names
[customer[0] for customer in customers if sum(customer[1])/len(customer[1]) > 100]

[name for name, orders in customers if sum(orders)/len(orders) > 100]

def get_average(numbers):
    return sum(numbers)/len(numbers)

[name for name, orders in customers if get_average(orders) > 100]