import base64

def textToNumber(text):
  ansii = [ord(c) for c in text]
  print(f"Ansii: {ansii}")
  text_bytecode = text.encode("utf-8")
  hex = text_bytecode.hex()
  print(f"Hex: {hex}")
  baseSixFour = base64.b64encode(text_bytecode)
  print(f"base64: {baseSixFour}")

def numberToText(standart, data):
  if standart == "base-10":
    try:
      dec16 = hex(data)
      text = bytes.fromhex(dec16[2:])
      print(f"Message: {text}")
    except TypeError:
      print("Wrong data type")
  if standart == "hex":
    try:
      text = bytes.fromhex(data[2:])
      print(f"Message: {text}")
    except TypeError:
      print("Wrong data type")
  if standart.lower() == "ansii":
    try:
      text = ''.join(chr(c) for c in data)
      print(f"Message: {text}")
    except TypeError:
      print("Wrong data type")