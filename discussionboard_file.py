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
    def __init__(self, name, email, facilitator_id):
        super().__init__(name, email)
        self.facilitator_id = facilitator_id
        self.created_courses = []

    def create_course(self, title):
        new_course = Course(title, self)
        self.created_courses.append(new_course)
        print(f"facilitator {self.name} created the course: {new_course.title}")
        return new_course

    def view_profile(self):
        super().view_profile()
        print(f"facilitator ID: {self.facilitator_id}")
        print(f"Created Courses: {[course.title for course in self.created_courses]}")

# Course class
class Course:
    def __init__(self, title, facilitator):
        self.title = title
        self.facilitator = facilitator

# Example usage

# Create users
facilitator = Instructor(name="facilitator Joe", email="josephnishimwe398@alustudent.com", facilitator_id="Joe2024")
student = Student(name="Joseph", email="j.nishimwe@alustudent.com", student_id="joseph2024")

# Instructor creates a course
course1 = facilitator.create_course("Python Programming")

# Student enrolls in the course
student.enroll_in_course(course1)

# Display user profiles
print("\n--- Student Profile ---")
student.view_profile()

print("\n--- Facilitator Profile ---")
facilitator.view_profile()
