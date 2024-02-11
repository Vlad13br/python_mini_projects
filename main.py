import asyncio
async def main():
    task = asyncio.create_task(other())
    print("A")
    await asyncio.sleep(5)
    print("B")
    value = await task
    print(value)

async def other():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return 10

asyncio.run(main())
