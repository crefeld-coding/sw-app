"""Senior Work App Data Management Prototype"""
import time

class studentAccount:
    def __init__(self):
        self.trackers = self.init_trackers()

    def init_trackers(self):
        """Creates list of trackers. Returns a list"""
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

    def get_trackers(self):
        """Copies contents of self.trackers, more secure than directly returning it"""
        trackers = list()
        for tracker in self.trackers:
            trackers.append(tracker.copy())
        return trackers

    def update_tracker(self, tracker_title, entry_index):
        """Changes the entry at entry_index to the current timestamp if null,
            changes the last entry to entry_index if the entry was changed.
            Expects a string and int, returns copy of updated tracker"""
        trackers = self.trackers
        # tests that entry_index between 1:4
        if not (1<=entry_index and entry_index<4):
            # Raises value error
            raise ValueError("Invalid entry_index: must >=1 and <4", f"entry_index = {entry_index}")
        
        for i in range(len(trackers)):
            tracker = trackers[i]
            if tracker[0] == tracker_title:
                # tests that the entry is null, so it doesn't overwrite
                if not tracker[entry_index]:
                    # tests if last entry is an int or string. If not, then entry is too high
                    if type(tracker[entry_index-1])==float or type(tracker[entry_index-1])==str:
                        # sets entry to current timestamp
                        tracker[entry_index] = time.time()
                        if len(tracker) > 2:
                            # doesn't run for math trackers
                            tracker[4] = entry_index
                    else:
                         raise ValueError(f"entry_index {entry_index} is too high, last entry must be updated first")
                else:
                    raise ValueError("Invalid entry_index: entry already filled", f"entry_index = {entry_index}")
                # copies tracker instead of returning the object, more secure
                return tracker.copy()
        # raises a ValueError only if search for tracker failed
        raise ValueError(f"Could not find '{tracker_title}' in list of trackers")


class teacherAccount:
    def __init__(self):
        pass


class guardianAccount:
    def __init__(self):
        pass
