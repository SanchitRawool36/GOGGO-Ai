from datetime import datetime


class ReflectionEngine:
    """
    Learns from completed tasks, failures,
    and successful solutions.
    """

    def __init__(self):

        self.lessons = []

    # ------------------------------------
    # Save Lesson
    # ------------------------------------

    def remember(
        self,
        task: str,
        error: str,
        solution: str,
        success: bool = True,
    ):

        lesson = {
            "time": datetime.now(),
            "task": task,
            "error": error,
            "solution": solution,
            "success": success,
        }

        self.lessons.append(lesson)

        return lesson

    # ------------------------------------
    # Search Lessons
    # ------------------------------------

    def search(self, keyword: str):

        results = []

        keyword = keyword.lower()

        for lesson in self.lessons:

            text = (
                lesson["task"]
                + " "
                + lesson["error"]
                + " "
                + lesson["solution"]
            ).lower()

            if keyword in text:

                results.append(lesson)

        return results

    # ------------------------------------
    # Print Lessons
    # ------------------------------------

    def show_all(self):

        return self.lessons

    # ------------------------------------
    # Total Lessons
    # ------------------------------------

    def count(self):

        return len(self.lessons)