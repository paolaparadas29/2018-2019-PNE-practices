import http.server
import socketserver
import termcolor

PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # -- printing the request line
        termcolor.cprint(self.requestline, 'green')

        if self.path == '/':
            f = open('form1.html','r')
            contents = f.read()
            f.close()

        elif '/echo' in self.path:
            contents = """<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Echo of the Received Message</title>
  </head>
  <h1>Echo of the Received Message</h1>
  <body style="background-color: yellow">"""+self.path.split('=')[1]+"""<br><a href="/">[Main Page]</a></body></html>"""

        else:
            f = open('error.html','r')
            contents = f.read()
            f.close()


        self.send_response(200)

        self.send_header('Content-Type', 'test/html')
        self.send_header('Content-Lenght', len(str.encode(contents)))
        self.end_headers()

        # Sending the body of the response message
        self.wfile.write(str.encode(contents))


# Main program

with socketserver.TCPServer(('', PORT), TestHandler) as httpd:
    print('Serving at port: {}'.format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Stopped by the user')
        httpd.server_close()

print('The server is stopped')
