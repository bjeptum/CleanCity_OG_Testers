# 🧪 CleanCity QA Project: Test Plan & Strategy

## 1. Objective
Plan and execute comprehensive testing for CleanCity - Waste Pickup Scheduler web application.

## 2. Scope
- Functional testing of authentication, scheduling, dashboard, and admin features.
- Non-functional testing: performance, accessibility, and compatibility.
- Testing on multiple browsers (Chrome, Firefox, Safari, Edge) and devices (desktop, tablet, mobile).
- No backend testing (localStorage only).

## 3. Tools
- **Manual Testing:** Browser DevTools, localStorage inspection
- **Project Management:** Jira
- **Accessibility:** axe DevTools, WAVE
- **Performance:** 
- **Documentation:** Markdown in `tests/` folder, GitHub issues for bugs

## 4. Testing Workflow

### (a) Epic Assignment

 Each team members selects a Jira Epic and focus on the associated features and test areas.
 
### (b) Test Case Creation

 Test cases are then documented in a tabular format in Markdown or spreadsheet form and stored under the tests/ directory.
 
 The table includes:
 
  (i) Test Case : Linked Requirement ID (e.g., FR-003)

  (ii) Test Type

  (iii) Tool

  (iv) Steps

  (v) Expected Result

  (vi) Actual Result : Pass/Fail Status
  

### (c) Test Execution & Defect Logging

Test Execution

Run tests (manual and/or automated) based on the defined test cases.

Ensure results are updated in the test case table (Pass/Fail and Actual Result).

### Defect Logging

Log any bugs or issues in the `tests/defect-log.md` file, including the following fields:

  - Defect ID
  - Summary
  - Severity
  - Steps to Reproduce
  - Linked Test Case

>  Ensure defects are clearly described and linked back to relevant test cases or functional requirements.

### Challenges

Note any challenges, blockers, or unexpected behaviors encountered during test execution.

Document them either:
  - In `tests/defect-log.md` under a "Challenges Faced" section, or
  - Inline within the related test case file as a comment or footnote

### Automation Scripts

Store all automation test scripts in the `tests/test_scripts/` directory.

Ensure:
  - Scripts are clearly named e.g.: `test_login_form_validation.js`
  - Scripts are traceable to functional requirements and test cases.
  - Add references or comments at the top of each script indicating the FRs and test cases covered.

## 5. Test Strategy

Test Strategy for the waste management platform involved creating epics on Jira (project management tool) then mapping each to functional requirements (FRs) to ensure complete coverage and easy tracing of the activities.

##  Test Strategy Overview 

| ** Jira Epic** | **Test Area** | **Test Type** | **Test Approach** | **Functional Requirements Covered** |
|----------|---------------|---------------|-------------------|-------------------------------------|
| **Epic 1: Authentication System Testing** | User Registration, Login, Logout, Role Access | Functional, Security | Manual and automated test cases for field validation, session management, and role restrictions. Includes positive, negative, and edge case testing. | FR-001 to FR-011 |
| | Session Handling | Functional | LocalStorage checks, session expiry, redirection logic | FR-006, FR-007, FR-008 |
| | Security Validation | Security | OWASP checks for input validation, XSS/SQLi attempts | FR-002, FR-082, FR-083 |
| **Epic 2: Waste Management Testing** | Pickup Scheduling | Functional, Business Rules | Validate scheduling logic (date, quantity, type), and input validation. Use boundary, positive/negative testing. | FR-012 to FR-015, BR 14.1 |
| | Request Management | Functional | CRUD operations on pickup requests and status validation | FR-016 to FR-019 |
| | Request Tracking | Functional | Simulate backend status changes, verify real-time updates, notifications, and feedback flow | FR-020 to FR-022 |
| **Epic 3: Dashboard & Analytics Testing** | User Dashboard | Functional, Usability | Manual and scenario-based tests for personalized dashboard info, real-time updates, and environmental impact metrics | FR-023 to FR-024 |
| | Analytics & Reports | Functional, Export Validation | Test visual accuracy of charts, leaderboards, trends, and CSV exports | FR-025 to FR-028 |
| | Gamification | Functional, UI | Validate badge awarding logic, level progress, and activity-based scoring | FR-029 to FR-030 |
| **Epic 4: Content Management Testing** | Blog System | Functional, UX | Create, update, and interact with blog posts; validate category/tag logic | FR-035 (implied), 6.1 |
| | Awareness Section | Functional, UX | Validate quiz logic, rotating tips, explanations, and interactivity | FR-036 to FR-040 |
| | Infographics | UI, Accessibility | Visual verification, alt text checks, and responsiveness | FR-039, FR-073 |
| **Epic 5: Community Features Testing** | Community Feed | Functional, Social | Manual and exploratory testing of post creation, interaction (like, comment), ordering, and moderation flows | FR-041 to FR-044 |
| | User Profiles | Functional, Usability | Edit, view stats, upload profile picture, and environmental history | FR-045 to FR-048 |
| | Social Features | Functional | Follow/unfollow logic, news feed validation, sharing, and community challenge rules | FR-049 to FR-052 |
| **Epic 6: Admin Functions Testing** | Request & User Management | Functional, Role-Based Access | Admin-only tests for approval flows, user role changes, account actions, filtering and reporting | FR-053 to FR-060 |
| | Content Moderation | Functional, Security | Admin workflows for flagged content, deletions, and announcements | FR-061 to FR-064 |
| | Role Validation | Functional, Security | Admin visibility and access tests, especially for restricted screens | FR-010, FR-058, BR 14.2 |
| **Epic 7: Non-Functional Testing** | Accessibility | Compliance, Usability | WCAG 2.1 AA checks via tools (axe, WAVE), keyboard-only navigation, screen reader testing | FR-071 to FR-074 |
| | Mobile Responsiveness | Compatibility, UI | Responsive testing on various screen sizes and mobile devices | FR-069 to FR-070 |
| | Cross-browser Testing | Compatibility | Visual and functional tests across Chrome, Firefox, Edge, Safari | FR-086 |
| | Performance Testing | Load, UI Responsiveness | Use Lighthouse and DevTools to validate page speed, load time, and responsiveness | FR-084 to FR-085 |
| | Data Persistence & Validation | Functional, Security | Validate localStorage usage, session continuity, input validation, and XSS/SQLi protections | FR-078 to FR-083 |
| | Error Handling | Functional, UX | Real-time form validation, user-friendly error messages, and recovery flows | FR-087 to FR-092 |
| | Notifications | Functional | Validate unread counters, categories, and notification history | FR-065 to FR-068 |
| | Support & Logging | Functional | Check help tooltips, FAQ links, and activity/error logging | FR-093 to FR-097 |


## 7.  Timeline (STLC Phases)
| Phase              | Date Range     |
|--------------------|----------------|
| Test Planning      | Jun 26 - Jul 2 |
| Test Design        | Jul 3 - Jul 4  |
| Test Execution     | Jul 5 - Jul 10 |
| Test Closure       | Jul 11 - Jul 16|

 ## 8. Team Member Roles

| Name               | Role                    | Responsibilities                                   |Assigned Key Feature |
|--------------------|-------------------------|----------------------------------------------------| ----- |
| Jeptum Brenda     | Test Lead and Tester         | Coordinates tasks, oversees test plan, executes allocated test cases | Dashboard & Analytics |
| Adams Apeh     | Tester       | Designs and executes allocated test cases, Jira setup          | Authentication System |
| Qaqamba Mpumela       | Tester   | Designs and executes allocated test cases | Waste Management |

### Collaboration Notes
- Daily updates via Jira
- Weekly meetings every Wednesday
- Shared documentation and collaboration using GitHub

## 9. Test Environment Setup Notes

## Browsers Used/Installed:
- Google Chrome - Brenda
- Firefox - Adams
- Safari - Qaqamba/ Brenda
- Microsoft Edge - Qaqamba

## 10. Devices for Testing:
- Laptop(Windows 11/10) - Qaqamba
- Laptop(Linux) - Brenda
- iOS device for Safari - Qaqamba/Brenda
- Android(Samsung Galaxy A32) - Adams

## 11. Tools Installed: 

| **Tool**     | **Purpose**                          |
| ------------ | ------------------------------------ |
| Jest     | Unit & component-level testing       |
| Selenium | Automation for end-to-end UI testing |



