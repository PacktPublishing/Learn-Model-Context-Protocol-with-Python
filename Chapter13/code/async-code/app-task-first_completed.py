# python
import asyncio
from typing import List, Optional

async def search_task(name: str, delay: int, workload: List[int], find_value: int, stop: asyncio.Event) -> Optional[str]:
    try:
        print(f"Task {name} started")
        await asyncio.sleep(delay)             # simulate I/O
        if stop.is_set():
            return None
        for no in workload:
            await asyncio.sleep(0)            # yield to allow cancellation
            if no == find_value:
                stop.set()
                return name
        return None
    except asyncio.CancelledError:
        print(f"Task {name} cancelled")
        raise

async def main():
    stop = asyncio.Event()
    tasks = [
        asyncio.create_task(search_task("A", 3, [1,2,3], 2, stop)),
        asyncio.create_task(search_task("B", 1, [4,5,6], 2, stop)),
        asyncio.create_task(search_task("C", 5, [7,8,9], 2, stop)),
    ]

    try:
        for finished in asyncio.as_completed(tasks):
            res = await finished
            if res:
                print("Found in", res)
                break
    finally:
        for t in tasks:
            if not t.done():
                t.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)

asyncio.run(main())