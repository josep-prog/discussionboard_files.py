#!/usr/bin/env python3

# Base class for all users (students, instructors)
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def login(self):
        print(f"{self.name} logged in.")
    
    def view_courses(self, courses):
        print(f"{self.name} is viewing the courses:")
        for course in courses:
            print(f"- {course.title}")

    def view_profile(self):
        print(f"Name: {self.name}\nEmail: {self.email}")

# Student class inherits from User
class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id
        self.enrolled_courses = []

    def enroll_in_course(self, course):
        self.enrolled_courses.append(course)
        print(f"{self.name} enrolled in {course.title}")

    def view_profile(self):
        super().view_profile()
        print(f"Student ID: {self.student_id}")
        print(f"Enrolled Courses: {[course.title for course in self.enrolled_courses]}")

# Instructor class inherits from User
class Instructor(User):
    def __init__(self, name, email, instructor_id):
        super().__init__(name, email)
        self.instructor_id = instructor_id
        self.created_courses = []

    def create_course(self, title):
        new_course = Course(title, self)
        self.created_courses.append(new_course)
        print(f"Instructor {self.name} created the course: {new_course.title}")
        return new_course

    def view_profile(self):
        super().view_profile()
        print(f"Instructor ID: {self.instructor_id}")
        print(f"Created Courses: {[course.title for course in self.created_courses]}")

# Course class
class Course:
    def __init__(self, title, instructor):
        self.title = title
        self.instructor = instructor

# Example usage

# Create users
instructor = Instructor(name="Dr. Smith", email="dr.smith@elearning.com", instructor_id="I001")
student = Student(name="Alice", email="alice@student.com", student_id="S001")

# Instructor creates a course
course1 = instructor.create_course("Python Programming")

# Student enrolls in the course
student.enroll_in_course(course1)

# Display user profiles
print("\n--- Student Profile ---")
student.view_profile()

print("\n--- Instructor Profile ---")
instructor.view_profile()


