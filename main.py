import os
import datetime
import colorama
from datamanage import Data
from dateutil.relativedelta import relativedelta

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
            print()
            return userinput
        
        else:
            userinput = input(f'{self.textmultiplier(self.terminalwidth //4 )}  >>> ')
            print()

        return userinput



        

    










class Main:
    dec = Decor()
    
    latestresponse = []
    maincmds = ['exit']

    def __init__(self):
        pass

    def immediatecommand(self, command):
        pass

    def showmain(self, newpage=1):
        if newpage == 1:
            self.dec.show_main_title()

        actionlist = ['Time Management', 'Analysis', 'Settings']


        # "makelist" : function for decorated list display + print

#        self.show_main_title()
        
        self.dec.alert('Type in your choice/shortcut')
        
        self.dec.makelist(actionlist)

        print()
        self.askforinput('main')

    
    #returns boolean values if command is immddiate
    def checkimmediatecommand(self, command):
        if command in self.maincmds:
            return True
        else:
            return False

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

    def shortcut_return_valid_date(self,command):
        #check if command is right
        listofcommands = ['days', 'months', 'years']
        howmanyofcommands = [0,0,0]
        
        #removing -s from the commands
        command = command[1:]
        if len(command) % 2 == 0 and len(command) > 0 and len(command) <=6:
            validation_step1 = 1
            for i in range(0, len(command)):
                if i % 2 == 0:
                    if command[i].isnumeric() == 0:
                        validation_step1 = 0
                else:
                    if command[i] not in listofcommands:
                        validation_step1 = 0
                    else:
                        howmanyofcommands[listofcommands.index(command[i])] += 1

            #checks if all values are 0
            sumx = 0
            if validation_step1 == 1:
                for i in howmanyofcommands:
                    if i > 1:
                        validation_step1 = 0
                    else:
                        sumx += i
            else:
                return False
            
            print('jo')
            if validation_step1 == 1 and sumx == 0:
                return False
            
            # If the program continues further from here it means that validation_step1 == 1
            # with this assumption sumx counts the number of listofcommands[] elements the main command has called
            # with that assumption ...

            #this variable here shows how many d,m,y do we need to get back
            valuescorwithcommandindex = [0,0,0]
            for i in range(0,len(command)):
                #up to now we are sure that the command is in the following format
                # number, cmd, number, cmd ...
                # so with that and knowing that our counter is 0 based we can say that if our counter number mod 2 == 0
                # the counter is pointing at a number that corelates to the string with the index countercalue+1

                if i % 2 == 0:
                    valuescorwithcommandindex[listofcommands.index(command[i+1])] += int(command[i])

                # this might have become too complicated i may change this later on ... !
                # I think I could have implemented it in better and clearer way

            
            prefinaldate = datetime.datetime.now()
            finaldate = prefinaldate - relativedelta(years=valuescorwithcommandindex[2], months=valuescorwithcommandindex[1]) - datetime.timedelta(days=valuescorwithcommandindex[0])

            print(finaldate)
            #here we return the database table name that is responsible for storing the wanted time values
            return f'rec_{finaldate.year}_{finaldate.month}_{finaldate.day}'

            

            
        else:
            return False



    def add_time(self,today):
        data = Data()

        tablename = ''
        if today == 1:
            todayexists = data.checktodayexists()
            if todayexists == 0:
                data.addDay()

            tablename = data.todayTableName()


            self.dec.alert('Today Selected! ...')
            self.daymanage_viewday(date)
            
        else:
            #you can pass in prev days in two ways ( -p 2 ) = 2 days before and yyyymmdd
            validdate = 0
            while validdate == 0:
                rawdate = self.dec.request("Enter date in (yyyy/mm/dd) or shortcut (starting with -s): ", showreqtext=1)
                if self.checkimmediatecommand(rawdate) == True:
                    self.immediatecommand()
                else:
                    # check if is shortcut or not
                    shortcutx = rawdate.split(' ')
                    shortcutx = [shct for shct in shortcutx if not '']
                    print(shortcutx)
                    if shortcutx[0] == '-s':
                        # shortcut function -- shortcut_return_valid_date
                        date = self.shortcut_return_valid_date(shortcutx)
                        if date != False:
                            dbexists = Data.checkotherdayexists(date)

                            tablename = date
                            validdate = 1
                            if dbexists != 1:
                                Data.addtable(self,name=date)
                                self.dec.alert(f'Day: {date} selected! ... [NewDay]''')
                            else:
                                
                                self.dec.alert(f'Day: {date} selected! ...''')

            self.daymanage_viewday(date)

    def showtable(self, key, date):
        datamanage = Data()
        daydata = datamanage.getdaydata(date=date)

        # Apply time sort
        if key[0] != '':
            stval = key[0].split(':')
            for i in daydata:
                pass




    def daymanage_viewday(self,date):

        
        # shortcut structure
        # * means show everything
        
        # -ts xx:yy is start time sort
        # -te xx:yy is end time sort
        # if only start time or endtime is passed
        # the other is considered as default

        # -tag x, y, z... selects desigered tags from the data
        # -pr num selects desigered priority tags from the table

        def returnsortkeys(self, cmd):
            sortkeys = ['', '', [], []]

            if cmd == '':
                return sortkeys

            cmdlist = cmd.split(' ')
            cmdlist = [ i for i in cmdlist if i != '']

            dashcommands = ['-st','-et','-pr','-tags']

            if cmdlist[0] not in dashcommands:
                return 0
            else:
                cmdstate = cmdlist[0]
                for i in cmdlist:
                    if i in dashcommands:
                        cmdstate = i
                    else:
                        cmdindex = dashcommands.index(cmdstate)
                        if cmdindex > 1:
                            sortkeys[cmdindex].append(i)
                        else:
                            sortkeys[cmdindex] = i

            return sortkeys
        

        validcmd = 0

        while validcmd == 0:
            cmd = self.dec.request('Enter your shortcut or Pass nothing: ')
            rsk = returnsortkeys(cmd)
            if rsk != 0:
                validcmd = 1
                self.showtable(rsk,date)


            else:
                self.dec.alert('Wrong Input ...')

        if cmd == '':
            pass



            



            





    map_func = {
        'main': {
            '0' : show_time_management,
            '1' : '',
            '2' : '',
        },

        'Time-Manage' : {
            #today
            '0' : lambda self: self.add_time(1),
            #load day
            '1' : lambda self: self.add_time(0),
            '2' : showmain,

        },

        'Day-Manage' : {
            # view / add / edit
            '0' : '',
            '1' : '',
            '2' : '',
        },

        'View-Day' : {


        },


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



        

