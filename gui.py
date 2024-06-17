import tkinter
import tkinter.ttk
import tkinter.messagebox
import tkinter.filedialog
import os
import ctypes
import genre_editor
#


def Print_Selection():
        genre_input_title.config(text = 'Input the genre you want to ' + mode.get() + ':')

def Path_Select():
        path_select_temp = tkinter.filedialog.askdirectory()
        if path_select_temp:
                path_input.delete(0, "end")
                path_input.insert(0, path_select_temp)




def Start():
        true_step = 0
        if os.path.isdir(path_input.get().replace('\\','/').replace('"','')) == True:
                true_step += 1
                path = path_input.get().replace('\\','/').replace('"','')
                file_list = os.listdir(path)
                song_list = [item for item in file_list if item.endswith('.mp3') or item.endswith('.flac') or item.endswith('.wav') or item.endswith('.m4a') or item.endswith('.aac')]
                song_edit_list = [item for item in song_list if key_word_input.get() in item]
                if len(song_edit_list):
                        true_step +=1
                else:
                        tkinter.messagebox.showerror(title='Error', message='No matching songs.')
        else:
                tkinter.messagebox.showerror(title='Error', message='Illegal path. Please check your input.')
        if mode.get() == 'add':
                true_step += 1
                if true_step == 3 : genre_editor.Genre_Addor(path, song_edit_list, genre_input.get())

        elif mode.get() == 'remove':
                true_step += 1
                if true_step == 3 : genre_editor.Genre_Remover(path, song_edit_list, genre_input.get())
        else :
                tkinter.messagebox.showerror(title='Error', message='Illegal mode. Please choose a mode.')
        if true_step == 3:
                tkinter.messagebox.showinfo(title='Done', message='Please check the result.')

#
mian = tkinter.Tk()
mian.title("Genre Editor")
mian.geometry('800x400')
mian.resizable(False, False)
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
mian.tk.call('tk', 'scaling', ScaleFactor/75)
#
path_input_title = tkinter.ttk.Label(mian, text='Input the path where your song located:')
path_input = tkinter.ttk.Entry(mian, show=None, width=70)
path_select_botton = tkinter.ttk.Button(mian, text='select', command = Path_Select)
#
mode = tkinter.StringVar()
mode.set('fuck')
mode_choose_title = tkinter.ttk.Label(mian, text='Choose a operation mode:')
mode_add = tkinter.ttk.Radiobutton(mian, text='Add', variable=mode, value='add', command=Print_Selection)
mode_remove = tkinter.ttk.Radiobutton(mian, text='Remove', variable=mode, value='remove', command=Print_Selection)
#
key_word_input_title = tkinter.ttk.Label(mian, text='Input the keyword included in the name of the songs you want to edit:')
key_word_input = tkinter.ttk.Entry(mian, show=None)
key_word_input_tip = tkinter.ttk.Label(mian, text='(If you want to edit all of songs, do not input anything.)')
#
genre_input_title = tkinter.ttk.Label(mian, text = 'Input the genre you want to do something:')
genre_input = tkinter.ttk.Entry(mian, show=None)
#
start_botton = tkinter.ttk.Button(mian, text='start', command = Start)
#













#
path_input_title.place(x=0, y=0, anchor='nw')
path_input.place(x=0, y=30, anchor='nw')
path_select_botton.place(x=710, y=82, anchor='center')
mode_choose_title.place(x=0, y=100, anchor='nw')
mode_add.place(x=0, y=130, anchor='nw')
mode_remove.place(x=0, y=160, anchor='nw')
key_word_input_title.place(x=0, y=200, anchor='nw')
key_word_input.place(x=0, y=230, anchor='nw')
key_word_input_tip.place(x=230, y=230, anchor='nw')
genre_input_title.place(x=0, y=280, anchor='nw')
genre_input.place(x=0, y=310, anchor='nw')
start_botton.place(x=0, y=350, anchor='nw')
mian.mainloop()
#
#
#
#
#