class ProgressTracker:
    def __init__(self):
        self.metrics = {
            "study": {"daily_target": 2, "completed": 0, "streak": 0}
        }

    def update_progress(self, category, value):
        if category in self.metrics:
            self.metrics[category]["completed"] += value
        return self.get_progress(category)

    def get_progress(self, category):
        if category not in self.metrics:
            return 0
        metric = self.metrics[category]
        return (metric["completed"] / metric["daily_target"]) * 100
 
