import datetime

class SupportIssue:
    def __init__(self, user_id, issue_category, specific_details, hardware_software_details="", steps_already_taken="", status="unresolved"):
        self.user_id = user_id
        self.issue_category = issue_category
        self.specific_details = specific_details
        self.hardware_software_details = hardware_software_details
        self.steps_already_taken = steps_already_taken
        self.status = status
        self.interaction_history = []
        self.timestamps = {
            "reported": datetime.datetime.now(),  # Set the reported time to now
            "last_updated": None
        }

    def update_status(self, new_status):
        self.status = new_status
        self.add_interaction(f"Status updated to {new_status}")
        self.timestamps["last_updated"] = datetime.datetime.now()  # Update last updated time

    def add_interaction(self, message):
        self.interaction_history.append(message)
        self.timestamps["last_updated"] = datetime.datetime.now()  # Update last updated time

    def __str__(self):
        history = "\n".join(self.interaction_history)
        return f"Support Issue for User {self.user_id}\nCategory: {self.issue_category}\nStatus: {self.status}\nDetails: {self.specific_details}\nHardware/Software: {self.hardware_software_details}\nSteps Taken: {self.steps_already_taken}\nHistory:\n{history}\nReported: {self.timestamps['reported']}\nLast Updated: {self.timestamps['last_updated']}"

# Example generic usage
if __name__ == "__main__":
    issue = SupportIssue(
        user_id="UserXYZ",
        issue_category="Example Category",
        specific_details="Example issue description.",
    )
    issue.add_interaction("Initial assessment made.")
    issue.update_status("awaiting user response")
    print(issue)
