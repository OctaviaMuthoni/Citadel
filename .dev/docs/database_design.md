### LIBRARY MANAGEMENT SYSTEM - DATABASE DESIGN

    This file describe all the tables used in library system:
    
This tables include:-
- Users
- User sessions
- Members
- Materials
- Cards

### User related tables:
Once a user login in the system, their details are looked up from the database tables.
If a user exists, then a session is created and is only killed when the user closes the window.

#### Users:
    user_uuid
    profile_image
    username
    email
    role
    password
    attempts - invisible field

#### User Sessions
    session_uuid
    user_uuid
    start
    end
    status

#### OTPs 
    otp_uuid
    user_uuid
    otp
    created_on
    expired_on
    status


    

    