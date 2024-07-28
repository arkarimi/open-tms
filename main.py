import os
import datetime
import colorama
import datamanage as dm

# Decoration Settings
class Decor:
    
    terminalwidth = os.get_terminal_size().columns
    
    def __init__(self):
        pass

    def clearterminal(self):
        if os.name == 'nt':
            cmd = os.system('cls')
        else:
            cmd = os.system('clear')


    def textmultiplier(self, charcnt=10, charx=' ', linecnt=1):
        #char must be string
        #charcnt and linecnt must be int
        
        final = ''''''

        for i in range(0, linecnt):
            for ii in range(0, charcnt):
                final += ' '


        return final
    
    def makelist(self, listx, shiftamount=4):
        #Shifting texts using spaces
        shiftspaces = self.textmultiplier(self.terminalwidth // shiftamount)
        
        for i in listx:
            print(f"{shiftspaces}  [{listx.index(i)}]: {i}")


    def justifycenter(self, text):
        splitedtxt = text.split("\n")
        final = ''
        
        for item in splitedtxt: 
            for i in range(0, (os.get_terminal_size().columns - len(item)) // 2):
                final += ' '

            final += item
            final += "\n"

        return final
    










class Response:
    dec = Decor()
    
    latestresponse = []

    def __init__(self):
        pass


    def askforinput(self, place):

        response_handler = Response()
        run = 1

        while run == 1:
            
            userinput = input(f'{self.dec.textmultiplier(self.dec.terminalwidth //4 )} >>> ')
            my_response = response_handler.get_response(userinput, place)
            
            if my_response == False:
                print(colorama.Style.BRIGHT, f'{self.dec.textmultiplier(self.dec.terminalwidth // 4)}[#] Command Does Not Exist. Try Again / Use Help Menu ', colorama.Style.NORMAL)
                print()

                

    def show_time_management(self):
        actionlist = ['add', 'view', 'edit']


        # "makelist" : function for decorated list display + print
        
        print( colorama.Style.BRIGHT, f'{self.dec.textmultiplier(self.dec.terminalwidth // 4)} [!] Type in your choice/shortcut ', colorama.Style.NORMAL)
        print(colorama.Style.BRIGHT, f'{self.dec.textmultiplier(self.dec.terminalwidth // 4)} ⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻ ', colorama.Style.NORMAL)
        
        self.dec.makelist(actionlist)

        print()
        self.askforinput('main')



    map_func = {
        'main': {
            '0' : show_time_management,
            '1' : '',
            '2' : '',
        },

        'TimeManage' : {
            #today
            '0' : '',
            #load day
            '1' : '',

        },

        'Today' : {
            # view / add / edit
            '0' : '',
            '1' : '',
            '2' : '',
        }


    }


    #Temporary class variables to deal with the function below

    temp_run = True
    temp_done = False

    def command_exists_recursive(self,dicx, command, index):
        
        if self.temp_run == True:
            
            #Checking wether its the last parameter or not
            if index == len(command) - 1:
                
                # Check if command exists in dict and also is a function
                # * note that the dictionary is architected in a way that..
                # ..all outer subdictionaries are strings to specify the path..
                # ..and the inner dictionary (the last subdictionary available to access)..
                # ..is a function. so with that assumption we need to make sure the command is not..
                # ..a callable function 

                if command[index] in dicx and callable(dicx[command[index]]):
                    dicx[command[index]](self)
                    self.temp_done = True
                
                else:
                    if index == 0:
                        return False
                
                self.temp_run = False
            
            else:
                
                if command[index] in dicx and callable(dicx[command[index]]) == False:
                    dicx = dicx[command[index]]
                    index += 1

                    self.command_exists_recursive(dicx, command, index)
                
                else:
                    self.temp_run = False
                    if index == 0:
                        return False
        
        
        else:
            
            if index == 0:
                
                if self.temp_done == False:
                    return False


        
    

    
    def get_response(self, inputx, place):
        inputx = inputx.split(' ')
        command = [item for item in inputx if item != '']

        r = self.command_exists_recursive(self.map_func[place], command,0)
        
        prev_temp_done = self.temp_done        
        self.temp_done = False
        self.temp_run = True


        return True if prev_temp_done == True else False
        




        
        







# Menu Handling
class Menu:
    dec = Decor()
    res = Response()

    loc = 'main'

    
    def __init__(self):
        pass


                            
    def show_main_title(self):


        self.dec.clearterminal()


        maintitle = self.dec.justifycenter('''
█████████████████████████████████████████████████████
█─▄▄─█▄─▄▄─█▄─▄▄─█▄─▀█▄─▄█▀▀▀▀▀██─▄─▄─█▄─▀█▀─▄█─▄▄▄▄█
█─██─██─▄▄▄██─▄█▀██─█▄▀─███████████─████─█▄█─██▄▄▄▄─█
▀▄▄▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▀▀▀▀▀▀▀▄▄▄▀▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀''')
        subtitle = self.dec.justifycenter('By @Arkarimi On Github')


            


        print(maintitle)
        print(subtitle)
        print()
        print()

    def showmain(self):

        actionlist = ['Time Management', 'Analysis', 'Settings']


        # "makelist" : function for decorated list display + print

#        self.show_main_title()
        
        print( colorama.Style.BRIGHT, f'{self.dec.textmultiplier(self.dec.terminalwidth // 4)} [!] Type in your choice/shortcut ', colorama.Style.NORMAL)
        print(colorama.Style.BRIGHT, f'{self.dec.textmultiplier(self.dec.terminalwidth // 4)} ⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻ ', colorama.Style.NORMAL)
        
        self.dec.makelist(actionlist)

        print()
        self.res.askforinput('main')

    def choose():



        

m = Menu()
m.show_main_title()
m.showmain()



        

