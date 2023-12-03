from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import json
import pyautogui

SERVER_PORT = 8080
# example of POST: {"content":"730869274163","raw":"373330383639323734313633","format":"CODE_128","errorCorrectionLevel":"","version":"","sequenceSize":"-1","sequenceIndex":"-1","sequenceId":"","timestamp":"2023-12-02 15:07:11"}
# example of GET: /?content=730869274163&raw=373330383639323734313633&format=CODE_128&errorCorrectionLevel=&version=&sequenceSize=-1&sequenceIndex=-1&sequenceId=&timestamp=2023-12-02+15%3A09%3A50 HTTP/1.1" 200 -

# https://gist.github.com/mscalora/b6f86291353c360cb5550dc978129069
# https://stackoverflow.com/questions/2490162/parse-http-get-and-post-parameters-from-basehttphandler
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a GET response"
        self.wfile.write(bytes(message, "utf8"))
    def do_POST(self):
        #self.send_response(200)
        self.send_response_only(200)
        self.end_headers()
        print(self.headers)
        post_data_length = int(self.headers.get('content-length'))
        field_data = self.rfile.read(post_data_length)
        fields = parse.parse_qs(str(field_data,"UTF-8"))
        #fields_json = json.dumps(fields, indent=2)
        content = fields["content"][0]
        print(content)
        if content != "" :
            pyautogui.press("enter")
            pyautogui.typewrite(content, interval=0.1)
            pyautogui.press("enter")


with HTTPServer(('', SERVER_PORT), handler) as server:
    server.serve_forever()

