import os
import datetime
import colorama

# Decorational Settings
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
            print(f"{shiftspaces} [{listx.index(i)}]: {i}")


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
    def __init__(self):
        pass


    map_func = {
        'main': {
            '0' : '',
            '1' : '',
            '2' : '',
        }


    }

    def command_exists_recursive(self, dicx, command, index, isfound):
        
        try:



        except KeyError:

    
    def get_response(self, inputx, place):
        inputx = inputx.split(' ')
        command = [item for item in inputx if item != '']

        for parameter in command:
            map_func





        
        







# Menu Handling
class Menu:
    dec = Decor()
    def __init__(self):
        pass

    def askforinput(self, place):

        response_handler = Response()
        run = 1

        while run == 1:
            
            userinput = input(f'{self.dec.textmultiplier(self.dec.terminalwidth //4 )} >>> ')
            my_response = response_handler.get_response(userinput, place)
            #print(colorama.Style.BRIGHT, f'{self.dec.textmultiplier(self.dec.terminalwidth // 4)}[#] {my_response} ', colorama.Style.NORMAL)



    def showmain(self):
        self.dec.clearterminal()


        maintitle = self.dec.justifycenter('''
█████████████████████████████████████████████████████
█─▄▄─█▄─▄▄─█▄─▄▄─█▄─▀█▄─▄█▀▀▀▀▀██─▄─▄─█▄─▀█▀─▄█─▄▄▄▄█
█─██─██─▄▄▄██─▄█▀██─█▄▀─███████████─████─█▄█─██▄▄▄▄─█
▀▄▄▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▀▀▀▀▀▀▀▄▄▄▀▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀''')
        subtitle = self.dec.justifycenter('By @Arkarimi On Github')
        actionlist = ['Time Management', 'Analysis', 'Settings']

        


        print(maintitle)
        print(subtitle)
        # "makelist" : function for decorated list display + print
        
        print( colorama.Style.BRIGHT, f'{self.dec.textmultiplier(self.dec.terminalwidth // 4)} [!] Type in your choice/shortcut ', colorama.Style.NORMAL)
        print(colorama.Style.BRIGHT, f'{self.dec.textmultiplier(self.dec.terminalwidth // 4)} ⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻ ', colorama.Style.NORMAL)
        
        self.dec.makelist(actionlist)

        print()
        self.askforinput('main')

m = Menu()
m.showmain()



        

