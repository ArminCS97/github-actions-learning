# Github Actions

1. The jobs are sequential and need each other
2. There are 2 types of tests that can run concurrently
3. The Jobs:
    1. Pass the tests
    2. needs 1.
   3. 
4. Triggers:
   1. On PUSH
   2. on manual running `workflow_dispatch`