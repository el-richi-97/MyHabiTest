from http.server import HTTPServer
from app.habi_properties_query.server import Handler, HOST, PORT

if __name__ == '__main__':
    with HTTPServer((HOST, int(PORT)), Handler) as server:
        print(f'Starting server on: {HOST}:{PORT}')
        server.serve_forever()

