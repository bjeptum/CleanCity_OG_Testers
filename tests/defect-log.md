
## DEFECTS 
**Title**: View achievements button

**Jira/GitHub (Bug) Link**: [Defect](https://adamsapeh35.atlassian.net/browse/SCRUM-81)

**Requirement Affected**: FR-051: The system shall allow users to share achievements and milestones.

**Severity**: Medium

**Summary**:  
 User earned badges/achievements are not displayed. There is no button to click to navigate to participation.
 .
--------------------------------------------

**Title**: Acceptance of invalid details

**Jira/GitHub (Bug) Link**: [Defect](https://github.com/bjeptum/CleanCity_OG_Testers/issues/2)

**Requirement Affected**: The application should display an error message like "Invalid email format" for invalid inputs

**Severity**: High

**Summary**:  The application accepts invalid email formats (short email addresses) without displaying an error message.

[After logging in with a short email address]![short email](<Screenshot 2025-07-14 205313.png>)
--------------------------------------------

**Title**: User login in Node.js and HTML version

**Jira/GitHub (Bug) Link**: [Defect](https://github.com/bjeptum/CleanCity_OG_Testers/issues/3)

**Requirement Affected** The application should display an error message like "Invalid email & password" in both application versions if the user in not registered

**Severity**: High

**Summary**:  When a user is not registered and logs, the HTML version displays an error message for invalid details, but the Node.js version doesn't. This allows invalid data into the system which risks account security and causing confusion for users.
 
 [Successful login in Node.js]![New unregistered user](<Screenshot 2025-07-16 110059.png>) ![alt text](<Screenshot 2025-07-16 110127.png>)
 [Unsuccessful login in HTML version]![alt text](<Screenshot 2025-07-16 113147.png>)
 --------------------------------------------

**Title**: Password error handling and guide format

**Jira/GitHub (Bug) Link**: [Defect](https://github.com/bjeptum/CleanCity_OG_Testers/issues/4)

**Requirement Affected** Should display an error message like "Password too short" and the correct format of after entering an invalid form

**Severity**: High

**Summary**:  The application allows passwords as short as one letter without warning or guidance. Short passwords are a major security risk and it makes accounts vulnerable to attacks and unauthorized access.

[1-letter password]![See the terminal for a succeful login](<Screenshot 2025-07-14 025106.png>)
 --------------------------------------------

**Title**: Pickup request reflection for users in Node.js version

**Jira/GitHub (Bug) Link**: [Defect](https://github.com/bjeptum/CleanCity_OG_Testers/issues/6)

**Requirement Affected** Pickup request made by a user does not appear on the dashboard after being logged (in Node.js version), and after a request is logged it should be displayed on the dashboard.

**Severity**: High

**Summary**:  Pickup requests do not appear on the dashboard after being logged in the Node.js version. Therefore users and admins cannot track or manage requests and this will lead to missed pickups and poor service reliability.

[Scheduled pickup]![Node.js version](<Screenshot 2025-07-16 112459.png>)![successful log](<Screenshot 2025-07-16 112518.png>)![Request is not reflected](<Screenshot 2025-07-16 112542-1.png>)
 --------------------------------------------

**Title**: Cancelling, Editing and Deleting requests

**Jira/GitHub (Bug) Link**: [Defect](https://github.com/bjeptum/CleanCity_OG_Testers/issues/7)

**Requirement Affected** Requested pickups cannot be cancelled, edited and deleted (in HTML version) and options should appear to cancel, edit or delete a request when it is clicked.
NOTE: this could not be verified in Node.js version because requests do not reflect there, see the previous bug.

**Severity**: High

**Summary**:  This limits the user and the admin because this will result in service complications and bad review for the application. 
[User's perspective]![alt text](<Screenshot 2025-07-16 113431.png>) [Admin's perspective]![alt text](<Screenshot 2025-07-16 122344.png>)

 --------------------------------------------

**Title**: Functionality of the edit-button for requests for the admin role

**Jira/GitHub (Bug) Link**: [Defect](https://github.com/bjeptum/CleanCity_OG_Testers/issues/8)

**Requirement Affected** Edit button does not respond when clicked by the admin (in HTML version). The edit button should respond to its function by resulting in the edit field/window being opened
NOTE: this could not be verified in Node.js version because requests do not reflect there, see the previous bug.

**Severity**: High

**Summary**:  This limits the user and the admin because this will result in service complications and bad review for the application.  
[Admin Edit button] ![alt text](<Screenshot 2025-07-16 122344-1.png>)

