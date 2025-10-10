import asyncio
from typing import List

async def create_task(name:str, delay:int, workload: List[int], find_value:int) -> str:
   print(f"Task {name} started")
   await asyncio.sleep(delay)
   # loop workload, if value found, then return, if not found return -1
   for no in workload:
      if no == find_value:
         return f"Task {name} found {no}"
   return f"Not found in {name}"

async def main():
    tasks = [
        create_task("A", 3, [1, 2, 3], 2),
        create_task("B", 1, [4, 5, 6], 2),
        create_task("C", 5, [7, 8, 9], 2),
    ]

    finished, unfinished = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    for x in finished:
       print("Found in task:", x.result())

asyncio.run(main())