Feature: CONTRIBUTING.md File Existence and Content
  As a contributor
  I want to verify that CONTRIBUTING.md exists and contains essential guidelines
  So that I can understand how to contribute to the project

  Scenario: CONTRIBUTING.md file exists in repository root
    Given the repository root directory
    When I check for CONTRIBUTING.md file
    Then the file should exist at the root

  Scenario: CONTRIBUTING.md contains environment setup section
    Given CONTRIBUTING.md file exists
    When I read the file content
    Then it should contain information about setting up the environment

  Scenario: CONTRIBUTING.md contains test execution section
    Given CONTRIBUTING.md file exists
    When I read the file content
    Then it should contain instructions on running tests

  Scenario: CONTRIBUTING.md contains pull request guidelines
    Given CONTRIBUTING.md file exists
    When I read the file content
    Then it should contain information about opening pull requests

  Scenario: CONTRIBUTING.md is written in Portuguese
    Given CONTRIBUTING.md file exists
    When I read the file content
    Then the content should be predominantly in Portuguese language