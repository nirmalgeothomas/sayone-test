Required credential to run the project are stored in requirements.txt which is enclosed in github 

github link = https://github.com/nirmalgeothomas/sayone-test/tree/master/event_management_system_project_django

pythonanywhere link = https://nirmalgeothomas.pythonanywhere.com/scm/

Note:  The project hosted on pythonanywhere has many issues on frontend while hosting.But the functionalities still work.For a working frontend project please clone the project on github and run it.Copy and paste admin_home on url to access the administrator pages and paste user_home to access user pages.Credential required to run the project are stored  

Details:
Single event contains the following details:
Title
Description
Location
Start date(Datetime)
End date(Datetime)
Image
Categories(Multiple)
published(Boolean)
paid(Boolean)

A single event contains the above fields.

Features successfully added:

Admin can add events from django default admin
Listed the events with pagination, 10 per page.
Shows all data together in table or can filter by inserting the specific fields in search section
By default sorts the events by date descending order
Filter events by:
Date range( start date is greater than or equal to and end date is lower than or equal to)
Categories (drop down list during add event and edit event pages)
Search event by keyword.
Users can book events in event booking tab and Admin can view them in event booking tab
Added RazorPay Payment Gateway for a fixed amount 500rs , frontend is completed and backend is partially integrated
Added an additional feature to edit and delete events by Admin


Features Missing:
Registered users can Like or dislike an event.
RazorPay payment functionality is not complete



Future Enhancements:
Registered users can comment on events
Users can download an invoice of payment made through the website
Admin can edit event booking details made from users
Show payment history for users
Show registered users for admin

Note: 
Category label does not have a drop down list in the search section,hence it is required to type it.
Pages are not fully responsive and some label fields are not aligned in a fashionable manner.


``






