# BOC_Priority

In order to run the script

-You must have Python downloaded directly into your computer (not just an IDE)
- Go to https://www.python.org/downloads/
- Download the latest version of Python for Windows
- During installation, make sure to check the box that says "Add Python to PATH"
- This will make Python accessible from anywhere in your command prompt
- You can access your command prompt by typing cmd into windows search
- In the command prompt enter pip3 install gspread oauth2client
- Make sure that the sheet is shared with the proper google cloud access email
- Create a folder
- Add the py file in the repo to the folder
- Ask a BOC E-Board member for the service_account_json file and also put it in the folder (NOTE: this json file contrains sensitive information do NOT make it public)
- In your command prompt ener cd then the path to that folder
- open up the py file and at the bottom of the notebook there are variables email_add_list and email_sub_list
- Copy and paste the club members bmails you had to reject into the email_add_list. Make sure they are comma seperated and contained in brackets!!
- Do the same thing to email_sub_list to any members that utilized their priority on a trip to subtract 1 from their priority level
- You cannot subtract priority from a member that has never had any and hasn't been added to the sheet, you will receive a value error
- 
