from openrouter import OpenRouter
client = OpenRouter(
  api_key = input("ingrese su apikey de ai.hackclub.com") ,
  server_url = "https://ai.hackclub.com/proxy/v1")

while 1:
  print("======ChatYipiti=======")
  mod = "qwen/qwen3.8-omni-flash"
  m = input("Inserte su mensaje:(/h para ayuda) ")
  if m == "/h":
    print("Comandos")
    print("/h : este menu")
    print("/e : salir")
    continue
  elif m == "/e":
    quit() #no quiero usar break
  elif m == "/m":
    print("Escoja un modelo de la siguiente lista")
    print()
  response = client.chat.send(
    model= mod,
    messages=[
        {"role": "user", "content": m}
    ],
    stream=False,
  )
  print(response.choices[0].message.content)