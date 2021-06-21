1. We create a new file in the .github/workflows directory named github-actions-demo.yml.

2. In the YAML file, we describe, the name of the action, when the action should be triggered. For ex  - on a push, on a new branch etc.

3. Then we specify the jobs that are required to be performed.`run` is used to run specific commands.

4. It is to be noted that, the repositories can contain multiple workflows, that trigger different jobs based on different events.

5. A good use case of the same is automatic testing of code.