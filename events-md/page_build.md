page_build is a webhook event that's triggered when a GitHub Pages site is built or rebuilt.

When you push changes to a repository that's configured with GitHub Pages, GitHub will build the site and publish it to the Pages URL. The page_build event is triggered when this build process happens.

You can use this event to run a workflow that does something when the site is built or rebuilt. For example, you might want to notify a chat room when a new version of the site is published, or you might want to run some tests on the built site to make sure everything is working correctly.

The payload of the page_build event includes information about the build, such as the commit SHA and the Pages URL of the built site.

```yml
on:
  page_build:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Print Pages URL
        run: echo "Pages URL is ${{ github.event.build.url }}"

```

    This workflow runs a single job that prints the Pages URL of the built site to the console.

