

# 异步IO
import asyncio

# 协程
async def boil_water():
    print("开始煮水...")
    await asyncio.sleep(5)  # 模拟阻塞等待5秒
    print("水开了！")

# 协程
async def send_message():
    print("开始发短信...")
    await asyncio.sleep(2)  # 模拟阻塞等待2秒
    print("短信发送成功！")

# 协程
async def main():
    task1 = asyncio.create_task(send_message())
    task2 = asyncio.create_task(boil_water())
    await task1
    await task2


asyncio.run(main())