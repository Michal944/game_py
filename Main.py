import project_game_window as Menu
import levels as lev1
import desk_ply as desk



class Run():
    def __init__(self,x_size):
        self.desk = desk.Desk(10,x_size)
        self.Menu1 = Menu.user_menu(x_size)
        self.level = []
        self.level.append(lev1.Window_L1(x_size))
        self.flag_menu = False
        
    def start(self):
        self.Menu1.options_init()
        self.Menu1.option_on_screen()
        self.Menu1.dsp_user_menu()
    def new_game(self):
        self.flag_menu = True        
        self.level[0].prepare_game()
        self.level[0].insert_desk(self.desk)
        


Run1 = Run(60)
Run1.start()
Run1.new_game()

