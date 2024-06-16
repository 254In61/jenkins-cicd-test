Overview
========
=> Directory contains code that's for setting up Jenkins CI/CD pipeline.
=> Once pipeline works, this code is left as it is.

Theory
======
=> Test Driven Development : Development and testing is reversed. You write your unit tests first, and then implement
code changes until the tests pass.

cicd
====
=> Jenkins used for CICD.
=> Pipeline name = jenkins-python-test-pipeline
=> Pipeline script is from SCM.
   - Jenkinsfile found in cicd/
=> Stages:
    1) clone repo  ** Not needed on the pipeline. Cloning down of Jenkinsfile achieves the stage.
    2) install dependencies 
    3) lint
    4) unittest
    5) integration test
    6) build
    7) ?? what next?
    


Design
=======
1. Git repo : https://github.com/254In61/jenkins-cicd-test.git
