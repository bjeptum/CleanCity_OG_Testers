# Project: CleanCity web application testing
### Testers/Members*:@adamsap1 @bjeptum @Qaqamba-M
### Date Due: 16 July 2025

### Tools:
### Environment:

## Techniques

| Category                   | Techniques Applied                                                                                                   |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Functional Testing**     | - Equivalence Partitioning  <br> - Boundary Value Analysis  <br> - State Transition Testing <br> - Black Box Testing |
| **Non-Functional Testing** | - Performance Testing  <br> - Responsiveness Testing <br> - Accessibility Testing                                    |
| **Test Automation**        | - Selenium for UI automation <br> - Pytest & Jest for backend/logic validation                                       |
| **Manual Testing**         | - Used for validation of UI messages, edge cases, and error handling                                                 |

## Testing Approach

| Phase                   | Details                                                                      |
| ----------------------- | ---------------------------------------------------------------------------- |
| **Requirement-Based**   | Test cases were derived from specific functional requirements (FR codes).    |
| **Role-Based Access**   | Tested access and restrictions based on roles (Admin vs. User).        |
| **Data-Driven Testing** | Validated various input combinations (short/long names, passwords).    |
| **Cross-Platform**      | Login performance was tested across browsers and devices.                    |
| **UI/UX Validation**    | Verified responsiveness, error messages, session persistence, and redirects. |
| **State-Based Testing** | Focused on user session handling, logout, redirection, and storage logic.    |

## Key Features Tested

| Area                            | Coverage                                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------------- |
| **Authentication**              | Registration (valid/invalid inputs), Login, Logout, Session storage, Role restrictions        |
| **Scheduling System**           | Pickup scheduling (validations, auto-fill, clashes), Time slot selection                      |
| **Admin Dashboard**             | View/manage/cancel/approve pickups, assign schedules, filter/search requests, user management |
| **User Dashboard**              | Recent activities, achievement badges         |
| **Blog System**                 | Viewing posts, interacting (like/comment), CRUD operations, tagging system                    |
| **Gamification Features**       | Awarding badges based on actions (first pickup, perfect recycling)                      |
| **Community Features**          | View/edit profile, upload profile picture, view achievements & news feed                      |
| **Performance & Accessibility** | Submission speed, layout responsiveness, Lighthouse score (>90), device/browser compatibility |

## DEFECTS 
**Title**: View achievements button

**Jira/GitHub (Bug) Link**: [Defect](https://adamsapeh35.atlassian.net/browse/SCRUM-81)

**Requirement Affected**: FR-051: The system shall allow users to share achievements and milestones.

**Severity**: Medium
--------------------------------------------

**Title**: Acceptance of invalid details

**Jira/GitHub (Bug) Link**: [Defect](https://github.com/bjeptum/CleanCity_OG_Testers/issues/2)

**Requirement Affected**: The application should display an error message like "Invalid email format" for invalid inputs

**Severity**: High
 --------------------------------------------

**Title**: User login in Node.js and HTML version

**Jira/GitHub (Bug) Link**: [Defect](https://github.com/bjeptum/CleanCity_OG_Testers/issues/3)

**Requirement Affected** The application should display an error message like "Invalid email & password" in both application versions if the user in not registered

**Severity**: High
 --------------------------------------------

**Title**: Password error handling and guide format

**Jira/GitHub (Bug) Link**: [Defect](https://github.com/bjeptum/CleanCity_OG_Testers/issues/4)

**Requirement Affected** Should display an error message like "Password too short" and the correct format of after entering an invalid form

**Severity**: High

**Title**: Pickup request reflection for users in Node.js version

**Jira/GitHub (Bug) Link**: [Defect](https://github.com/bjeptum/CleanCity_OG_Testers/issues/6)

**Requirement Affected** Pickup request made by a user does not appear on the dashboard after being logged (in Node.js version), and after a request is logged it should be displayed on the dashboard.

**Severity**: High
 --

**Title**: Cancelling, Editing and Deleting requests

**Jira/GitHub (Bug) Link**: [Defect](https://github.com/bjeptum/CleanCity_OG_Testers/issues/7)

**Requirement Affected** Requested pickups cannot be cancelled, edited and deleted (in HTML version) and options should appear to cancel, edit or delete a request when it is clicked.
NOTE: this could not be verified in Node.js version because requests do not reflect there, see the previous bug.

**Severity**: High

 --------------------------------------------

**Title**: Functionality of the edit-button for requests for the admin role

**Jira/GitHub (Bug) Link**: [Defect](https://github.com/bjeptum/CleanCity_OG_Testers/issues/8)

**Requirement Affected** Edit button does not respond when clicked by the admin (in HTML version). The edit button should respond to its function by resulting in the edit field/window being opened. [See the defect shown in the video this Jira scrum https://adamsapeh35.atlassian.net/browse/SCRUM-57]
NOTE: this could not be verified in Node.js version because requests do not reflect there, see the previous bug.

**Severity**: High



## Reflection

