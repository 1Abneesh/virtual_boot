import tkinter as tk
class Virtualboot:
    def __init__(self):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(master=self.window,width = 800, height = 600, bg = '#3B56A3')

        #robo face
        self.face = self.canvas.create_oval(260, 192, 630, 595, fill='#EDE2FE')
        self.in_face = self.canvas.create_oval(308, 330, 580, 570, fill='black', outline='#B6B1CB', width=10)

        #robo antenna
        self.ant_o = self.canvas.create_line(440, 193, 310, 70, fill='black', width=7)
        self.ant_t = self.canvas.create_line(440, 193, 440, 51, fill='black', width=7)
        self.ant_th = self.canvas.create_line(440, 193, 545, 60, fill='black', width=7)

        #robo ears
        self.l_ear = self.canvas.create_oval(244, 327, 302, 481, fill='black', activefill = '#22B14C')
        self.r_ear = self.canvas.create_oval(585, 327, 650, 481, fill='black',activefill = '#22B14C')

        #robo eyes
        self.l_eye = self.canvas.create_oval(353, 435, 391, 464, fill='#47A7FE')
        self.l_eye_pupil = self.canvas.create_oval(367, 445, 380, 460, fill='#400180')
        self.r_eye = self.canvas.create_oval(496, 435, 535, 464, fill='#47A7FE')
        self.r_eye_pupil = self.canvas.create_oval(510, 445, 523, 460, fill='#400180')

        #robo eyebrows
        self.canvas.create_line(353, 430, 372, 418, 391, 424, fill='#47A7FD', width=5, smooth=1)
        self.canvas.create_line(500, 424, 520, 412, 540, 430, fill='#47A7FD', width=5, smooth=1)
        #robo smile
        self.smile = self.canvas.create_line(410, 512, 455, 555, 500, 512, fill='#47A7FD', smooth=1, width=10)
        self.happy = self.canvas.create_arc(400, 492, 500 ,550,start=180, extent=180,fill='#47A7FD',state = 'hidden')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.window.bind('<Motion>', self.mouse_move)
        self.window.bind('<Leave>', self.mouse_out)
        self.window.bind('<Enter>', self.mouse_over)

        self.keep_blinking = True
        self.keep_ant_blinking = False
        self.coords_l_eye_pupil = self.canvas.coords(self.l_eye_pupil)
        self.coords_r_eye_pupil = self.canvas.coords(self.r_eye_pupil)

        self.window.after(1000, self.blink)
        self.window.after(250,self.ant_blink)
        self.window.mainloop()

    def mouse_move(self, event):
        if event.x >= self.coords_l_eye_pupil[0] and event.x <= self.coords_r_eye_pupil[2] and event.y >= self.coords_l_eye_pupil[1] and event.y <= self.coords_r_eye_pupil[3]:
            # center
            self.canvas.coords(self.l_eye_pupil, self.coords_l_eye_pupil)
            self.canvas.coords(self.r_eye_pupil, self.coords_r_eye_pupil)

        elif event.x >= self.coords_l_eye_pupil[0] and event.x <= self.coords_r_eye_pupil[2]:
            if event.y < self.coords_l_eye_pupil[1]:
                # up
                self.canvas.coords(self.l_eye_pupil, self.coords_l_eye_pupil[0], self.coords_l_eye_pupil[1] - 8, self.coords_l_eye_pupil[2], self.coords_l_eye_pupil[3] - 8)
                self.canvas.coords(self.r_eye_pupil, self.coords_r_eye_pupil[0], self.coords_r_eye_pupil[1] - 8, self.coords_r_eye_pupil[2], self.coords_r_eye_pupil[3] - 8)
            elif event.y > self.coords_l_eye_pupil[3]:
                # down
                self.canvas.coords(self.l_eye_pupil, self.coords_l_eye_pupil[0], self.coords_l_eye_pupil[1] + 6, self.coords_l_eye_pupil[2], self.coords_l_eye_pupil[3] + 6)
                self.canvas.coords(self.r_eye_pupil, self.coords_r_eye_pupil[0], self.coords_r_eye_pupil[1] + 6, self.coords_r_eye_pupil[2], self.coords_r_eye_pupil[3] + 6)
        elif event.y >= self.coords_l_eye_pupil[1] and event.y <= self.coords_r_eye_pupil[3]:
            if event.x < self.coords_l_eye_pupil[0]:
                # left
                self.canvas.coords(self.l_eye_pupil, self.coords_l_eye_pupil[0] - 10, self.coords_l_eye_pupil[1], self.coords_l_eye_pupil[2] - 10, self.coords_l_eye_pupil[3])
                self.canvas.coords(self.r_eye_pupil, self.coords_r_eye_pupil[0] - 10, self.coords_r_eye_pupil[1], self.coords_r_eye_pupil[2] - 10, self.coords_r_eye_pupil[3])
            elif event.x > self.coords_l_eye_pupil[3]:
                # right
                self.canvas.coords(self.l_eye_pupil, self.coords_l_eye_pupil[0] + 10, self.coords_l_eye_pupil[1], self.coords_l_eye_pupil[2] + 10, self.coords_l_eye_pupil[3])
                self.canvas.coords(self.r_eye_pupil, self.coords_r_eye_pupil[0] + 10, self.coords_r_eye_pupil[1], self.coords_r_eye_pupil[2] + 10, self.coords_r_eye_pupil[3])

        elif event.x < self.coords_l_eye_pupil[0]:
            if event.y < self.coords_l_eye_pupil[1]:
                # up left
                self.canvas.coords(self.l_eye_pupil, self.coords_l_eye_pupil[0] - 10,self.coords_l_eye_pupil[1] - 8, self.coords_l_eye_pupil[2] - 10,self.coords_l_eye_pupil[3] - 8)
                self.canvas.coords(self.r_eye_pupil, self.coords_r_eye_pupil[0] - 10, self.coords_r_eye_pupil[1] - 8, self.coords_r_eye_pupil[2] - 10, self.coords_r_eye_pupil[3] - 8)
            elif event.y > self.coords_l_eye_pupil[3]:
                # down left
                self.canvas.coords(self.l_eye_pupil, self.coords_l_eye_pupil[0] - 10, self.coords_l_eye_pupil[1] + 6, self.coords_l_eye_pupil[2] - 10, self.coords_l_eye_pupil[3] + 6)
                self.canvas.coords(self.r_eye_pupil, self.coords_r_eye_pupil[0] - 10, self.coords_r_eye_pupil[1] + 6, self.coords_r_eye_pupil[2] - 10, self.coords_r_eye_pupil[3] + 6)
        elif event.x > self.coords_r_eye_pupil[2]:
            if event.y < self.coords_l_eye_pupil[1]:
                # up right
                self.canvas.coords(self.l_eye_pupil, self.coords_l_eye_pupil[0] + 10, self.coords_l_eye_pupil[1] - 8, self.coords_l_eye_pupil[2] + 10, self.coords_l_eye_pupil[3] - 8)
                self.canvas.coords(self.r_eye_pupil, self.coords_r_eye_pupil[0] + 10, self.coords_r_eye_pupil[1] - 8, self.coords_r_eye_pupil[2] + 10, self.coords_r_eye_pupil[3] - 8)
            elif event.y > self.coords_l_eye_pupil[3]:
                # down right
                self.canvas.coords(self.l_eye_pupil, self.coords_l_eye_pupil[0] + 10, self.coords_l_eye_pupil[1] + 6, self.coords_l_eye_pupil[2] + 10, self.coords_l_eye_pupil[3] + 6)
                self.canvas.coords(self.r_eye_pupil, self.coords_r_eye_pupil[0] + 10, self.coords_r_eye_pupil[1] + 6, self.coords_r_eye_pupil[2] + 10, self.coords_r_eye_pupil[3] + 6)

    def mouse_over(self, event):
        self.keep_blinking = False
        self.keep_ant_blinking = True
        # ensure that the eyes are open and ear and eyes are on their orignal colour
        self.canvas.itemconfig(self.l_eye, fill='#47A7FE')
        self.canvas.itemconfig(self.r_eye, fill='#47A7FE')
        self.canvas.itemconfig(self.l_ear, fill='black')
        self.canvas.itemconfig(self.r_ear, fill='black')
        self.canvas.itemconfig(self.l_eye_pupil, state='normal')
        self.canvas.itemconfig(self.r_eye_pupil, state='normal')
            # ensure that pet smiles
        self.canvas.itemconfig(self.smile, state='hidden')
        self.canvas.itemconfig(self.happy, state='normal')

    def mouse_out(self, event):
        self.keep_blinking = True
        self.keep_ant_blinking = False
        # ensure that pet stops smiling
        self.canvas.itemconfig(self.smile, state='normal')
        self.canvas.itemconfig(self.happy, state='hidden')
        # ensure that pupils are centered
        self.canvas.coords(self.l_eye_pupil, self.coords_l_eye_pupil)
        self.canvas.coords(self.r_eye_pupil, self.coords_r_eye_pupil)
        self.canvas.itemconfig(self.ant_o, fill = 'black')
        self.canvas.itemconfig(self.ant_t, fill='black')
        self.canvas.itemconfig(self.ant_th, fill='black')

    def blink(self):
        if self.keep_blinking == True:  # toggle
            # fetch the eye color
            current_color = self.canvas.itemcget(self.l_eye, 'fill')
            current_color_ear = self.canvas.itemcget(self.l_ear, 'fill')
            if current_color == '#47A7FE':
                new_color = '#EDE2FE'
                pupil_state = 'hidden'

            else:
                new_color = '#47A7FE'
                pupil_state = 'normal'

            if current_color_ear == 'black':
                new_color_ear = '#22B14C'
            else:
                new_color_ear = 'black'


            # apply the new color and pupil state
            self.canvas.itemconfig(self.l_eye, fill=new_color)
            self.canvas.itemconfig(self.r_eye, fill=new_color)
            self.canvas.itemconfig(self.l_eye_pupil, state=pupil_state)
            self.canvas.itemconfig(self.r_eye_pupil, state=pupil_state)
            self.canvas.itemconfig(self.l_ear, fill = new_color_ear)
            self.canvas.itemconfig(self.r_ear, fill=new_color_ear)

        self.window.after(1000, self.blink)
    def ant_blink(self):
        if self.keep_ant_blinking == True:
            current_colour_line_o = self.canvas.itemcget(self.ant_o,'fill')
            current_colour_line_t = self.canvas.itemcget(self.ant_o,'fill')
            current_colour_line_th =self.canvas.itemcget(self.ant_o,'fill')

            if current_colour_line_o == 'black':
                new_colour_line_o = 'red'
            else:
                new_colour_line_o = 'black'

            if current_colour_line_t == 'black':
                new_colour_line_t = 'green'
            else:
                new_colour_line_t = 'black'

            if current_colour_line_th == 'black':
                new_colour_line_th = 'yellow'
            else:
                new_colour_line_th = 'black'

            self.canvas.itemconfig(self.ant_o, fill = new_colour_line_o)
            self.canvas.itemconfig(self.ant_t, fill = new_colour_line_t)
            self.canvas.itemconfig(self.ant_th, fill = new_colour_line_th)
        self.window.after(300,self.ant_blink)


Virtualboot()