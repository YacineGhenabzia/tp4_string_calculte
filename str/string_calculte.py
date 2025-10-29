def stringcalcult(number:str)->int:

    if not number or number.strip() == "":
     return 0

    parts = number.split(",")

    total = 0
    for part in parts:
     part = part.strip()
     if part:
      total += int(part)

     return total
