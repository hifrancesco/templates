import os
import time


events = [
    "branch_protection_rule",
    "check_run",
    "check_suite",
    "create",
    "delete",
    "deployment",
    "deployment_status",
    "discussion",
    "discussion_comment",
    "fork",
    "gollum",
    "issue_comment",
    "issues",
    "label",
    "merge_group",
    "milestone",
    "page_build",
    "project",
    "project_card",
    "project_column",
    "public",
    "pull_request",
    "pull_request_comment",
    "pull_request_review",
    "pull_request_review_comment",
    "pull_request_target",
    "push",
    "registry_package",
    "release",
    "repository_dispatch",
    "schedule",
    "status",
    "watch",
    "workflow_call",
    "workflow_dispatch",
    "workflow_run",
]

keywords = [
    "name: specifies the name of the workflow.",
    "on: specifies the events that trigger the workflow.",
    "jobs: specifies one or more jobs to run as part of the workflow.",
    "steps: specifies a sequence of steps to run as part of a job.",
    "uses: specifies an action or a composite run command to use in the job.",
    "env: specifies environment variables to set for the workflow.",
    "with: provides input parameters for an action or a composite run command.",
    "runs-on: specifies the type of machine or virtual environment to run the job on.",
    "needs: specifies dependencies between jobs in the workflow.",
]


def gh_events(events):
    for i, event in enumerate(events, start=1):
        time.sleep(0.1)
        print(f"{i}. {event}")


def gh_keywords(keywords):
    print("\nname on jobs, steps uses env with runs-on needs\n")
    for i, keyword in enumerate(keywords, start=1):
        time.sleep(0.1)
        print(f"{i}. {keyword}")

if __name__ == "__main__":
    os.system("clear")
    gh_events(events)
    gh_keywords(keywords)
