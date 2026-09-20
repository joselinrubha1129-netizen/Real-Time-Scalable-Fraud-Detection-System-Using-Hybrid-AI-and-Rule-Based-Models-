"""
Standalone Web Server for SentinelAI Website Dashboard
Serves the frontend interface independently on http://127.0.0.1:3000
"""

import http.server
import os
import socketserver
import webbrowser

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


def run_server():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
        print("===============================================================")
        print(f"  SentinelAI Website Dashboard running at: http://127.0.0.1:{PORT}")
        print(f"  Serving directory: {DIRECTORY}")
        print("  Connected to Backend REST API at: http://127.0.0.1:8000")
        print("===============================================================")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nDashboard server stopped.")


if __name__ == "__main__":
    run_server()
