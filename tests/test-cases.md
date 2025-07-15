# Test cases for User Authentication

## Functional Testing

| Test Case ID  | Description                                     | Test Type                 | Tool                        | Steps                                 | Expected Result                        |
|---------------|-------------------------------------------------|---------------------------|-----------------------------|----------------------------------------|-----------------------------------------|
| FR001-01      | Register with valid data                        | Equivalence partitioning  | Selenium (Automated), Manual| Fill all required fields correctly     | Account created with "User" role       |
| FR001-02      | Register with invalid email                     | Equivalence partitioning  | Selenium, Manual            | Enter invalid email                    | Error: "Invalid email format"          |
| FR001-04      | Input unidentical passwords during registration | Equivalence partitioning  | Selenium                    | Mismatch password & confirm            | Error: "Passwords do not match"        |
| FR002-01      | Leave full name empty                           | Equivalence partitioning  | Selenium                    | Leave full name blank                  | Error: "Full name is required"         |
| FR002-02      | Enter long name > 50 chars                      | Boundary value Analysis    | Selenium                    | Input long name                        | Error: "Full name too long"            |
| FR001-03      | Password < 8 chars                              | Boundary value Analysis    | Selenium, Manual            | Enter "1234567"                         | Error: "Password too short"            |
| FR010-01      | Admin role can access admin page                | Boundary value Analysis    | Selenium, Pytest            | Login as admin → access `/admin`       | Access granted                         |
| FR011-01      | Normal user restricted from admin               | Boundary value Analysis    | Selenium                    | Login as User → access `/admin`        | Error/Access denied page               |
| FR007-01      | Redirect after login                            | State transition testing   | Selenium                    | Visit restricted page, login           | Redirect to intended page              |
| FR008-01      | Logout clears session                           | State transition testing   | Jest, DevTools              | Click logout → Check localStorage      | Session/token removed                  |
| FR009-01      | Redirect to login after logout                  | State transition testing   | Selenium                    | Logout from user page                  | Redirected to login page               |

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
| FR012-05  | Special instructions > 200 characters         | Functional              | Jest               | Input long string                                | Error: "Max length exceeded"                     |
| FR012-06  | Address auto-filled from profile             | Functional              | Pytest/Selenium    | Open scheduling form                             | Address field auto-filled                        |
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
| FR053-01 | View all pickup requests | Functional, Black Box | Selenium | 1. Login as admin<br>2. Navigate to requests | All requests displayed |
| FR054-01 | Approve a pending request | Functional | Selenium | Click “Approve” on a request | Status changes to “Approved” |
| FR054-02 | Reject a pending request | Functional | Selenium | 1. Click “Reject”<br>2. Confirm | Status changes to “Rejected” |
| FR054-03 | Modify a request (e.g., time) | Functional | Selenium | 1. Edit details<br>2. Save | Request is updated successfully |
| FR055-01 | Assign pickup date and time | Functional | Selenium | 1. Choose date/time<br>2. Assign | Assignment saved and shown in list |
| FR056-01 | Filter requests by status | Functional | Selenium | Use dropdown filter by status (Pending, completed, scheduled, missed) and location | Only pending requests shown if pending was chosen for either all cities or one chosen city |
| FR056-02 | Search requests by user/email | Functional | Selenium | Enter user email in search box | Matching requests displayed |

##  User Management Test Cases

| Test Case | Description | Type | Tool | Steps | Expected Result |
|-----------|-------------|------|------|-------|------------------|
| TC-FR057-01 | View all users | Functional | Selenium | Navigate to user list | All users listed |
| FR058-01 | Change user role (User → Admin) | Functional | Selenium, Pytest | 1. Select user<br>2. Change role<br>3. Confirm | Role updated to Admin |
| FR059-02 | Delete a user account | Functional | Selenium | 1. Locate a Delete option<br>2. Confirm | User is removed from the system |

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


