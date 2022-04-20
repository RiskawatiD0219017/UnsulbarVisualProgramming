import tkinter

main_window =tkinter.Tk()

def eventombol():
    label2 = tkinter.Label(main_window,text='TEKAN')
    label2.pack()

label = tkinter.Label(main_window, text='Halo guys')

tombol = tkinter.Button(main_window, text='Tekan Tombol', command = eventombol)
label.pack()
tombol.pack()
main_window.mainloop()
