class Response:
    def __init__(self):
        pass



    def hi(self):
        print('hi')

    
    map_func = {'main' : {'1' : { '2' : { '3' : hi}}}}

    def command_exists_recursive(self,dicx, command, index, keyerror):
        if keyerror == 0:
            if index < len(command) - 1:
                try:
                    dicx = dicx[command[index]]
                except KeyError:

                    keyerror = 1

                index += 1
                self.command_exists_recursive(dicx, command, index, keyerror)

                if index == len(command) - 1 and keyerror == 0:
                    try:
                        newdic = dicx[command[index]]
                    except KeyError:
                        keyerror = 1
                    if keyerror == 0:
                        print(newdic)
                        newdic(self)


        else:
            return False




c = Response()
m = c.command_exists_recursive(c.map_func['main'], ['1', '2', '3'], 0, 0)
print(m)