import asyncio

async def fetch_data(url: str):
   print("Fetching data...")
   await asyncio.sleep(1)
   return {"data": f" Result from {url}: some data"}

async def main():
   # Gather multiple coroutines correctly by passing them as separate arguments
   results = await asyncio.gather(
       fetch_data("google.com"),
       fetch_data("bing.com"),
       fetch_data("yahoo.com"),
   )

   print(results)

asyncio.run(main())