import os
import datetime
import colorama
from datamanage import Data as data

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
    
    def alert(self, text, showseperator=1):
        lendashsfordecor = '⁻' * (len(text)+4)

        print( colorama.Style.BRIGHT, f'{self.textmultiplier(self.terminalwidth // 4)} [!] {text} ', colorama.Style.NORMAL)
        if showseperator:
            print( colorama.Style.BRIGHT, f'{self.textmultiplier(self.terminalwidth // 4)} {lendashsfordecor} ', colorama.Style.NORMAL)



    
                            
    def show_main_title(self):


        self.clearterminal()


        maintitle = self.justifycenter('''
█████████████████████████████████████████████████████
█─▄▄─█▄─▄▄─█▄─▄▄─█▄─▀█▄─▄█▀▀▀▀▀██─▄─▄─█▄─▀█▀─▄█─▄▄▄▄█
█─██─██─▄▄▄██─▄█▀██─█▄▀─███████████─████─█▄█─██▄▄▄▄─█
▀▄▄▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▀▀▀▀▀▀▀▄▄▄▀▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀''')
        subtitle = self.justifycenter('By @Arkarimi On Github')


            


        print(maintitle)
        print(subtitle)
        print()
        print()

    
    def request(self, request='', showreqtext=0, place=''):
        if showreqtext==1:
            lendashsfordecor = '⁻' * (len(request)+4)
            print( colorama.Style.BRIGHT, f'{self.textmultiplier(self.terminalwidth // 4)} [!] {request} ', colorama.Style.NORMAL)
            print( colorama.Style.BRIGHT, f'{self.textmultiplier(self.terminalwidth // 4)} {lendashsfordecor} ', colorama.Style.NORMAL)

        if place != '':
            userinput = input(f'{self.textmultiplier(self.terminalwidth //4 )}  {place} | >>> ')
            return userinput
        
        else:
            userinput = input(f'{self.textmultiplier(self.terminalwidth //4 )}  >>> ')

        return userinput



        

    










class Main:
    dec = Decor()
    
    latestresponse = []

    def __init__(self):
        pass


    def showmain(self):

        actionlist = ['Time Management', 'Analysis', 'Settings']


        # "makelist" : function for decorated list display + print

#        self.show_main_title()
        
        self.dec.alert('Type in your choice/shortcut')
        
        self.dec.makelist(actionlist)

        print()
        self.askforinput('main')

    


    def askforinput(self, place):

        response_handler = Main()
        run = 1

        while run == 1:
            
            userinput = self.dec.request(place=place)

            my_response = response_handler.get_response(userinput, place)
            
            if my_response == False:
                print(colorama.Style.BRIGHT, f'{self.dec.textmultiplier(self.dec.terminalwidth // 4)}[#] Command Does Not Exist. Try Again / Use Help Menu ', colorama.Style.NORMAL)
                print()

                

    def show_time_management(self):
        self.dec.clearterminal()
        self.dec.show_main_title()
        actionlist = ['Load Today', 'Load Other Days', 'Back']


        # "makelist" : function for decorated list display + print
        
        print( colorama.Style.BRIGHT, f'{self.dec.textmultiplier(self.dec.terminalwidth // 4)} [!] Type in your choice/shortcut ', colorama.Style.NORMAL)
        print(colorama.Style.BRIGHT, f'{self.dec.textmultiplier(self.dec.terminalwidth // 4)} ⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻ ', colorama.Style.NORMAL)
        
        self.dec.makelist(actionlist)

        print()
        self.askforinput('Time-Manage')

    def add_time(self, today):

        tablename = ''
        if today == 1:
            todayexists = data.checktodayexists()
            if todayexists == 0:
                data.addDay()

            tablename = data.todayTableName()

            self.dec.alert('Today Selected! ...')

            
        else:
#            self.dec.request()
            pass



    map_func = {
        'main': {
            '0' : show_time_management,
            '1' : '',
            '2' : '',
        },

        'Time-Manage' : {
            #today
            '0' : add_time(today=1),
            #load day
            '1' : add_time(today=0),

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
        




        
        






        

m = Main()
d = Decor()
d.show_main_title()
m.showmain()



        

