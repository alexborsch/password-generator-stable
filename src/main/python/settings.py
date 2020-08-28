from tkinter import Tk

def settings_window():
	root = Tk()
	root.iconbitmap(data_dir+'/images/p_gen.ico')
	root.resizable(width=False, height=False)
	root.title(app_name+' v ' + app_version)
	root.geometry("420x362+300+300")




	
	root.mainloop()	