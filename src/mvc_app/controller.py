from model import CourseModel
from view import ConsoleView

class AppController:
    def __init__(self):
        self.model = CourseModel()
        self.view = ConsoleView()

    def run(self):
        while True:
            # 1. Ask Model for data
            courses = self.model.get_all_courses()
            # 2. Tell View to render data
            self.view.show_courses(courses)

            # 3. Get user input from View
            user_input = self.view.get_user_input()
            if user_input == 'Q':
                break

            # 4. Route input to Model for processing
            success, msg = self.model.enroll_student(user_input)

            # 5. Tell View to render the result
            self.view.show_message(msg, success)

if __name__ == "__main__":
    app = AppController()
    app.run()
    