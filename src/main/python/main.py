from fbs_runtime.application_context.PyQt5 import ApplicationContext
import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox
import json, datetime, os, webbrowser,random
from functools import partial
from sys import argv, executable
import os

from settings import settings_window as sw



with open('settings.json') as f:
    file_content = f.read()
    settings = json.loads(file_content)

chars = settings['chars']
pass_length = settings['pass_length']
data_dir = settings['data_dir']
passlist_dir = settings['passlist_dir']
lang_file = data_dir + '/lang/' + settings['lang'] + '.json'

app_name = 'CDL PassGen'
app_version = '0.15'
release = settings['release']
author = 'CoderLOG Projects (c), 2019'
app_license = 'GNU 3.0' 


def restart_program():
    os.execl(executable, os.path.abspath(__file__), *argv)

root = Tk()
root.iconbitmap(data_dir+'/images/p_gen.ico')
root.resizable(width=False, height=False)
root.title(app_name+' v ' + app_version)
root.geometry("420x362+300+300")
calculated_text = Text(root, height=14, width=50)
FILE_NAME = tkinter.NONE
lang_sw_ru = ''
lang_sw_eng = ''
if settings['lang'] == 'ru':
	lang_sw_ru = '*  '

if settings['lang'] == 'eng':
	lang_sw_eng = '*  '


def lang_load():
	with open(lang_file, encoding='utf-8') as f:
		file_content = f.read()
		global lang
		lang = json.loads(file_content)
	
lang_load()

def erase():
    calculated_text.delete('1.0', END)


def password():
    for n in range(int(number_entry.get())):
        password = ''
        for i in range(int(length_entry.get())):
            password += random.choice(chars)
        calculated_text.insert(END, password + "\n")


def save_passlist():
	out = asksaveasfile(mode='w', defaultextension='md')
	data = calculated_text.get('1.0', tkinter.END)
	try:
		out.write(data.rstrip())
	except Exception:
		showerror(title=lang['error_window'], message=lang['error_messages'])


def github():
    return webbrowser.open('https://github.com/alexborsch/CDL-PassGen')

def info():
	messagebox.showinfo("Information", app_name+" v "+app_version+" \nby "+author+"\nhttps://coderlog.top")


def app_settings():
    pass

def switch_lang(lang):
	
	if lang == 1:
		with open('settings.json', 'r+') as f:
			json_data = json.load(f)
			json_data['lang'] = 'eng'
			f.seek(0)
			f.write(json.dumps(json_data))
			f.truncate()
			
	elif lang == 2:
		with open('settings.json', 'r+') as f:
			json_data = json.load(f)
			json_data['lang'] = 'ru'
			f.seek(0)
			f.write(json.dumps(json_data))
			f.truncate()
	else:
		pass
	
	messagebox.showinfo("Information", "restart app")
	


'''
Окно настроек
'''


display_button = Button(text=lang['button_generate'], command=password)
erase_button = Button(text=lang['button_clear'], command=erase)
info_button = Button(text=lang['button_information'], command=sw)
text_label = Label(text=author + " |   "+ app_name+" v " + app_version + " Release: " + release + "      | " + app_license, fg="#003363", bg="#99adc0")
#number_entry = int(1)

number_entry = Entry(width=10, justify=CENTER)
length_entry = Entry(width=10, justify=CENTER)
length_entry.insert(0, pass_length)
number_entry.insert(0, "8")

length_label = Label(text="      "+lang['length_label'])
number_label = Label(text="      "+lang['passwords'])
length_label.grid(row=1, column=0, sticky="w")
length_entry.grid(row=1, column=1, padx=1, pady=5)

number_label.grid(row=0, column=0, sticky="w")
number_entry.grid(row=0,column=1, padx=1, pady=5)

display_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")
erase_button.grid(row=2, column=2, padx=7, pady=5, sticky="w")
info_button.grid(row=2, column=0, padx=12, pady=5, sticky="w")
text_label.place(x=0,y=320)
calculated_text.grid(row=4, column=0, sticky='nsew', columnspan=3)

scrollb = Scrollbar(root, command=calculated_text.yview)
scrollb.grid(row=4, column=4, sticky='nsew')
calculated_text.configure(yscrollcommand=scrollb.set)


menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
infoMenu = tkinter.Menu(menuBar)
settingsMenu = tkinter.Menu(menuBar)
settings_submenu = tkinter.Menu(menuBar)

fileMenu.add_command(label=lang['menu_savepasslist'], command=save_passlist)
infoMenu.add_command(label=lang['github'], command=github)
infoMenu.add_command(label=lang['menu_info'], command=info)
settings_submenu.add_command(label=lang_sw_eng+'eng', command=partial(switch_lang, 1))
settings_submenu.add_command(label=lang_sw_ru+'ru', command=partial(switch_lang, 2))

settingsMenu.add_cascade(label=lang['menu_language'], menu=settings_submenu)
menuBar.add_cascade(label=lang['menu_file'], menu=fileMenu)
menuBar.add_cascade(label=lang['menu_settings'], menu=settingsMenu)
menuBar.add_cascade(label=lang['menu_info'], menu=infoMenu)
menuBar.add_cascade(label=lang['menu_exit'], command=root.quit)

root.config(menu=menuBar)


root.mainloop()