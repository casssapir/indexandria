class SupportIssue:
    def __init__(self, user_id, issue_category, specific_details, hardware_software_details, steps_already_taken, status="unresolved"):
        self.user_id = user_id
        self.issue_category = issue_category
        self.specific_details = specific_details
        self.hardware_software_details = hardware_software_details
        self.steps_already_taken = steps_already_taken
        self.status = status
        self.interaction_history = []
        self.timestamps = {"reported": None, "last_updated": None}

    def update_status(self, new_status):
        self.status = new_status
        self.add_interaction(f"Status updated to {new_status}")

    def add_interaction(self, message):
        self.interaction_history.append(message)
        # Update last_updated timestamp as well, depending on your timestamping approach

    def __str__(self):
        return f"Support Issue for User {self.user_id}\nCategory: {self.issue_category}\nStatus: {self.status}\nDetails: {self.specific_details}\nHardware/Software: {self.hardware_software_details}\nSteps Taken: {self.steps_already_taken}\nHistory: {self.interaction_history}"

# Example usage:
if __name__ == "__main__":
    # Creating a new support issue
    issue = SupportIssue(user_id="User123", issue_category="Charging Issue", specific_details="Car not charging at station", hardware_software_details="Tesla Model 3, ChargePoint Station", steps_already_taken="Tried different cable")
    issue.update_status("awaiting more information")
    issue.add_interaction("Asked user for more details about the charging station.")
    print(issue)
