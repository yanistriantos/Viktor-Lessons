# Define a base class 'CourseContent' to represent general content of a course.
class CourseContent:
    # The constructor initializes each instance with discipline, description, and mentor.
    def __init__(self, discipline, description, mentor):
        self.discipline = discipline
        self.description = description
        self.mentor = mentor

# Define a class 'Course' that inherits from 'CourseContent'.
class Course(CourseContent):
    # The constructor calls the parent class constructor using super()
    # and initializes a list to store lessons related to the course.
    def __init__(self, discipline, description, mentor):
        super().__init__(discipline, description, mentor)
        self.lessons = []

    # Method to add a lesson to the course.
    def add_lesson(self, lesson):
        self.lessons.append(lesson)

# Define a class 'Lesson' that also inherits from 'CourseContent'.
# This represents a specific lesson within a course.
class Lesson(CourseContent):
    # The constructor additionally accepts 'content', specific to the lesson,
    # calling the parent constructor for common attributes.
    def __init__(self, discipline, description, mentor, content):
        super().__init__(discipline, description, mentor)
        self.content = content

# Define a class 'Quiz' that inherits from 'CourseContent',
# representing a quiz that could be part of a course.
class Quiz(CourseContent):
    # The constructor accepts 'questions', specific to the quiz,
    # and calls the parent constructor for common attributes.
    def __init__(self, discipline, description, mentor, questions):
        super().__init__(discipline, description, mentor)
        self.questions = questions

# Define a simple 'Question' class to represent a quiz question.
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Example usage of the classes to create and manipulate a course structure.
python_course = Course("Intro to Python", "A course for beginners.", "Viktor Stefanov")  # Create a Course instance.
# Create a Lesson instance. Note there's a minor typo in the mentor attribute's content.
python_lesson = Lesson("Variables and Data Types", "Learn about different data types in Python.", "Viktor Stefanov", "course content blablabla....")
python_course.add_lesson(python_lesson)  # Add the lesson to the course.

# Display course and its lessons information.
print(f"Course: {python_course.discipline}")
for lesson in python_course.lessons:
    print(f"Lesson: {lesson.discipline}")
