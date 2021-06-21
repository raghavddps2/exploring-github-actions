1. Github actions help us automate tasks within the software development life cycle. The github actions are self driven, which implies we can run a series of commands after a specified event has occured.

2. This event may be a push to a specific branch, or when a new pull request is created.

3. An event automatically triggers the workflow, which contains a job. The job then uses steps to control the order in which ations are run. These actions are the commands that automate the testing of the codebase.

4. Workflows are made up of one or more jobs that can be scheduled or triggered by an event.

5. An event is a specific activity that triggers a workflow. For example - A commit/a push etc.

6. A job is basically a set of steps that execute on the same runner. By default, a workflow with multiple jobs will run those jobs in parallel.

7. A step is an individual task that can run commands in a job. A step can either be an action or a shell command. Each step in a job executes on the same runner.
