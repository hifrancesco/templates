    The label event is triggered when a label is added or removed from an issue or pull request.
    This event is useful for automating actions based on the labels assigned to an issue or pull request.
    You can use the on keyword to specify that your workflow should be triggered by the label event.
    You can filter the label event based on the action that triggered it. The possible actions are created and deleted.
    You can access information about the label that was added or removed using the github.event context object.
    This event can be used to automate actions like assigning an issue to a specific team based on the label, notifying a Slack channel when a certain label is added, or updating the status of a pull request based on the labels assigned.