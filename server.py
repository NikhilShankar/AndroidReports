from http.server import HTTPServer, SimpleHTTPRequestHandler
import os


class ReportHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="/reports", **kwargs)

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>CI Reports</title>
                <style>
                    body { font-family: Arial; margin: 50px; }
                    h1 { color: #333; }
                    .links { margin-top: 30px; }
                    a { 
                        display: block; 
                        padding: 15px; 
                        margin: 10px 0;
                        background: #007bff;
                        color: white;
                        text-decoration: none;
                        border-radius: 5px;
                        width: 200px;
                        text-align: center;
                    }
                    a:hover { background: #0056b3; }
                </style>
            </head>
            <body>
                <h1>Android CI Reports</h1>
                <div class="links">
                    <a href="/testresults/index.html">Unit Test Results</a>
                    <a href="/lint/index.html">Lint Report</a>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
        else:
            super().do_GET()


def run(server_class=HTTPServer, handler_class=ReportHandler, port=9898):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    print(f'Access reports at:')
    print(f'  http://localhost:{port}/')
    print(f'  http://localhost:{port}/testresults/index.html')
    print(f'  http://localhost:{port}/lint/index.html')
    httpd.serve_forever()


if __name__ == '__main__':
    run()