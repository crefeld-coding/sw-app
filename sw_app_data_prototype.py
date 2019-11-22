"""Senior Work App Data Management Prototype"""

class studentAccount:
    def __init__(self):
        self.trackers = self.init_trackers()

    def init_trackers(self):
        """Creates list of trackers. Expects None, returns a list"""
        ### Standard format:
        ### [title, time started, time in progress, time completed, current status]
        trackers = [
            # Formal Writing
            ["Literary Analysis", None, None, None, None],
            ["Timed Persuasive Essay", None, None, None, None],
            # Transition
            ["Personal Transition Plan", None, None, None, None],
            # Research and Understanding
            ["History Oral Exam", None, None, None, None],
            ["Research Paper", None, None, None, None],
            ["Science Project", None, None, None, None],
            ["Technology", None, None, None, None],
            # Self Reflection
            ["Personal Learning Reflection", None, None, None, None],
            ["Creative Expression", None, None, None, None],
            ["Public Presentation", None, None, None, None],
            # Citizenship
            ["Civics Exam", None, None, None, None],
            ["Independent Service Learning", None, None, None, None],
            ["Leadership", None, None, None, None],
            ### Math format: [name, time completed]
            # Math
            ["CANS Test", None],
            ["Algebra Test", None],
            ["Geometry Test", None]
            ]
        return trackers


class teacherAccount:
    def __init__(self):
        pass


class guardianAccount:
    def __init__(self):
        pass
