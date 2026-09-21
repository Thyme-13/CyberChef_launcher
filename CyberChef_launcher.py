import os
import sys
import subprocess
import webbrowser
import time
import functools

if sys.platform == 'win32':
    import ctypes


HTML_NAME = 'CyberChef_v11.4.0.html'
PORTS = (8000, 5500, 8080, 8888, 3000)
BIND_ADDR = '127.0.0.1'


def show_error(message: str) -> None:
    if sys.platform == 'win32':
        ctypes.windll.user32.MessageBoxW(0, message, 'CyberChef Launcher', 0x10)
    else:
        print(f'[CyberChef Launcher] {message}', file=sys.stderr)


def run_in_process(script_dir: str, p: int) -> None:
    from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
    handler = functools.partial(SimpleHTTPRequestHandler, directory=script_dir)
    httpd = ThreadingHTTPServer((BIND_ADDR, p), handler)
    webbrowser.open(f'http://{BIND_ADDR}:{p}/{HTML_NAME}')
    httpd.serve_forever()


def main() -> int:
    if getattr(sys, 'frozen', False):
        script_dir = os.path.dirname(sys.executable)
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))

    html_path = os.path.join(script_dir, HTML_NAME)
    if not os.path.isfile(html_path):
        show_error(f'HTML file not found: {HTML_NAME}')
        return 1

    for p in PORTS:
        if getattr(sys, 'frozen', False):
            try:
                run_in_process(script_dir, p)
            except OSError:
                continue
            return 0

        try:
            server = subprocess.Popen(
                [sys.executable, '-m', 'http.server', '--bind', BIND_ADDR, '--directory', script_dir, str(p)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0,
            )
        except Exception as e:
            show_error(f'Failed to start server on port {p}: {e}')
            continue

        time.sleep(0.15)
        if server.poll() is None:
            try:
                webbrowser.open(f'http://{BIND_ADDR}:{p}/{HTML_NAME}')
            except Exception as e:
                show_error(f'Failed to open browser: {e}')
                server.terminate()
                return 1

            try:
                server.wait()
            except KeyboardInterrupt:
                server.terminate()
            return 0

    show_error(f'No available port (tried: {", ".join(map(str, PORTS))})')
    return 1


if __name__ == '__main__':
    sys.exit(main())
