from pyodide.http import pyfetch
import asyncio

async def get_data():
  print('hi PYSCRIPT is working?')
  response = await pyfetch("/background_process_test")
  # data = await response.json()
  print(response)

print(await get_data())