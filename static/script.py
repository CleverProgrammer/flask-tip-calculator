from pyodide.http import pyfetch
import asyncio

async def get_data():
  print('hi PYSCRIPT is working?')
  print('getting data from python...')
  # response = await pyfetch("/get_dog")
  response = await pyfetch("https://dog.ceo/api/breeds/image/random")
  data = await response.json()
  console.log(type(data))
  print(type(data))
  pyscript.write('dog', f"<img src='{data['message']}'/>")

  # data = await response.json()
  print(data)

await get_data()