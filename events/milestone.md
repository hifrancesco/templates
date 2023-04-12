    The milestone event occurs when a milestone is created, updated, or deleted on a repository or organization.
    This event triggers a workflow run, which allows you to automate tasks based on milestone-related activities.
    The payload of this event contains information about the milestone, including its title, description, state, and due date.
    The action key in the payload specifies the type of activity that triggered the event. The possible values for this key are created, closed, opened, edited, or deleted.
    You can use the types keyword to specify the specific actions that should trigger your workflow. For example, types: [opened, closed] will run your workflow when a milestone is opened or closed.
    The milestone event is useful for automating project management tasks, such as creating or updating issues or pull requests related to a milestone, or notifying team members of milestone updates.