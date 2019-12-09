from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 5507

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		#self.wfile.write("Hello World !")
		#https://stackoverflow.com/questions/4706499/how-do-you-append-to-a-file-in-python
		with open("python_logs.txt", "a") as myfile:
			myfile.write("This API endpoint was hit! GET \n")
		return
	def do_POST(self):
		self.send_response(200)
		self.end_headers()
		#https://stackoverflow.com/questions/4706499/how-do-you-append-to-a-file-in-python
		with open("python_logs.txt", "a") as myfile:
			myfile.write("This API endpoint was hit! POST \n")

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()




