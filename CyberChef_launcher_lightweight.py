import os
import subprocess
import webbrowser
import time
import sys

PORTS = (8000, 5500, 8080, 8888, 3000)
HTML_NAME = 'CyberChef_v11.4.0.html'

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root_dir)

    for p in PORTS:
        server = subprocess.Popen(
            [sys.executable, '-m', 'http.server', str(p)]
        )
        time.sleep(1)
        if server.poll() is None:
            webbrowser.open(f'http://localhost:{p}/{HTML_NAME}')
            server.wait()
            return


if __name__ == '__main__':
    main()