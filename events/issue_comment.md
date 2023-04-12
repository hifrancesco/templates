    The issue_comment event is triggered when a user comments on an issue or pull request in a repository.
    The event provides information about the comment, such as the comment body, the user who made the comment, and the timestamp of the comment.
    You can use the issue_comment event to automate tasks based on comments made on issues or pull requests, such as assigning labels, closing issues, or notifying team members.
    The issue_comment event has an associated action property that describes the type of action that was taken on the comment. The possible values for action include created, edited, and deleted.
    You can use the if conditional statement to check the action property and perform different actions based on the type of action taken on the comment.
    To use the issue_comment event, you need to define a workflow in your repository's .github/workflows directory, and specify the issue_comment event as the trigger for the workflow.