import time
class GPSLogger:
    def __init__(self):
        self.log={}
        self.lastInsert={}
        pass
    def insert(self,x,y,time=0):
        self.log[x,y]=time
        self.lastInsert={}
        self.lastInsert[x,y]=time
    def print(self):
        for x,y in self.log.items():
            print(f'{x[0]}:{x[1]} orario:{y}')
    def lastLog(self):
        return self.lastInsert
    def getBaricentro(self):
        sommaX=0
        sommaY=0
        for x in self.log.keys():
            sommaX+=x[0]
            sommaY+=x[1]
        return [sommaX/len(self.log),sommaY/len(self.log)]
    def __str__(self):
        output =''
        for x,y in self.log.items():
            output+=f'lat:{x[0]} lon:{x[1]} orario:{y}\n'
        return output


def getData():
    return time.strftime('%S:%M:%H',time.localtime())
if __name__ == '__main__':
    print(time.localtime())
    tragitto = GPSLogger()
    tragitto.insert(0,0,time=getData())
    time.sleep(1)
    tragitto.insert(0,3,time=getData())
    time.sleep(1)
    tragitto.insert(4,5,time=getData())
    tragitto.print()
    print(tragitto.lastLog())
    print(tragitto.getBaricentro())

    print(tragitto)