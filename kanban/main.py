import os
import signal
from db import init_db
from mcp_tools import mcp

if __name__ == "__main__":
    try:
        with open('/tmp/mcp_pid') as f:
            pid = f.read()
            if pid:
                print(f'Killing old server pid: {pid}')
                os.kill(int(pid), signal.SIGTERM)
    except FileNotFoundError:
        print('No old mcp_pid found, starting new server.')

    with open('/tmp/mcp_pid', 'w') as f:
        pid = os.getpid()
        f.write(str(pid))
        print(f'Running mcp server as pid: {pid}')

    init_db()
    mcp.run(transport='stdio')
