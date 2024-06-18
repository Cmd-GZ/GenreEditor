import tkinter
import tkinter.ttk
import tkinter.messagebox
import tkinter.filedialog
import os
import ctypes
import genre_editor
#####
def Text_Get(vaule_name, text_list):
        start_number = text_list.find(vaule_name)
        end_number = text_list.find('\n', start_number)
        return text_list[start_number + len(vaule_name) + 3 : end_number]
#
def Path_Select():
        path_select_temp = tkinter.filedialog.askdirectory()
        if path_select_temp:
                path_input.delete(0, "end")
                path_input.insert(0, path_select_temp)
#
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
                        if hex(dll_h.GetSystemDefaultUILanguage()) != '0x804' : tkinter.messagebox.showerror(title='Error', message='No matching songs.')
                        if hex(dll_h.GetSystemDefaultUILanguage()) == '0x804' : tkinter.messagebox.showerror(title='错误', message='不存在目标歌曲')
        else:
                if hex(dll_h.GetSystemDefaultUILanguage()) != '0x804' : tkinter.messagebox.showerror(title='Error', message='Illegal path. Please check your input.')
                if hex(dll_h.GetSystemDefaultUILanguage()) == '0x804' : tkinter.messagebox.showerror(title='错误', message='非法路径，请检查输入')
        if mode.get() == 'add':
                true_step += 1
                if true_step == 3 : genre_editor.Genre_Addor(path, song_edit_list, genre_input.get())

        elif mode.get() == 'remove':
                true_step += 1
                if true_step == 3 : genre_editor.Genre_Remover(path, song_edit_list, genre_input.get())
        else :
                if hex(dll_h.GetSystemDefaultUILanguage()) != '0x804' : tkinter.messagebox.showerror(title='Error', message='Illegal mode. Please choose a mode.')
                if hex(dll_h.GetSystemDefaultUILanguage()) == '0x804' : tkinter.messagebox.showerror(title='错误', message='请选择一个模式')
        if true_step == 3:
                if hex(dll_h.GetSystemDefaultUILanguage()) != '0x804' : tkinter.messagebox.showinfo(title='Done', message='Please check the result.')
                if hex(dll_h.GetSystemDefaultUILanguage()) == '0x804' : tkinter.messagebox.showinfo(title='完成', message='请检查结果')
#####
mian = tkinter.Tk()
mian.title("Genre Editor")
mian.geometry('800x400')
mian.resizable(False, False)
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
mian.iconbitmap('favicon.ico') 
mian.tk.call('tk', 'scaling', ScaleFactor/75)
#
text_path_input_title = tkinter.StringVar()
text_path_select_botton = tkinter.StringVar()
text_mode_choose_title = tkinter.StringVar()
text_mode_add = tkinter.StringVar()
text_mode_remove = tkinter.StringVar()
text_key_word_input_title = tkinter.StringVar()
text_key_word_input_tip = tkinter.StringVar()
text_genre_input_title = tkinter.StringVar()
text_start_botton = tkinter.StringVar()
dll_h = ctypes.windll.kernel32
if hex(dll_h.GetSystemDefaultUILanguage()) == '0x804' :
        lang = open('lang/en-Us.lang', 'r', encoding='utf-8')
if hex(dll_h.GetSystemDefaultUILanguage()) == '0x804' :
        lang = open('lang/zh-CN.lang', 'r', encoding='utf-8')
text_list = lang.read()
text_path_input_title = Text_Get('text_path_input_title', text_list)
text_path_select_botton = Text_Get('text_path_select_botton', text_list)
text_mode_choose_title = Text_Get('text_mode_choose_title', text_list)
text_mode_add = Text_Get('text_mode_add', text_list)
text_mode_remove = Text_Get('text_mode_remove', text_list)
text_key_word_input_title = Text_Get('text_key_word_input_title', text_list)
text_key_word_input_tip = Text_Get('text_key_word_input_tip', text_list)
text_genre_input_title = Text_Get('text_genre_input_title', text_list)
text_start_botton = Text_Get('text_start_botton', text_list)
#####
path_input_title = tkinter.ttk.Label(mian, text = text_path_input_title)
path_input = tkinter.ttk.Entry(mian, show=None, width=70)
path_select_botton = tkinter.ttk.Button(mian, text = text_path_select_botton, command = Path_Select)
#
mode = tkinter.StringVar()
mode.set('fuck')
mode_choose_title = tkinter.ttk.Label(mian, text = text_mode_choose_title)
mode_add = tkinter.ttk.Radiobutton(mian, text = text_mode_add, variable=mode, value='add')
mode_remove = tkinter.ttk.Radiobutton(mian, text = text_mode_remove, variable=mode, value='remove')
#
key_word_input_title = tkinter.ttk.Label(mian, text = text_key_word_input_title)
key_word_input = tkinter.ttk.Entry(mian, show=None)
key_word_input_tip = tkinter.ttk.Label(mian, text = text_key_word_input_tip)
#
genre_input_title = tkinter.ttk.Label(mian, text = text_genre_input_title)
genre_input = tkinter.ttk.Entry(mian, show=None)
#
start_botton = tkinter.ttk.Button(mian, text = text_start_botton, command = Start)
#####













#####
path_input_title.place(x=0, y=0, anchor='nw')
path_input.place(x=0, y=30, anchor='nw')
path_select_botton.place(x=710, y=82, anchor='center')
mode_choose_title.place(x=0, y=100, anchor='nw')
mode_add.place(x=0, y=130, anchor='nw')
mode_remove.place(x=0, y=160, anchor='nw')
key_word_input_title.place(x=0, y=200, anchor='nw')
key_word_input.place(x=0, y=230, anchor='nw')
key_word_input_tip.place(x=230, y=230, anchor='nw')
genre_input_title.place(x=0, y=270, anchor='nw')
genre_input.place(x=0, y=300, anchor='nw')
start_botton.place(x=0, y=345, anchor='nw')
mian.mainloop()
#####