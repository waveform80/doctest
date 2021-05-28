#!/usr/bin/python3

import sys
import time
import socket
import argparse
import subprocess as sp
import multiprocessing as mp
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler


__version__ = '0.1'


class DevRequestHandler(SimpleHTTPRequestHandler):
    server_version = 'DocsPreview/' + __version__
    protocol_version = 'HTTP/1.0'


class DevServer(ThreadingHTTPServer):
    allow_reuse_address = True
    base_path = None


def get_best_family(*address):
    infos = socket.getaddrinfo(
        *address,
        type=socket.SOCK_STREAM,
        flags=socket.AI_PASSIVE,
    )
    family, type, proto, canonname, sockaddr = next(iter(infos))
    return family, sockaddr


def server(config, queue=None):
    try:
        DevServer.address_family, addr = get_best_family(config.bind, config.port)
        handler = partial(DevRequestHandler, directory=config.html_path)
        with DevServer(addr, handler) as httpd:
            host, port = httpd.socket.getsockname()[:2]
            hostname = socket.gethostname()
            print(f'Serving {config.html_path} HTTP on {host} port {port}')
            print(f'http://{hostname}:{port}/ ...')
            httpd.serve_forever()
    except Exception as e:
        if queue is not None:
            queue.put(e)
        raise


def get_stats(path):
    for p in path.iterdir():
        if p.is_dir():
            yield from get_stats(p)
        else:
            yield p, p.stat()


def rebuild(config):
    print(f'Rebuilding...')
    sp.run(['make', 'html'], cwd=Path(__file__).parent)
    return max(
        stat.st_mtime for p, stat in get_stats(config.html_path))


def builder(config, queue=None):
    try:
        output_time = rebuild(config)
        while True:
            for p, stat in get_stats(config.source_path):
                if any(p.match(pattern) for pattern in config.ignore):
                    continue
                if stat.st_mtime > output_time:
                    print(f'Change detected in {p}')
                    output_time = rebuild(config)
                    break
            else:
                time.sleep(0.1)  # make sure we're not a busy loop
    except Exception as e:
        if queue is not None:
            queue.put(e)
        raise


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'source_path', default='source', type=Path, nargs='?',
        help="The directory containing the source the HTML is generated from. "
        "Default: %(default)s")
    parser.add_argument(
        'html_path', default='build/html', type=Path, nargs='?',
        help="The base directory which you wish to server over HTTP. Default: "
        "%(default)s")
    parser.add_argument(
        '-i', '--ignore', action='append', default=['*.swp', '*.bak', '*~', '.*'],
        help="Can be specified multiple times to append to the list of "
        "patterns to ignore.")
    parser.add_argument(
        '--bind', metavar='ADDR', default='0.0.0.0',
        help="The address to listen on. Default: %(default)s")
    parser.add_argument(
        '--port', metavar='PORT', default='8000',
        help="The port to listen on. Default: %(default)s")
    config = parser.parse_args(args)

    queue = mp.Queue()
    builder_proc = mp.Process(target=builder, args=(config, queue), daemon=True)
    server_proc = mp.Process(target=server, args=(config, queue), daemon=True)
    builder_proc.start()
    server_proc.start()
    exc = queue.get()
    server_proc.terminate()
    builder_proc.terminate()
    print(repr(exc))


if __name__ == '__main__':
    sys.exit(main())
