#Levels
from desk_ply import Desk as D
from project_game_window import Window


class Window_L1(Window):
    def __init__(self,_x=60, _y=25):
        super().__init__(_x,_y)
        self.puzzle = (
            "|___| |___| |____| |___| |___| |___| |____| |______|",
            "|______| |____| |____| |___| |_____| |___| |_____|  ",
            "|_______________| |_______|  |_________|  |_____|   " )
    def center_line(self, arg_puzzle):
        if self.x_size-2 == 0:
                raise Exception('Error! Wrong size of window #15levels')
        return int(((self.x_size-2) - len(arg_puzzle))/2)

    def ins_to_screen(self, text, locate, p_start):
            self.crt_str_wnd()
            if self.x_size-2 == 0:
                raise Exception('Error! Wrong size of window #18levels')
            locate_all = {'right' : int(self.x_size - len(text[0]) - 2),
                          'centre': self.center_line(text),
                          'left'  : 2}
            try:
                if locate.lower() == 'right':
                    for item in text: 
                        self.dft_win[p_start] = '|'
                        self.dft_win[p_start] += ' '* locate_all.get(locate.lower())
                        self.dft_win[p_start] += item
                        self.dft_win[p_start] += '|'
                        p_start+=2
                        if p_start >= self.y_size:
                            break;

                elif locate.lower() == 'left':                
                    for item in text: 
                        self.dft_win[p_start] = '|'
                        self.dft_win[p_start] += " "*locate_all[locate.lower()]
                        self.dft_win[p_start] += item
                        self.dft_win[p_start] += " "* (self.x_size-len(self.dft_win[p_start]) -1)
                        self.dft_win[p_start] += '|'
                        p_start+=2
                        if p_start >= self.y_size:
                            break;
                elif locate.lower() == 'centre':    
                    for item in text: 
                        self.dft_win[p_start] = '|'
                        self.dft_win[p_start] += " "*locate_all[locate.lower()]
                        self.dft_win[p_start] += item
                        self.dft_win[p_start] += " "*locate_all[locate.lower()]
                        self.dft_win[p_start] += '|'
                        p_start+=2
                        if p_start >= self.y_size:
                            break;
            except:
                print('wrong locate value')
            
        
        
    def crt_level(self, start_x=5):
        index_puzzle=0
        for item in self.puzzle: 
           self.dft_win[start_x] = '|'
           self.dft_win[start_x] += " "*self.center_line(self.puzzle[index_puzzle])
           self.dft_win[start_x] += item
           self.dft_win[start_x] += " "*self.center_line(self.puzzle[index_puzzle])
           self.dft_win[start_x] += '|'
           start_x+=2
    def prepare_game(self):
        self.crt_str_wnd()
        self.crt_level()        
        

    def insert_desk(self, desk):
        desk2 = desk.get_desk()
        self.dft_win[-3] = desk2[0]
        self.dft_win[-2] = desk2[1]
        self.dsp_window()
