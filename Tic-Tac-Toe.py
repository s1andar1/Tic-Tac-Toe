import tkinter as tk

window = False


class Restart:
    def __init__(self, win):
        self.win = win
        self.btn = tk.Button(self.win, text='Новая игра', bg='#E0E0E0', command=self.restart)
        self.btn.place(x=125, y=300)

    def restart(self):
        WIN.restart_win(self)


class WIN:
    def __init__(self):
        self.start_win()

    def step1(self):
        radio_button = self.var.get()
        if radio_button == 0:
            self.btn_NW.config(text='X')
        else:
            self.btn_NW.config(text='O')
        self.btn_NW.config(state=tk.DISABLED)
        WIN.result(self)

    def step2(self):
        radio_button = self.var.get()
        if radio_button == 0:
            self.btn_N.config(text='X')
        else:
            self.btn_N.config(text='O')
        self.btn_N.config(state=tk.DISABLED)
        WIN.result(self)

    def step3(self):
        radio_button = self.var.get()
        if radio_button == 0:
            self.btn_NE.config(text='X')
        else:
            self.btn_NE.config(text='O')
        self.btn_NE.config(state=tk.DISABLED)
        WIN.result(self)

    def step4(self):
        radio_button = self.var.get()
        if radio_button == 0:
            self.btn_W.config(text='X')
        else:
            self.btn_W.config(text='O')
        self.btn_W.config(state=tk.DISABLED)
        WIN.result(self)

    def step5(self):
        radio_button = self.var.get()
        if radio_button == 0:
            self.btn_C.config(text='X')
        else:
            self.btn_C.config(text='O')
        self.btn_C.config(state=tk.DISABLED)
        WIN.result(self)

    def step6(self):
        radio_button = self.var.get()
        if radio_button == 0:
            self.btn_E.config(text='X')
        else:
            self.btn_E.config(text='O')
        self.btn_E.config(state=tk.DISABLED)
        WIN.result(self)

    def step7(self):
        radio_button = self.var.get()
        if radio_button == 0:
            self.btn_SW.config(text='X')
        else:
            self.btn_SW.config(text='O')
        self.btn_SW.config(state=tk.DISABLED)
        WIN.result(self)

    def step8(self):
        radio_button = self.var.get()
        if radio_button == 0:
            self.btn_S.config(text='X')
        else:
            self.btn_S.config(text='O')
        self.btn_S.config(state=tk.DISABLED)
        WIN.result(self)

    def step9(self):
        radio_button = self.var.get()
        if radio_button == 0:
            self.btn_SE.config(text='X')
        else:
            self.btn_SE.config(text='O')
        self.btn_SE.config(state=tk.DISABLED)
        WIN.result(self)

    def result(self):
        # победа для 'X' 3 в ряд
        if self.btn_NW['text'] == self.btn_N['text'] == self.btn_NE['text'] == 'X':
            self.lbl.config(text='Победил X!')
        if self.btn_W['text'] == self.btn_C['text'] == self.btn_E['text'] == 'X':
            self.lbl.config(text='Победил X!')
        if self.btn_SW['text'] == self.btn_S['text'] == self.btn_SE['text'] == 'X':
            self.lbl.config(text='Победил X!')

        # победа для 'O' 3 в ряд
        if self.btn_NW['text'] == self.btn_N['text'] == self.btn_NE['text'] == 'O':
            self.lbl.config(text='Победил O!')
        if self.btn_W['text'] == self.btn_C['text'] == self.btn_E['text'] == 'O':
            self.lbl.config(text='Победил O!')
        if self.btn_SW['text'] == self.btn_S['text'] == self.btn_SE['text'] == 'O':
            self.lbl.config(text='Победил O!')

        # победа для 'X' 3 в столбик
        if self.btn_NW['text'] == self.btn_W['text'] == self.btn_SW['text'] == 'X':
            self.lbl.config(text='Победил X!')
        if self.btn_N['text'] == self.btn_C['text'] == self.btn_S['text'] == 'X':
            self.lbl.config(text='Победил X!')
        if self.btn_NE['text'] == self.btn_E['text'] == self.btn_SE['text'] == 'X':
            self.lbl.config(text='Победил X!')

        # победа для 'O' 3 в столбик
        if self.btn_NW['text'] == self.btn_W['text'] == self.btn_SW['text'] == 'O':
            self.lbl.config(text='Победил O!')
        if self.btn_N['text'] == self.btn_C['text'] == self.btn_S['text'] == 'O':
            self.lbl.config(text='Победил O!')
        if self.btn_NE['text'] == self.btn_E['text'] == self.btn_SE['text'] == 'O':
            self.lbl.config(text='Победил O!')

        # победа для 'X' 3 в диагональ NE - SW
        if self.btn_SW['text'] == self.btn_C['text'] == self.btn_NE['text'] == 'X':
            self.lbl.config(text='Победил X!')

        # победа для 'O' 3 в диагональ NE - SW
        if self.btn_SW['text'] == self.btn_C['text'] == self.btn_NE['text'] == 'O':
            self.lbl.config(text='Победил O!')

        # победа для 'X' 3 в диагональ NW - SE
        if self.btn_NW['text'] == self.btn_C['text'] == self.btn_SE['text'] == 'X':
            self.lbl.config(text='Победил X!')

        # победа для 'O' 3 в диагональ NW - SE
        if self.btn_NW['text'] == self.btn_C['text'] == self.btn_SE['text'] == 'O':
            self.lbl.config(text='Победил O!')

        # ничья
        if self.btn_NW['text'] == self.btn_N['text'] == self.btn_E['text'] == self.btn_SE['text'] == self.btn_SW[
            'text'] == 'X':
            self.lbl.config(text='Ничья!')
        if self.btn_NW['text'] == self.btn_NE['text'] == self.btn_W['text'] == self.btn_S['text'] == self.btn_SE[
            'text'] == 'X':
            self.lbl.config(text='Ничья!')
        if self.btn_SW['text'] == self.btn_W['text'] == self.btn_N['text'] == self.btn_NE['text'] == self.btn_SE[
            'text'] == 'X':
            self.lbl.config(text='Ничья!')
        if self.btn_NW['text'] == self.btn_NE['text'] == self.btn_E['text'] == self.btn_SW['text'] == self.btn_S[
            'text'] == 'X':
            self.lbl.config(text='Ничья!')
        if self.btn_NW['text'] == self.btn_N['text'] == self.btn_E['text'] == self.btn_SW['text'] == self.btn_S[
            'text'] == 'X':
            self.lbl.config(text='Ничья!')
        if self.btn_NE['text'] == self.btn_N['text'] == self.btn_W['text'] == self.btn_S['text'] == self.btn_SE[
            'text'] == 'X':
            self.lbl.config(text='Ничья!')
        if self.btn_SW['text'] == self.btn_W['text'] == self.btn_N['text'] == self.btn_E['text'] == self.btn_SE[
            'text'] == 'X':
            self.lbl.config(text='Ничья!')
        if self.btn_NW['text'] == self.btn_W['text'] == self.btn_S['text'] == self.btn_E['text'] == self.btn_NE[
            'text'] == 'X':
            self.lbl.config(text='Ничья!')
        if self.btn_N['text'] == self.btn_C['text'] == self.btn_W['text'] == self.btn_NE['text'] == self.btn_SE[
            'text'] == 'X':
            self.lbl.config(text='Ничья!')
        if self.btn_N['text'] == self.btn_C['text'] == self.btn_E['text'] == self.btn_SW['text'] == self.btn_SE[
            'text'] == 'X':
            self.lbl.config(text='Ничья!')
        if self.btn_NW['text'] == self.btn_C['text'] == self.btn_E['text'] == self.btn_S['text'] == self.btn_SW[
            'text'] == 'X':
            self.lbl.config(text='Ничья!')
        if self.btn_NW['text'] == self.btn_NE['text'] == self.btn_W['text'] == self.btn_C['text'] == self.btn_S[
            'text'] == 'X':
            self.lbl.config(text='Ничья!')

        if self.btn_NW['text'] == self.btn_N['text'] == self.btn_E['text'] == self.btn_SE['text'] == self.btn_SW[
            'text'] == 'O':
            self.lbl.config(text='Ничья!')
        if self.btn_NW['text'] == self.btn_NE['text'] == self.btn_W['text'] == self.btn_S['text'] == self.btn_SE[
            'text'] == 'O':
            self.lbl.config(text='Ничья!')
        if self.btn_SW['text'] == self.btn_W['text'] == self.btn_N['text'] == self.btn_NE['text'] == self.btn_SE[
            'text'] == 'O':
            self.lbl.config(text='Ничья!')
        if self.btn_NW['text'] == self.btn_NE['text'] == self.btn_E['text'] == self.btn_SW['text'] == self.btn_S[
            'text'] == 'O':
            self.lbl.config(text='Ничья!')
        if self.btn_NW['text'] == self.btn_N['text'] == self.btn_E['text'] == self.btn_SW['text'] == self.btn_S[
            'text'] == 'O':
            self.lbl.config(text='Ничья!')
        if self.btn_NE['text'] == self.btn_N['text'] == self.btn_W['text'] == self.btn_S['text'] == self.btn_SE[
            'text'] == 'O':
            self.lbl.config(text='Ничья!')
        if self.btn_SW['text'] == self.btn_W['text'] == self.btn_N['text'] == self.btn_E['text'] == self.btn_SE[
            'text'] == 'O':
            self.lbl.config(text='Ничья!')
        if self.btn_NW['text'] == self.btn_W['text'] == self.btn_S['text'] == self.btn_E['text'] == self.btn_NE[
            'text'] == 'O':
            self.lbl.config(text='Ничья!')
        if self.btn_N['text'] == self.btn_C['text'] == self.btn_W['text'] == self.btn_NE['text'] == self.btn_SE[
            'text'] == 'O':
            self.lbl.config(text='Ничья!')
        if self.btn_N['text'] == self.btn_C['text'] == self.btn_E['text'] == self.btn_SW['text'] == self.btn_SE[
            'text'] == 'O':
            self.lbl.config(text='Ничья!')
        if self.btn_NW['text'] == self.btn_C['text'] == self.btn_E['text'] == self.btn_S['text'] == self.btn_SW[
            'text'] == 'O':
            self.lbl.config(text='Ничья!')
        if self.btn_NW['text'] == self.btn_NE['text'] == self.btn_W['text'] == self.btn_C['text'] == self.btn_S[
            'text'] == 'O':
            self.lbl.config(text='Ничья!')

    def start_win(self):
        self.win = tk.Tk()
        Restart(self.win)
        self.win.title('Крестики-нолики')
        self.win.geometry(f'320x350+200+200')
        self.win.resizable(False, False)

        self.var = tk.BooleanVar()
        self.tac = tk.Radiobutton(self.win, text='X', variable=self.var, value=0)
        self.tac.place(x=115, y=20)
        self.toe = tk.Radiobutton(self.win, text='O', variable=self.var, value=1)
        self.toe.place(x=167, y=20)

        self.btn_NW = tk.Button(self.win, width=6, height=3, bg='#E0E0E0', command=self.step1)
        self.btn_NW.place(x=80, y=60)
        self.btn_N = tk.Button(self.win, width=6, height=3, bg='#E0E0E0', command=self.step2)
        self.btn_N.place(x=135, y=60)
        self.btn_NE = tk.Button(self.win, width=6, height=3, bg='#E0E0E0', command=self.step3)
        self.btn_NE.place(x=190, y=60)

        self.btn_W = tk.Button(self.win, width=6, height=3, bg='#E0E0E0', command=self.step4)
        self.btn_W.place(x=80, y=120)
        self.btn_C = tk.Button(self.win, width=6, height=3, bg='#E0E0E0', command=self.step5)
        self.btn_C.place(x=135, y=120)
        self.btn_E = tk.Button(self.win, width=6, height=3, bg='#E0E0E0', command=self.step6)
        self.btn_E.place(x=190, y=120)

        self.btn_SW = tk.Button(self.win, width=6, height=3, bg='#E0E0E0', command=self.step7)
        self.btn_SW.place(x=80, y=180)
        self.btn_S = tk.Button(self.win, width=6, height=3, bg='#E0E0E0', command=self.step8)
        self.btn_S.place(x=135, y=180)
        self.btn_SE = tk.Button(self.win, width=6, height=3, bg='#E0E0E0', command=self.step9)
        self.btn_SE.place(x=190, y=180)

        self.lbl = tk.Label(self.win, width=23)
        self.lbl.place(x=78, y=260)
        self.win.mainloop()

    def restart_win(self):
        self.win.quit()
        self.win.destroy()
        WIN()


if window == False:
    WIN()