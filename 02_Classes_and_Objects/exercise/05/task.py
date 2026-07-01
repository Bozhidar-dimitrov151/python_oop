class Task:
    completed = False
    def __init__(self, name, due_date, comments: list):
        self.name = name
        self.due_date = due_date
        self.comments = comments

    def change_name(self, new_name):
        self.name = new_name
        return self.name

    def change_due_date(self, new_date: str):
        self.due_date = new_date
        return self.due_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number >= len(self.comments):
            return "Cannot find comment."

        self.comments[comment_number] = new_comment
        return ', '.join(self.comments)

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"