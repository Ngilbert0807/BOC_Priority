import gspread
from oauth2client.service_account import ServiceAccountCredentials

class AutoPriorityTable:
	def __init__(self, sheet_name):
		scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
		credentials = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/natha/OneDrive/Documents/Python Scripts/BOC_priority/service_account.json.json", scope) 
  		#edit to the file path of your service_account_json, make sure to change all \ to /
		client = gspread.authorize(credentials)
		self.sheet = client.open(sheet_name).worksheet('Automated Priority List')
	def increase_priority(self, email_add_list):
		data = self.sheet.get_all_values()
		headers = data[0] if data else []
		rows = data[1:] if len(data) > 1 else []
		if "bmail" not in headers or "Priority Level" not in headers: 
			raise ValueError("The sheet must have 'bmail' and 'Priority Level' columns.")
		bmail_idx = headers.index("bmail")
		priority_idx = headers.index("Priority Level")
		email_to_row_map = {row[bmail_idx]: i for i, row in enumerate(rows)}
		for email in email_add_list:
			if email in email_to_row_map:
				row_idx = email_to_row_map[email] + 2
				current_priority = int(self.sheet.cell(row_idx, priority_idx + 1).value or 0)
				self.sheet.update_cell(row_idx, priority_idx + 1, current_priority + 1)
			else:
				new_row = [""] * len(headers)
				new_row[bmail_idx] = email
				new_row[priority_idx] = 1
				self.sheet.append_row(new_row)
	def decrease_priority(self, email_sub_list):
		data = self.sheet.get_all_values()
		headers = data[0] if data else []
		rows = data[1:] if len(data) > 1 else []
		if "bmail" not in headers or "Priority Level" not in headers: 
			raise ValueError("The sheet must have 'bmail' and 'Priority Level' columns.")
		bmail_idx = headers.index("bmail")
		priority_idx = headers.index("Priority Level")
		email_to_row_map = {row[bmail_idx]: i for i, row in enumerate(rows)}
		for email in email_sub_list:
			if email in email_to_row_map:
				row_idx = email_to_row_map[email] + 2
				current_priority = int(self.sheet.cell(row_idx, priority_idx + 1).value or 0)
				self.sheet.update_cell(row_idx, priority_idx + 1, current_priority - 1)
			else:
				raise ValueError("Email not found in the sheet.")
	def sort_sheet(self):
		self.sheet.sort((2, 'des'))
		
		
		
email_add_list=[]
email_add_list=[element.lower() for element in email_add_list]
email_sub_list=[]
email_sub_list=[element.lower() for element in email_sub_list]

if __name__ == "__main__":
    counter = AutoPriorityTable('Automated Priority List')
    counter.increase_priority(email_add_list)
    counter.decrease_priority(email_sub_list)
    counter.sort_sheet()


