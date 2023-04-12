The issues event is triggered when an issue is created, updated, assigned, labeled, or closed on a repository. Here are the bullet points that explain this event:

    The issues event is triggered when any change happens in an issue on a repository.
    This event includes all the changes made to an issue, such as creating, updating, assigning, labeling, or closing an issue.
    This event can be used to trigger a workflow that performs certain actions based on the changes made to the issue.
    The payload of this event includes information about the issue, such as the title, body, state, labels, assignee, and more.
    You can use the information from the payload to customize your workflow's behavior and take actions accordingly.
    The issues event can be subscribed to by adding it to the on field in your workflow file.