#!/usr/bin/env python
"""Docstring missing."""

__author__ = "Darren Bono"
__email__ = "dbono215@gmail.com"
__version__ = "1.0"

import socket
import subprocess

from ansible.module_utils.basic import *

PORTS = [22, 23, 830]


def host_port(host, port):
    """Docstring missing."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((host, port))
    if result == 0:
        status = "OPEN"
        sock.close()
    else:
        status = "CLOSED"

    return status


def getHostDetails(host):
    """Docstring missing."""
    host_port_status = []
    try:
        for port in PORTS:
            host_port_status.append(host_port(host, port))
    except socket.error:
        host_port_status.append("FAILED")

    return host_port_status


def main():
    """Docstring missing."""
    fields = {
        "host": { "default": "True", "type": "str" },
        "ports": { "default": "True", "type": "str" }
    }

    result = dict(changed=True)
    module = AnsibleModule(argument_spec=fields)
    host_details = getHostDetails(module.params["host"])
    module.params.update({"ports": host_details})
    module.exit_json(**result, meta=module.params)


if __name__ == '__main__':
    main()
