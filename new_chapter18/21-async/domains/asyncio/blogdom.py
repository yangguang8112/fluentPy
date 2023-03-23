#!/usr/bin/env python3
import asyncio
import socket
from keyword import kwlist
from typing import Tuple as tuple

MAX_KEYWORD_LEN = 4  # <1>


async def probe(domain: str) -> tuple[str, bool]:  # <2>
    loop = asyncio.get_running_loop()  # <3>
    try:
        await loop.getaddrinfo(domain, None)  # <4>
    except socket.gaierror:
        return (domain, False)
    return (domain, True)


async def main() -> None:  # <5>
    names = (kw for kw in kwlist if len(kw) <= MAX_KEYWORD_LEN)  # <6>
    domains = (f'{name}.dev'.lower() for name in names)  # <7>
    coros = [probe(domain) for domain in domains]  # <8>
    for coro in asyncio.as_completed(coros):  # <9>
        # 这里coro已经是完成的了，为什么还要await，去掉会报错的，可能是解包相关的问题。
        # 原文解释：the await expression will not block but we need it to get the
                    # result from coro. If coro raised an unhandled exception, 
                    # it would be re-raised
                    # here.
        domain, found = await coro  # <10>
        mark = '+' if found else ' '
        print(f'{mark} {domain}')


if __name__ == '__main__':
    asyncio.run(main())  # <11>
