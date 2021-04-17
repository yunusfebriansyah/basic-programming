import random
# program tebak angka

while(True) :  
  
  level = input("\nPilih level [mudah/medium/sulit] : ")
  while( level != "mudah" and level != "medium" and level != "sulit" ) :
    level = input("Maaf level anda tidak sesuai!\nPilih level [mudah/medium/sulit] : ")
  
  if level == "mudah" :
    kesempatan = 3
    bilRandom = random.randint(1,10)
  elif level == "medium" :
    kesempatan = 4
    bilRandom = random.randint(1,20)
  elif level == "sulit" :
    kesempatan = 5
    bilRandom = random.randint(1,100)
  
  print("Anda memilih level", level, "dengan kesempatan", kesempatan, "kali.")


  while( kesempatan >= 0 ) :
    if kesempatan == 0 :
      print("Yah gagal menebak angkanya :(")
      kesempatan -= 1
    else :
      print("\nKesempatan :", kesempatan)
      tebakan = int(input("Tebak bilangan : "))
      if tebakan == bilRandom :
        print("Widiih bener dong!!")
        break
      elif bilRandom > tebakan :
        print("Angkanya diatas", tebakan)
        kesempatan -= 1
      elif bilRandom < tebakan :
        print("Angkanya dibawah", tebakan)
        kesempatan -= 1
      



  lanjut = input("\nMain lagi?? [y/n] : ")
  while( lanjut != "y" and lanjut != "n" ) :
    lanjut = input("Maaf inputan anda tidak sesuai!\nMain lagi?? [y/n] : ")
  
  if lanjut == "n" :
    print("Terimakasih sudah bermain game Tebak Angka.\n")
    break
  elif lanjut == "y" :
    print("Silahkan main game Tebak Angka lagi!!")
