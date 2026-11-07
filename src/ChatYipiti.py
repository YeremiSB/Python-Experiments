#lol yipiti
from openrouter import OpenRouter
client = OpenRouter(
  api_key = input("ingrese su apikey de ai.hackclub.com") ,
  server_url = "https://ai.hackclub.com/proxy/v1")
mod = "qwen/qwen3.8-omni-flas[]h"
history = []
while 1:
  print("======ChatYipiti=======")
  msg = input("Inserte su mensaje:(/h para ayuda) ")
  if msg == "/h":
    print("Comandos")
    print("/h : este menu")
    print("/e : salir")
    continue
  elif msg == "/e":
    quit() #no quiero usar break
  elif msg == "/m":
    print("Escoja un modelo de la siguiente lista")
    print("1. ChatGPT")
    print("2. Gemini")
    print("3. Qwen")
    try:
      opcion = int(input("ingrese indice de opcion (numero): "))
      if opcion == 1:
        mod = "openai/gpt-5.6-sol"
        continue
      elif opcion == 2:
        mod = "google/gemini-3.5-flash"
        continue
      elif opcion == 3:
        mod = "qwen/qwen3.8-omni-flash"
        continue
      else:
        print("modelo invalido")
        continue
    except ValueError:
      print("modelo invalido")
      continue
  history.append(("user", msg))
  response = client.chat.send(
    model= mod,
    messages=[
        {"role": "user", "content": msg}
    ],
    stream=False,
  )
  history.append(("assistant", response.choices[0].message.content))
  print(response.choices[0].message.content)