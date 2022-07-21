from pyodide.http import pyfetch
print('hi PYSCRIPT is working?')
response = await pyfetch("/background_process_test")
data = await response.json()
print(data)