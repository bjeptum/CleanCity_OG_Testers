# Test cases for User Authentication

## Functional Testing
| **Test Cases**    | **Description**                                        | **Test Type**            | **Tool**                     | **Steps**                                                                    | **Expected Result**                     | **Results**                                                                                 |
| ----------------- | ------------------------------------------------------ | ------------------------ | ---------------------------- | ---------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------- |
| FR001-01 & FR-003 | Register with valid data and create a new User account | Equivalence partitioning | Selenium (Automated), Manual | Fill all required fields correctly                                           | Account created with "User" role        | Account is created successfully, but no message for a successful registration is displayed. |
| FR001-02          | Register with invalid email                            | Equivalence partitioning | Selenium, Manual             | 1. Enter invalid email (missing .com)<br>2. Click Register                   | Error: "Invalid email format"           | No error message is displayed. Page redirects to login page.                                |
| FR001-03          | Register with an empty email field                     | Boundary Analysis        | Selenium                     | 1. Leave the email field empty<br>2. Click Register                          | Error: "Please enter an email"          | “Please fill out the field” message is displayed.                                           |
| FR001-04          | Input unidentical passwords during registration        | Equivalence partitioning | Selenium                     | Mismatch password & confirm                                                  | Error: "Passwords do not match"         | Password confirmation not required during registration                                      |
| FR002-01          | Leave full name empty                                  | Equivalence partitioning | Selenium                     | Leave full name blank                                                        | Error: "Full name is required"          | “Please fill out this field” is displayed.                                                  |
| FR002-02          | Enter long name > 50 chars                             | Boundary value Analysis  | Selenium                     | Input a long name                                                            | Error: "Full name too long"             | No error message. Page redirects to login page.                                             |
| FR002-03          | Enter short name < 50 chars                            | Boundary value Analysis  | Selenium                     | 1. Enter 1-letter name<br>2. Click Register                                  | Error: "Full name too short"            | No error message. Page redirects to login page.                                             |
| FR002-04          | Empty password field                                   | Equivalence partitioning | Selenium                     | 1. Leave password field empty<br>2. Click Register                           | Error: "Please enter a password"        | “Please fill out this field” message is displayed.                                          |
| FR002-04          | Password < 8 chars                                     | Boundary value Analysis  | Selenium                     | 1. Enter a 1-letter password<br>2. Click Register                            | Error: "Password too short"             | No error message. Page redirects to login page.                                             |
| FR002-05          | Password > 8 chars                                     | Boundary value Analysis  | Selenium                     | 1. Enter 15-character password<br>2. Click Register                          | Error: "Password too long"              | No error message. Page redirects to login page.                                             |
| FR-004            | Login registered user with valid details               | Equivalence partitioning | Selenium                     | 1. Enter registered user details<br>2. Click Login                           | Display: “Login successful”             | Redirected to profile page                                                                  |
| FR-005            | Login with invalid details                             | Equivalence partitioning | Selenium                     | 1. Enter invalid user details<br>2. Click Login                              | Display: “Invalid user details entered” | No error message. Redirected to profile page.                                               |
| FR010-01          | Admin role can access admin page                       | Boundary value Analysis  | Selenium                     | 1. Login as admin<br>2. Redirect to admin page                               | Access granted                          | “Login successful! Redirecting...” then admin page loads                                    |
| FR011-01          | Normal user restricted from admin                      | Boundary value Analysis  | Selenium                     | 1. Login as user<br>2. Try to access admin page                              | Error/Access denied                     | No admin button in nav bar. Error in terminal.                                              |
| FR006             | User session is maintained in localStorage             | State transition testing | DevTools                     | 1. Login 2. Check Local Storage  3. Refresh 4. Logout 5. Re-check | Session data remains until logout       | Session not saved in localStorage                                                           |
| FR007             | Redirect after login                                   | State transition testing | Selenium                     | Visit restricted page, login                                                 | Redirect to intended page               | Redirected to profile page                                                                  |
| FR008             | Logout clears session                                  | State transition testing | DevTools                     | 1. Login 2. Check Local Storage 3. Logout 4. Re-check               | Clears session from Local Storage       | Session cleared as expected                                                                 |
| FR009             | Redirect to login after logout                         | State transition testing | Selenium                     | Click Logout button                                                          | Redirected to login page                | Redirected to landing page instead                                                          |

## Non-functional Testing

| Test Case                | Test Type        | Tool                              | Steps                                             | Expected Result                                |
|--------------------------|------------------|-----------------------------------|--------------------------------------------------|-------------------------------------------------|
| Registration performance | Non-Functional   | DevTools (Network tab)            | Register → Measure response time                 | Should be < 1.5 seconds                         |
| Login performance in browsers | Non-Functional   | Microsoft Edge, Chrome, Safari    | Open the web application in different browsers   | Web application remains responsive              |
| Login performance in devices  | Non-Functional   | Laptop, mobile device             | Open the web application in different devices    | Web application and layout remains responsive   |


# Test Cases for Waste Management

## Pick-up Scheduling

| Test Case | Description                                  | Type                    | Tool               | Steps                                           | Expected Result                                 |
|-----------|----------------------------------------------|-------------------------|--------------------|--------------------------------------------------|--------------------------------------------------|
| FR012-01  | Schedule pickup with all valid fields        | Functional, Black Box   | Selenium           | Select future date, valid type, quantity, etc.   | Pickup scheduled successfully                    |
| FR012-02  | Pickup date in the past                      | Functional              | Selenium/Manual    | Select a past date                              | Error: "Pickup date must be in the future"       |
| FR012-03  | Pickup date is today                         | Functional              | Selenium           | Select today’s date                             | Error: "Must be at least 24 hours in advance"    |
| FR012-04  | Missing required fields                      | Functional              | Selenium           | Leave fields blank                               | Validation error messages shown                  |
| FR012-05  | Special instructions > 200 characters         | Functional              | Manual               | Input long string                                | Error: "Max length exceeded"                     |
| FR012-06  | Address auto-filled from profile             | Functional              | Manual    | Open scheduling form                             | Address field auto-filled                        |
| FR014-01  | Display available time slots                 | Functional              | Selenium           | Open scheduling form                             | Shows selectable time slots                      |
| FR015-01  | Try scheduling two pickups on same date      | Functional              | Selenium           | Submit two requests for same day                 | Error: "Pickup already scheduled for this date"  |

## Request Management

| Test ID    | Description                                 | Type        | Tool     | Steps                                  | Expected Result                           |
|------------|---------------------------------------------|-------------|----------|-----------------------------------------|--------------------------------------------|
| FR016-01   | View pickup history                         | Functional  | Selenium | Login, then go to history               | Shows list of previous requests            |
| FR017-01   | Cancel a pending request                    | Functional  | Selenium | Click "Cancel" on pending request       | Status changes to "Cancelled"              |
| FR017-02   | Cancel a completed request                  | Functional  | Selenium | Try canceling a completed request       | Error: "Request can’t be cancelled"        |
| FR018-01   | Edit pickup before 24 hours                 | Functional  | Selenium | Modify date/time > 24 hrs in advance    | Update successful                          |
| FR018-02   | Edit pickup within 24 hours                 | Functional  | Selenium | Try editing close to pickup time        | Error: "Modifications not allowed"         |
| FR019-01   | Display status for each request             | Functional  | Jest     | View request cards                       | Shows statuses like "Pending", "Confirmed" |

## Request Tracking

| Test Case  | Description                                | Type        | Tool              | Steps                                             | Expected Result                                  |
|------------|--------------------------------------------|-------------|-------------------|---------------------------------------------------|---------------------------------------------------|
| FR020-01   | Real-time status updates                   | Functional  | Pytest/Selenium   | Track active request                              | Status updates without page refresh              |
| FR021-01   | Notifications on status change             | Functional  | Manual, Jest      | Mark request as “Confirmed”                       | Notification appears/sent                        |
| FR022-01   | Submit feedback after completion           | Functional  | Selenium          | Click "Leave Feedback" after status = Completed   | Feedback form appears and submits                |

## Non-functional Test Cases

| Test ID  | Description                        | Type           | Tool                  | Steps                             | Expected Result                       |
|----------|------------------------------------|----------------|-----------------------|------------------------------------|----------------------------------------|
| NF-001   | Time to submit pickup form         | Non-Functional | DevTools              | Fill & submit, measure time        | Response < 2 seconds                  |
| NF-003   | Form layout on mobile              | Non-Functional | DevTools (Mobile)     | Open scheduling form               | Responsive and usable UI              |
| NF-004   | Accessibility check                | Non-Functional | Lighthouse            | Run audit on pickup page           | Score > 90                            |

# Test Cases for the Admin Dashboard

##  Request Management Test Cases

| Test Case | Description | Type | Tool | Steps | Expected Result |
|-----------|-------------|------|------|-------|------------------|
| FR053-01 | View all pickup requests | Functional, Black Box | Selenium | 1. Login as admin
2. Navigate to requests | All requests displayed |
| FR054-01 | Approve a pending request | Functional | Selenium | Click “Approve” on a request | Status changes to “Approved” |
| FR054-02 | Reject a pending request | Functional | Selenium | 1. Click “Reject”
2. Confirm | Status changes to “Rejected” |
| FR054-03 | Modify a request (e.g., time) | Functional | Selenium | 1. Edit details
2. Save | Request is updated successfully |
| FR055-01 | Assign pickup date and time | Functional | Selenium | 1. Choose date/time
2. Assign | Assignment saved and shown in list |
| FR056-01 | Filter requests by status | Functional | Selenium | Use dropdown filter by status (Pending, completed, scheduled, missed) and location | Only pending requests shown if pending was chosen for either all cities or one chosen city |
| FR056-02 | Search requests by user/email | Functional | Selenium | Enter user email in search box | Matching requests displayed |

##  User Management Test Cases

| Test Case | Description | Type | Tool | Steps | Expected Result |
|-----------|-------------|------|------|-------|------------------|
| TC-FR057-01 | View all users | Functional | Selenium | Navigate to user list | All users listed |
| FR058-01 | Change user role (User → Admin) | Functional | Selenium, Pytest | 1. Select user
2. Change role
3. Confirm | Role updated to Admin |
| FR059-02 | Delete a user account | Functional | Selenium | 1. Locate a Delete option
2. Confirm | User is removed from the system |

# Personalized Dashboard Test Cases

## Test Cases for User Dashboard

| Test Case ID | Description                         | Type       | Tool     | Steps                                   | Expected Result                                  |
|--------------|-------------------------------------|------------|----------|-----------------------------------------|--------------------------------------------------|
| FR023-01     | Display personalized dashboard      | Functional | Selenium | 1. Login as a user                      | Personalized dashboard is displayed              |
| FR023-02     | View recent pickup requests         | Functional | Selenium | 1. Login 2. Go to dashboard             | Recent pickup requests shown                     |
| FR023-03     | View upcoming scheduled pickups     | Functional | Selenium | 1. Login 2. Go to dashboard             | Scheduled pickups are listed                     |
| FR023-04     | View environmental impact stats     | Functional | Selenium | 1. Login 2. Go to dashboard             | Environmental stats displayed (waste, CO2, trees saved) |
| FR023-05     | View achievement badges             | Functional | Selenium | 1. Login 2. Go to dashboard             | Achievement badges visible                       |
| FR023-06     | Use quick action buttons            | Functional | Selenium | 1. Login 2. Click quick action buttons  | Redirects/Actions occur correctly                |
| FR024-01     | Calculate & display total waste diverted | Functional | Selenium | 1. Login 2. View impact stats           | Total waste diverted is shown accurately         |
| FR024-02     | Calculate & display CO2 saved       | Functional | Selenium | 1. Login 2. View impact stats           | CO2 savings displayed                            |
| FR024-03     | Calculate & display trees equivalent | Functional | Selenium | 1. Login 2. View impact stats           | Trees equivalent is shown                        |

## Test Cases for  Analytics & Reports

| Test Case ID | Description                         | Type       | Tool     | Steps                                   | Expected Result                                  |
|--------------|-------------------------------------|------------|----------|-----------------------------------------|--------------------------------------------------|
| FR025-01     | View waste management charts/graphs | Functional | Selenium | 1. Login 2. Navigate to Analytics       | Visual data charts displayed                     |
| FR026-01     | Display community leaderboard       | Functional | Selenium | 1. Login 2. Go to Leaderboard           | Leaderboard ranked by impact                     |
| FR027-01     | View monthly waste trends           | Functional | Selenium | 1. Login 2. View trends section         | Monthly trends graph visible                     |
| FR027-02     | View yearly waste trends            | Functional | Selenium | 1. Login 2. View trends section         | Yearly trends graph visible                      |
| FR028-01     | Export user data to CSV             | Functional | Selenium | 1. Login 2. Click Export button         | CSV file downloaded successfully                 |

## Test  Cases for Gamification

| Test Case ID | Description                              | Type       | Tool     | Steps                                  | Expected Result                                |
|--------------|------------------------------------------|------------|----------|----------------------------------------|------------------------------------------------|
| FR029-01     | Award badge: First pickup scheduled      | Functional | Selenium | Schedule first pickup                  | Badge for first pickup awarded                 |
| FR029-02     | Award badge: 10 pickups completed        | Functional | Selenium | Complete 10 pickups                    | "10 pickups" badge awarded                    |
| FR029-03     | Award badge: Perfect recycling score     | Functional | Selenium | Get perfect recycling score            | Badge appears on dashboard                     |
| FR029-04     | Award badge: Community contributor       | Functional | Selenium | Contribute in community events         | Contributor badge awarded                      |
| FR030-01     | Track user points and level              | Functional | Selenium | Perform pickup and recycling actions   | Points increase and level updated              |

# Community Features Testing

## FR-045: View and Edit Profile Information

| ID   | Description                      | Test Steps                                                                 | Expected Result                                            |
|------|----------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------|
| 045-1 | View profile information         | 1. Login 2. Go to Profile                                                | User profile data (name, email, etc.) is shown             |
| 045-2 | Edit profile information         | 1. Go to Profile<br>2. Click "Edit"<br>3. Modify fields<br>4. Save         | Updated info is saved and displayed                        |
| 045-3 | Invalid profile data handling    | 1. Edit profile<br>2. Enter invalid email or empty field<br>3. Save        | Validation error shown; profile not updated                |

## FR-046: Display Activity History and Achievements

| ID   | Description                      | Test Steps                                                                 | Expected Result                                            |
|------|----------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------|
| 046-1 | View activity history            | 1. Login<br>2. Go to Profile      | List of actions (blog posts, comments, requets) shown                  |
| 046-2 | View achievements                | 1. Go to Profile                                      | Earned badges/achievements displayed                       |

## FR-047: Upload Profile Picture

| ID   | Description                      | Test Steps                                                                 | Expected Result                                            |
|------|----------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------|
| 047-1 | Upload a valid image            | 1. Go to Profile<br>2. Click on Edit profilw <br>3. Paste image url<br>4. Click save profile  | Profile picture is updated and displayed                   |
| 047-2 | Upload invalid file type        | 1. Try uploading .txt or .exe file as profile picture                      | Error shown: "Invalid file type"                           |
| 047-3 | Remove profile picture          | 1. 1. Go to Profile<br>2. Click on Edit profilw <br>3. Delete image url<br>4. Click save profile                 | Default avatar is shown                                    |

## FR-048: Show Statistics and Environmental Impact

| ID   | Description                      | Test Steps                                                                 | Expected Result                                            |
|------|----------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------|
| 048-1 | View statistics                 | 1. Go to Profile > Statistics                                              | Data like cleanups done, CO2 saved, reports filed shown    |
| 048-2 | Statistics update after action | 1. Perform cleanup or report<br>2. Refresh stats                          | Stats reflect the new action                               |

## FR-050: News Feed of Community Activities

| ID   | Description                      | Test Steps                                                                 | Expected Result                                            |
|------|----------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------|
| 050-1 | View community feed             | 1. Login<br> 2. Go to  Community                                                        | Activities of users shown                         |
| 050-2 | Feed updates dynamically        | 1. Like or comment feed of a user<br>2. Refresh feed        | New activity appears in feed                               |

# Test cases for Blogs
| **Test Case** | **Feature**          | **Description**                                     | **Expected Result**                          | **Results** |
| ------------- | -------------------- | --------------------------------------------------- | -------------------------------------------- | ----------- |
| TC-001        | Blog System          | Blog section related to waste management is present | Users see blog posts about waste/environment | Pass        |
| TC-002        | Blog System          | Users can view blog posts                           | Blog content is readable                     | Pass        |
| TC-003        | Blog Interaction     | Users can interact with posts (like and comment)    | Interaction buttons work                     | Pass        |
| TC-004        | Blog Management      | Users/admins can create, edit, delete blog posts    | Blog post management UI functional           | Fail        |
| TC-005        | Blog Categories/Tags | Blog supports tags or categories                    | Posts show under proper tags/categories      | Fail        |

