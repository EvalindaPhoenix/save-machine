#!/usr/bin/env python3
# -*- coding: utf8 -*-

from tkinter import*

main_window = Tk()
quitter = Button(main_window, width = 20, height = 5,\
          text = 'quitter', bg = 'green', fg = 'white',\
          command = main_window.quit)
quitter.pack(padx=60, pady=40)
main_window.mainloop()
