import http.server
import socketserver
import termcolor
from Seq import Seq

sequenceproof = 'ACTGactg'

# Define the Server's port
PORT = 8008


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def function(self, t, d):
        # Function which performs the task that the client is asking for

        s1 = Seq(t)

        if d == 'len':
            s2 = s1.len()
            return s2
        elif d == 'complement':
            s2 = s1.complement()
            return s2.strbases
        elif d == 'reverse':
            s2 = s1.reverse()
            return s2.strbases
        elif d == 'countA':
            s2 = s1.count('A')
            return s2
        elif d == 'countC':
            s2 = s1.count('C')
            return s2
        elif d == 'countT':
            s2 = s1.count('T')
            return s2
        elif d == 'countG':
            s2 = s1.count('G')
            return s2
        elif d == 'percA':
            s2 = s1.perc('A')
            return s2
        elif d == 'percC':
            s2 = s1.perc('C')
            return s2
        elif d == 'percT':
            s2 = s1.perc('T')
            return s2
        elif d == 'percG':
            s2 = s1.perc('G')
            return s2

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        global response
        termcolor.cprint(self.requestline, 'green')

        if self.path == '/':

            filename = 'form1.html'
            # Open the form1.html file
            f = open(filename, 'r')
            contents = f.read()
            f.close()

        elif '/seq' in self.path:

            contents = """<!DOCTYPE html>
            <html lang='en'>
            <head>
                <meta charset='UTF-8'>
                <title>Server Response</title>
            </head>
            <body style='brackground-color: white'>"""

            request = self.path.split('=')[1]
            request1 = request.split('&')
            DNAsequence = request1[0]
            contents = contents + '<p>DNA sequence: ' + DNAsequence + '</p>'

            response = ''
            for i in DNAsequence:

                if i not in sequenceproof:
                    response = 'Error\n'
                    break
                else:
                    response = 'OK\n'

            if response == 'OK\n':

                s = DNAsequence
                if 'chk=on' in self.path:
                    Lenght = self.function(s, 'len')
                    contents = contents + "<p>Lenght: " + str(Lenght) + "</p>"
                operation = self.path.split('operation=')[1].split("&")[0]
                contents = contents + "<p>Operation: " + operation + "</p>"
                base = self.path.split('base=')[1].split("&")[0]
                contents = contents + "<p>Base: " + base + "</p>"
                combination = operation + base
                response = self.function(s, combination)
                contents = contents + "<p>Response: " + str(response) + "</p>"

            else:
                contents = contents + "<p>It is not a valid sequence</p>"

            contents = contents + """<br> <a href="/"> [Main page] </a>
                       </body></html>"""
        else:
            f = open('error.html', 'r')
            contents = f.read()

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
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")
