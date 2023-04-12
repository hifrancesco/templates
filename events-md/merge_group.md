    merge_group is a webhook event payload for the GitHub Actions platform.
    This event is triggered when a pull request is added to a merge queue and added to a merge group.
    The checks_requested activity type triggers this event.
    The GITHUB_SHA and GITHUB_REF values for this event are the SHA and Ref of the merge group, respectively.
    This feature is currently in public beta and is subject to change.
    You can limit your workflow runs to specific activity types using the types keyword in the on block of your workflow YAML file.