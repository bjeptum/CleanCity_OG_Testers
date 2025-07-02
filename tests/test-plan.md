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

## 4. Test Strategy
| Area                | Type                   | Approach      |
| --------------------| ---------------- |-------------------- |
| *Authentication System* | Functional, Security       | Manual test cases for registration/login, password rules, session handling, role-based access  |
| *Core Functionality*  | Functional, Validation     | Positive/negative tests for scheduling, request tracking, localStorage checks, and error handling                 |
| *Dashboard & Analytics* | Functional, Usability      | Verify dashboard accuracy, charts, gamification, and real-time updates via exploratory and scenario-based testing |
| *Content Management*    | Functional, UX             | Manual test cases for blog posts, comments, community interactions, quizzes, and infographics                     |
| *User Management*     | Functional, Admin          | Role-based testing for user settings, admin panel, feedback/report workflows, and notification logic              |
| *Accessibility*       | Non-functional, Compliance | WCAG 2.1 testing using tools (axe, WAVE), screen reader checks, keyboard-only navigation                          |
| *Cross-browser Testing* | Compatibility              | Validate functionality and UI across Chrome, Firefox, Safari, and Edge                                            |
| **Mobile Responsiveness* | Compatibility, UI/UX       | Test responsive behavior in browser device modes and real mobile devices                                          |
| *Performance Testing**   | Non-functional, Load       | Use Lighthouse and DevTools to evaluate page speed, memory usage, and UI responsiveness                           |
| *Data Persistence*    | Functional, Reliability    | Inspect and validate localStorage usage, data retention, and integrity after reloads/sessions                     |



## 5.  Timeline (STLC Phases)
| Phase              | Date Range     |
|--------------------|----------------|
| Test Planning      | Jun 26 - Jul 2 |
| Test Design        | Jul 3 - Jul 4  |
| Test Execution     | Jul 5 - Jul 10 |
| Test Closure       | Jul 11 - Jul 16|

 ## 6. Team Member Roles

| Name               | Role                    | Responsibilities                                   |Assigned Key Feature |
|--------------------|-------------------------|----------------------------------------------------| ----- |
| Jeptum Brenda     | Test Lead and Tester         | Coordinates tasks, oversees test plan, executes allocated test cases | Dashboard & Analytics |
| Adams Apeh     | Tester       | Designs and executes allocated test cases, Jira setup          | Authentication System |
| Qaqamba Mpumela       | Tester   | Designs and executes allocated test cases | Waste Management |

### Collaboration Notes
- Daily updates via Jira
- Weekly meetings every Wednesday
- Shared documentation and collaboration using GitHub

## 7. Test Environment Setup Notes

## Browsers Used/Installed:
- 

## 8. Devices Used for Testing:
- 

## 9. Tools Installed: Jest/Pytest/Selenium


