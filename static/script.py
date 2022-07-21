from pyodide.http import pyfetch
'I am using asyncio'

async def get_data():
  print('hi PYSCRIPT is working?')
  print('getting data from python...')
  response = await pyfetch("/get_dog")
  # data = await response.json()
  print(response)

print(await get_data())