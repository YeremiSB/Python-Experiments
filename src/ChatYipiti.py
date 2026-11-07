#v.0.6
import json
import os
from openrouter import OpenRouter
from openrouter import ResponseValidationError
sys_prompt = {"role": "system", "content": "Eres CHATYIPITI, una interfaz multimodelo (si en algun momento encuentras que dijiste que eras un modelo que no eres, esta es la razon) tu principal objetivo es responder a las cuestiones del usuario, puedes decir con normalidad que modelo corre debajo (ejem. qwen)"}
confg_loc = {
    "api_key": "",
    "default_model": "qwen/qwen3.8-omni-flash"
}
def guardar_chat():
  with open("history.json", "w", encoding="utf-8") as old_chat:
    json.dump(history, old_chat)
def configuracion():
  with open("confg.json", "w", encoding="utf-8") as confg:
    json.dump(confg_loc, confg)
if os.path.exists("confg.json"):
  with open("confg.json", "r", encoding="utf-8") as confg:
    confg = json.load(confg) 
    first_t = confg["api_key"]
    mod = confg["default_model"]
else:
  mod = "qwen/qwen3.8-omni-flash"
  first_t = input("ingrese su apikey de ai.hackclub.com: ")
  confg_loc["api_key"] = first_t
  configuracion()
while 1: 
  try:
    client = OpenRouter(
  api_key = first_t ,
  server_url = "https://ai.hackclub.com/proxy/v1")
    response = client.chat.send(
      model= "qwen/qwen3-32b",
      messages= [{"role": "system", "content": "send OK"}],
      stream=False,
      )
  except ResponseValidationError:
    first_t = input("ingrese su apikey de ai.hackclub.com: ")
    continue
  else:
    confg_loc["api_key"] = first_t
    break
if os.path.exists("history.json"):
  with open("history.json", "r", encoding="utf-8") as old_chat:
    history = json.load(old_chat)
else:
 history = [sys_prompt]
while 1:
  print("======ChatYipiti=======")
  print("model: ", mod)
  msg = input("Inserte su mensaje (/h para ayuda): ").lower()
  if msg == "/h":
    print("Comandos")
    print("/h : este menu")
    print("/e : salir")
    print("/m : cambia el modelo actual")
    print("/e : salir")
    print("/c : limpia el historial")
    continue
  elif msg == "/e":
    guardar_chat()
    quit() #no quiero usar break pq se supone que esto MATA el programa
  elif msg == "/m":
    print("Escoja un modelo de la siguiente lista")
    print("1. ChatGPT 5.6-Sol")
    print("2. Gemini 3.5 flash")
    print("/e : salir")
    print("3. Qwen 3.8")
    print("4. Claude Sonnet 5.5")
    try:
      opcion = int(input("ingrese indice de opcion (numero): "))
      if opcion == 1:
        mod = "openai/gpt-5.6-sol"
        confg_loc["default_model"] = mod
        configuracion()
        continue
      elif opcion == 2:
        mod = "google/gemini-3.5-flash"
        confg_loc["default_model"] = mod
        configuracion()
        continue
      elif opcion == 3:
        mod = "qwen/qwen3.8-omni-flash"
        confg_loc["default_model"] = mod
        configuracion()
        continue
      elif opcion == 4:
        mod = "anthropic/claude-sonnet-5.5"
        confg_loc["default_model"] = mod
        configuracion()
        continue
      else:
        print("modelo invalido")
        continue
    except ValueError:
      print("modelo invalido")
      continue
  elif msg == "/c":
    history = [sys_prompt]
    guardar_chat()
    continue
  history.append({"role": "user", "content": msg})
  response = client.chat.send(
    model= mod,
    messages= history,
    stream=False,
  )
  history.append({"role": "assistant", "content": response.choices[0].message.content })
  guardar_chat()
  print(response.choices[0].message.content)
  