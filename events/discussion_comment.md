    The discussion_comment event is triggered when a user creates, edits, or deletes a comment on a discussion in a repository.
    This event is only triggered for discussions in public repositories and private repositories that the authenticated user has access to.
    When this event is triggered, a workflow can be run to perform certain actions based on the changes made to the comment, such as sending notifications or updating related data.
    The discussion_comment event has several properties, including the action (created, edited, or deleted), the ID of the comment, the contents of the comment, the user who created the comment, and the timestamp of when the comment was last updated.
    This event can be filtered based on the contents of the comment, the user who created the comment, or the action that was performed on the comment.
    To use the discussion_comment event in a workflow, you need to configure a trigger for the event in your workflow file using the on keyword, along with any necessary filtering criteria.

