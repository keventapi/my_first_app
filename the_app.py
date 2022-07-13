
try:
	import tkinter as tk
except:
	import Tkinter as tk
class main():
	def __init__(self):
		self.window = tk.Tk()
		self.frame = tk.Frame(self.window)
		self.list_of_content=[]
		self.clip_content = lambda: main.format_content(self.window.clipboard_get())
			
			
	def make_screen_content(self):
		label = tk.Label(self.window, text="make sure to have copied all content")
		label.pack()
		button = tk.Button(self.window, text="get the content from your clipboard ", command=self.clip_content)
		button.pack()
		self.frame.pack()
		self.window.mainloop()
		
		
	def format_content(self, content):
		while "\n " in content:
			content = content.replace('\n ', '\n')
		new_text = ''
		had_breake_line = False
		for letter in content:
			if letter.lower() in "qwertyuiopasdfghjklzxcvbnm ":
				new_text+=letter
				had_breake_line=False
			if letter == "\n" and had_breake_line == False:
				new_text+=letter
				had_breake_line = True
			if had_breake_line:
				pass
		main.order_content(new_text)
	
			
	def order_content(self, content):
		list_of_qna=[]
		list_of_content=[]
		string=""
		counter=0
		for letter in content:
			string+=letter
			if letter =="\n":
				list_of_qna.append(string)
				string=""
				counter+=1				
				if counter == 2:
					list_of_content.append(list_of_qna)
					counter=0
					list_of_qna=[]
		self.list_of_content=list_of_content
		main.break_line(list_of_content)
			
			
	def break_line(self, content):
		new_text = ""
		counter = 0
		for index_1 in range(len(content)):
					for index_2 in range(len(content[index_1])):
						for letter in content[index_1][index_2]:
							if counter >= 40 and letter == " ":
								new_text+="\n"
								counter=0
								if letter == "\n":
									counter=0
									new_text+=f'\n'
							new_text+=f'{letter}'
							counter+=1
						content[index_1][index_2] = new_text
						new_text=''
						counter=0
		main.make_buttons(content)
			
			
	def make_buttons(self, content):
		list_of_buttons=[]
		row=1
		column=1
		for i in range(len(content)):
					list_of_buttons.append(tk.Button(self.frame, text=f"{i+1}", command= lambda v=i: main.put_on_clipboard(self.list_of_content[v])) )
					list_of_buttons[i].grid(row=row, column=column, sticky="W")
					column+=1
					if column > 5:
						row+=1
						column=1
					
	def put_on_clipboard(self, content):
		self.window.clipboard_clear()
		self.window.clipboard_append(f"{content[0]} {content[1]}")
		
if __name__ == "__main__":
		main = main()
		main.make_screen_content()
		
	
