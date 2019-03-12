import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8003


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')


        if self.path == '/':

            filename = 'form22.html'
            # Open the form1.html file
            f = open(filename, 'r')
            contents = f.read()
            f.close()

        elif '/echo' in self.path:
            if 'chk=on' in self.path:
                msg = self.path.split('=')[1]
                msgg= msg.split('&')[0]
                msgg=msgg.upper()

                contents = """<!DOCTYPE html>
                            <html lang="en" dir="ltr">
                            <head>
                            <meta charset="utf-8">
                            <title>Echo of the Received Message</title>
                            </head>
                            <h1>Echo of the Received Message</h1>
                            <body style="background-color: yellow"><br>"""+msgg+"""<p><a href="/">[Main Page]</a></p></body></html>"""
            else:
                msg = self.path.split('=')[1]
                msgg = msg.split('&')[0]

                contents ="""<!DOCTYPE html>
                            <html lang="en" dir="ltr">
                            <head>
                            <meta charset="utf-8">
                            <title>Echo of the Received Message</title>
                            </head>
                            <h1>Echo of the Received Message</h1>
                            <body style="background-color: yellow">"""+msgg+"""<p><a href="/">[Main Page]</a></p></body></html>"""

        else:
            filename = 'error.html'
            # Open the form1.html file
            f = open(filename, 'r')
            contents = f.read()
            f.close()


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")