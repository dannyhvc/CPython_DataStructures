# standard imports
from socket import AF_INET, SOCK_STREAM, socket

# styling and typing imports
from typing import Any, List, NoReturn
from colorama import init, Fore, Back, Style

# threading and mp imports]\
from multiprocessing import Process, Lock, synchronize


init()
SERVER = '192.168.1.10'
port = 0
s = socket(AF_INET, SOCK_STREAM)


def pscan(port: int):
    # TODO: test todo
    try:
        s.connect((SERVER, port))
        return True
    except Exception:
        return False


def run_socket_batch(
    num_range: List[int], locker: synchronize.Lock
) -> NoReturn:
    locker.acquire()
    try:
        for i in num_range:
            if pscan(i):
                print(
                    f'\n<Port {i}>: {Fore.LIGHTGREEN_EX}open.\
                            {Style.RESET_ALL}'
                )
            else:
                print(
                    f'\n<Port {i}>: {Fore.RED}closed.\
                            {Style.RESET_ALL}'
                )
    except:
        pass
    finally:
        locker.release()


if __name__ == "__main__":
    data = [x for x in range(1_000 + 1)]
    lock = Lock()

    for chunk in [data[x:x+1] for x in range(1, len(data), 1)]:
        Process(target=run_socket_batch, args=(chunk, lock)).start()
