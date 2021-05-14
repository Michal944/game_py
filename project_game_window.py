
class Window():
    def __init__(self, size_x, size_y):
        self.dft_win = []
        self.y_size = size_y
        self.x_size = size_x
        
    def crt_str_wnd(self):
        self.dft_win.append("_"*self.x_size)
        y_num   = 0
        while y_num < self.y_size:
            if y_num+1 == self.y_size:
               self.dft_win.append("|"+ "_"*(self.x_size-2) +"|")
               break
            self.dft_win.append("|"+" "*(self.x_size-2) +"|")
            y_num+=1
        
    def dsp_window(self):
        for win in self.dft_win:
            print(win)

class Menu_window():
    def __init__(self,x,y):
        self.dft_wnd = Window(x,y)
        self.menu_str = (
            'MMM   MMM  EEEE  NNN   NN  UU   UU',
            'MM M M MM  EE    NN N  NN  UU   UU',
            'MM  M  MM  EEEE  NN  N NN  UU   UU',
            'MM     MM  EE    NN   NNN  UUU UUU',
            'MM     MM  EEEE  NN    NN  UUUUUUU',)
        self.dft_wnd.crt_str_wnd()
        
    def crt_menu(self):
        i=3
        for count in self.menu_str:
            self.dft_wnd.dft_win[i] = '|' + ' '*int((int( self.dft_wnd.x_size - len(self.menu_str[0]))/2) - 1) + count + ' '*int((int( self.dft_wnd.x_size - len(self.menu_str[0]))/2) - 1) + '|'
            i+=1
        return i
        
        
class user_menu():
    def __init__(self, x=60, y=25):
        self.M_window = Menu_window(x,y)
        #M_window.crt_menu()
        self.options = {}
        self.option_pos = self.M_window.crt_menu()
        self.cursor = '---> '
        self.cursor_pos = 0
        self.map_opt = []
    def options_init(self):
        self.options['option 1'] = '1. N E W   G A M E '
        self.options['option 2'] = '2. R e t u r n'
        self.options['option 3'] = '3. O p t i o n s'
        self.options['option 4'] = '4. E x i t '

        self.map_opt.append('option 1')
        self.map_opt.append('')
        self.map_opt.append('option 2')
        self.map_opt.append('')
        self.map_opt.append('option 3')
        self.map_opt.append('')
        self.map_opt.append('option 4')
    def option_on_screen(self):
        saved_opt=self.option_pos

        self.option_pos += 5
        
        for opt_i in self.options.values():             
            self.M_window.dft_wnd.dft_win[self.option_pos]  = '|'
            if opt_i == self.options['option 1']:            
                self.M_window.dft_wnd.dft_win[self.option_pos] += ' '*int((int( self.M_window.dft_wnd.x_size - len(self.options['option 1']))/2) - 1 - len(self.cursor))
                self.M_window.dft_wnd.dft_win[self.option_pos] += self.cursor
            else:
                self.M_window.dft_wnd.dft_win[self.option_pos] += ' '*int((int( self.M_window.dft_wnd.x_size - len(self.options['option 1']))/2) - 1)
            self.M_window.dft_wnd.dft_win[self.option_pos] += opt_i
            self.M_window.dft_wnd.dft_win[self.option_pos] += ' '*(self.M_window.dft_wnd.x_size - len(self.M_window.dft_wnd.dft_win[self.option_pos]) - 1 )    
            self.M_window.dft_wnd.dft_win[self.option_pos] += '|'
            self.option_pos+=2
        self.option_pos=saved_opt

        
    def dsp_user_menu(self):
        self.M_window.dft_wnd.dsp_window()

    def move_up(self):       
        saved_pos = self.option_pos
        if self.cursor_pos >= 2:
            self.option_pos += 5
            for opt_i in self.options.values():
                self.M_window.dft_wnd.dft_win[self.option_pos]  = '|'
                self.M_window.dft_wnd.dft_win[self.option_pos] += ' '*int((int( self.M_window.dft_wnd.x_size - len(self.options['option 1']))/2) - 1)
                self.M_window.dft_wnd.dft_win[self.option_pos] += opt_i
                self.M_window.dft_wnd.dft_win[self.option_pos] += ' '*(self.M_window.dft_wnd.x_size - len(self.M_window.dft_wnd.dft_win[self.option_pos]) - 1 )    
                self.M_window.dft_wnd.dft_win[self.option_pos] += '|'
                self.option_pos+=2

            self.option_pos= saved_pos + 5
            self.cursor_pos-=2  
            self.M_window.dft_wnd.dft_win[self.option_pos+self.cursor_pos]  = '|'
            self.M_window.dft_wnd.dft_win[self.option_pos+self.cursor_pos] += ' '*int((int( self.M_window.dft_wnd.x_size - len(self.options['option 1']))/2) - 1 - len(self.cursor))
            self.M_window.dft_wnd.dft_win[self.option_pos+self.cursor_pos] += self.cursor
            self.M_window.dft_wnd.dft_win[self.option_pos+self.cursor_pos] += self.options.get(self.map_opt[self.cursor_pos])
            self.M_window.dft_wnd.dft_win[self.option_pos+self.cursor_pos] += ' '*(self.M_window.dft_wnd.x_size - len(self.M_window.dft_wnd.dft_win[self.option_pos+self.cursor_pos]) - 1 )    
            self.M_window.dft_wnd.dft_win[self.option_pos+self.cursor_pos] += '|'
            self.option_pos = saved_pos
            
            
        
        
    def move_dw(self):        
        saved_pos = self.option_pos     
        if self.cursor_pos < len(self.map_opt) - 2:    
            self.option_pos += 5
            for opt_i in self.options.values():
                self.M_window.dft_wnd.dft_win[self.option_pos]  = '|'
                self.M_window.dft_wnd.dft_win[self.option_pos] += ' '*int((int( self.M_window.dft_wnd.x_size - len(self.options['option 1']))/2) - 1)
                self.M_window.dft_wnd.dft_win[self.option_pos] += opt_i
                self.M_window.dft_wnd.dft_win[self.option_pos] += ' '*(self.M_window.dft_wnd.x_size - len(self.M_window.dft_wnd.dft_win[self.option_pos]) - 1 )    
                self.M_window.dft_wnd.dft_win[self.option_pos] += '|'
                self.option_pos+=2

            self.option_pos= saved_pos + 5
            self.cursor_pos+=2            
            self.M_window.dft_wnd.dft_win[self.option_pos+self.cursor_pos]  = '|'
            self.M_window.dft_wnd.dft_win[self.option_pos+self.cursor_pos] += ' '*int((int( self.M_window.dft_wnd.x_size - len(self.options['option 1']))/2) - 1 - len(self.cursor))
            self.M_window.dft_wnd.dft_win[self.option_pos+self.cursor_pos] += self.cursor
            self.M_window.dft_wnd.dft_win[self.option_pos+self.cursor_pos] += self.options.get(self.map_opt[self.cursor_pos])
            self.M_window.dft_wnd.dft_win[self.option_pos+self.cursor_pos] += ' '*(self.M_window.dft_wnd.x_size - len(self.M_window.dft_wnd.dft_win[self.option_pos+self.cursor_pos]) - 1 )    
            self.M_window.dft_wnd.dft_win[self.option_pos+self.cursor_pos] += '|'
            self.option_pos = saved_pos
        

