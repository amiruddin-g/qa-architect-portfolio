# GitHub Actions CI

GitHub Actions integration for Continuous Integration and execution of workflows.
This workflow uses workflow_dispatch (manual trigger) in Docker for the pytest test cases. 

## How to Trigger

- Navigate to your GitHub repo in browser, open Actions.
- A workflow named CI will be on the left.
- Open it and click 'Run workflow'.
- It should follow the steps in your yml file and produce output if success and error if failed.

## What the workflow does

- Workflow checkout the code, means clones the repo on the GitHub-hosted Ubuntu runner.
- Build the docker image.
- Runs 9 pytest tests inside the container.

All happens within GitHub servers while local Docker setup left untouched.

## Local Docker vs GitHub Actions Docker

### Local Docker (your machine):

- Local setup gives faster feedback, test before push.
- Faster debug without waiting for CI to complete.
- Dockerfile verification before committing.


### GitHub Actions Docker:

- Can be triggered from anywhere, no machine dependency.
- Runs automatically on every actions specified (Push/PR) or manually.
- Team can be assured that it works for all and not just on their machine.
