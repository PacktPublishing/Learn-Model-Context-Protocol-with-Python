import asyncio

async def fetch_data(url: str):
   print("Fetching data...")
   await asyncio.sleep(1)
   return {"data": f" Result from {url}: some data"}

async def main():
   done, _ = await asyncio.wait([
       fetch_data("google.com"),
       fetch_data("bing.com"),
       fetch_data("yahoo.com")
   ])

   for task in done:
       print(task.result())

asyncio.run(main())