from tkinter import *
from tkinter import filedialog, messagebox
import webbrowser, time

btns, btns_place, save=[], [], 0
GEO='1004x652'

#time.sleep(2)

def upd_name():
    global win, txt, filename
    if win.title()=='Untitled.txt' and txt.get('0.0', END)!='\n':
        win.title('*Untitled.txt')
    elif win.title()=='*Untitled.txt' and txt.get('0.0', END)=='\n':
        win.title('Untitled.txt')
    elif win.title()!='Untitled.txt' and win.title()!='*Untitled.txt':
        if win.title()[0]=='*':
            with open(filename, 'r', encoding='utf8') as textfile:
                text=textfile.read()
                if txt.get('0.0', END)==text or txt.get('0.0', END)==text+'\n':
                    win.title(filename.split('/')[-1])
        else:
            with open(filename, 'r', encoding='utf8') as textfile:
                text=textfile.read()
                if txt.get('0.0', END)!=text and txt.get('0.0', END)!=text+'\n':
                    win.title('*'+filename.split('/')[-1])

    win.after(1, upd_name)

def new():
    global win, txt, save
    if win.title()[0]=='*':
        title=win.title()[1:]
        if messagebox.askyesno('Create file', f"Do you want to save changes in file {title}?\n(Don't forget to add .txt in the end of the file name)"):
            save_as()
    txt.delete('0.0', END)
    win.title('Untitled.txt')
    save=0

def open1():
    global win, txt, filename
    filename=filedialog.askopenfilename(filetypes=(("Текстовые файлы","*.txt"),("Все файлы","*.*")))
    try:
        with open(filename, 'r', encoding='utf8') as textfile:
            text=textfile.read()
            txt.delete('0.0', END)
            txt.insert('0.0', text)
        win.title(filename.split('/')[-1])
    except:
        messagebox.showerror('Error', 'Failed to open file')
        txt.delete('0.0', END)

def save1():
    global win, save
    if win.title()[0]=='*' or win.title()=='Untitled.txt':
        if 'Untitled.txt' in win.title() and save==0:
            save_as()
        else:
            with open(filename, 'w', encoding='utf8') as textfile:
                textfile.write(txt.get('0.0', END))

def save_as():
    global filename, save, win
    filename=filedialog.asksaveasfilename(filetypes=(("Текстовые файлы","*.txt"),("Все файлы","*.*")))
    try:
        with open(filename, 'w', encoding='utf8') as textfile:
            textfile.write(txt.get('0.0', END))
        win.title(filename.split('/')[-1])
        save=1
    except:
        messagebox.showerror('Error', 'Failed to save file')

def exit1():
    win.destroy()

def bing():
    global txt
    text1=txt.get('0.0', END).split('\n')[:-1]
    search='https://www.bing.com/search?q='
    for i in text1:
        search+='+'
        search+=i
    webbrowser.open_new_tab(search)

def wrap():
    global txt
    if txt['wrap']==None:
        txt['wrap']=WORD
    else:
        txt['wrap']=None
#менять wrap на None или WORD, ставить галочку в конце при WORD

def scale_in():
    global txt
    font=int(txt['font'][-2:])
    font+=1
    txt['font']=f'arial {font}'

def scale_de():
    global txt
    font=int(txt['font'][-2:])
    font-=1
    txt['font']=f'arial {font}'

def scale_re():
    global txt
    txt['font']='arial 12'

def help_link():
    webbrowser.open_new_tab('https://www.bing.com/search?q=справка+по+использованию+блокнота+в+windows%c2%a010&filters=guid:"4466414-ru-dia"%20lang:"ru"&form=T00032&ocid=HelpPane-BingIA')

def fb():
    webbrowser.open_new_tab('https://t.me/KruASe')

def about():
    messagebox.showinfo('About', 'А pathetic parody of Notepad in Windows 10')

def keys():
    messagebox.showinfo('Keyboard shortcuts for editing', 'Copy                   Ctrl+C\nPaste                   Ctrl+V\nCut                      Ctrl+X\nSelect all             Ctrl+A\nDelete                      Del')


def new_(event):
    new()
def open1_(event):
    open1()
def save1_(event):
    save1()
def save_as_(event):
    save_as()
def exit1_(event):
    exit1()
def bing_(event):
    bing()
def scale_in_(event):
    scale_in()
def scale_de_(event):
    scale_de()
def scale_re_(event):
    scale_re()
def help_link_(event):
    help_link()
def about_(event):
    about()
def keys_(event):
    keys()


win=Tk()
win.geometry(GEO)
win.title('Untitled.txt')
#win.resizable(False, False)
menu=Menu(win)
win['menu']=menu
label=Label(win, width=1000, height=1000, bg='#ffffff')
scrollbary=Scrollbar(win)
txt=Text(win, width=123, height=36, font='arial 12', wrap=None, yscrollcommand=scrollbary.set)
txt.focus()
scrollbary=Scrollbar(win)

File=Menu(menu, tearoff=0)
Edit=Menu(menu, tearoff=0)
Format=Menu(menu, tearoff=0)
View=Menu(menu, tearoff=0)
Help=Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=File)
menu.add_cascade(label='Edit', menu=Edit)
menu.add_cascade(label='Format', menu=Format)
menu.add_cascade(label='View', menu=View)
menu.add_cascade(label='Help', menu=Help)
File.add_command(label='Create new file', command=new)
File.add_command(label='Open file', command=open1)
File.add_command(label='Save file', command=save1)
File.add_command(label='Save file as...', command=save_as)
File.add_command(label='Exit', command=exit1)
Edit.add_command(label='Search in Bing', command=bing)
Format.add_command(label='Word wrapping (on/off, firstly off)', command=wrap)
View.add_command(label='Increase scale', command=scale_in)
View.add_command(label='Decrease scale', command=scale_de)
View.add_command(label='Reset scale', command=scale_re)
Help.add_command(label='Shortcuts', command=keys)
Help.add_command(label='View Help', command=help_link)
Help.add_command(label='Send feedback', command=fb)
Help.add_command(label='About', command=about)

win.bind('<Control-n>', new_)
win.bind('<Control-o>', open1_)
win.bind('<Control-s>', save1_)
win.bind('<Control-S>', save_as_)
win.bind('<Control-q>', exit1_)
win.bind('<Control-b>', bing_)
win.bind('<Control-equal>', scale_in_)
win.bind('<Control-minus>', scale_de_)
win.bind('<Control-0>', scale_re_)
win.bind('<Control-h>', help_link_)
win.bind('<Control-i>', about_)
win.bind('<Control-k>', keys_)


txt.place(x=-1, y=-1)
scrollbary.pack(side=RIGHT, fill=Y)
label.place(x=-5, y=-5)

scrollbary.config(command=txt.yview)

win.after(1, upd_name)

mainloop()
