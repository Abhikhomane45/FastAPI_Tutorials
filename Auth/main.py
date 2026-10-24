from fastapi import FastAPI
import asyncio

app=FastAPI()

#------------------Async Programming---------------

@app.get("/home")
async def home():
    await asyncio.sleep(3)
    return "hello Abhijeet Lets wait for 3 sec for other task to complete using await"

