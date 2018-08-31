import threading
import time

class Ticker(threading.Thread):
    
    def __init__(self):
        super().__init__()
        self.seconds = 0
        self.is_work = True
        self.is_print = True
        self.event = threading.Event()
        self.event.set()

    def run(self):
        self.start()

    def start(self):
        while self.is_work:
            self.event.wait()
            self.seconds += 1
            if self.is_print:
                print(str(self.seconds) + '*' * 30, end = '\r')
            time.sleep(1)
    
    def pause(self):
        print('pause')
        self.event.clear()

    def stop(self):
        self.is_work = False

    def begin(self):
        self.event.set()

    def restart(self):
        self.seconds = 0

    def silence(self):
        self.is_print = False

    def unsilence(self):
        self.is_print = True


class HendlerTicker(threading.Thread):
    
    def __init__(self, ticker):
        super().__init__()
        self.is_work = True
        self.ticker = ticker        
        self.list_hendler = {
            'start': ticker.begin,
            'stop': self.stop,
            'restart': ticker.restart,
            'pause': ticker.pause,
            'silence': ticker.silence,
            'unsilence': ticker.unsilence,
            'help': self.help_command
        }

    def help_command(self):
        print(self.list_hendler.keys())

    def stop(self):
        self.ticker.stop()
        self.is_work = False

    def run(self):
        while self.is_work:
            u_input = input('help?')
            print(u_input)
            self.handle(u_input)

    def handle(self, command):
        if command in self.list_hendler:
            self.list_hendler[command]()

        

ticker2 = Ticker()
handler_ticker = HendlerTicker(ticker2)

handler_ticker.start()
ticker2.start()
