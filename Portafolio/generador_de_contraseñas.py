import random

letras_mayusculas1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","U","V","W","X","Y","Z"]
letras_minusculas1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","u","v","w","x","y","z"]
numeros1 = ["1","2","3","4","5","6","7","8","9","10"]
carateres1 = ["-","+","*"]

letras_mayusculas2 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","U","V","W","X","Y","Z"]
letras_minusculas2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","u","v","w","x","y","z"]
numeros2 = ["1","2","3","4","5","6","7","8","9","10"]
carateres2 = ["-","+","*"]

letras_mayusculas3 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","U","V","W","X","Y","Z"]
letras_minusculas3 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","u","v","w","x","y","z"]
numeros3 = ["1","2","3","4","5","6","7","8","9","10"]
carateres3 = ["-","+","*"]

ramdom_mayus1 = letras_mayusculas1[random.randint(0,23)]
ramdom_minus1 = letras_minusculas1[random.randint(0,23)]
ramdom_num1 = numeros1[random.randint(0,9)]
ramdom_caracteres1 = carateres1[random.randint(0,2)]

ramdom_mayus2 = letras_mayusculas2[random.randint(0,23)]
ramdom_minus2 = letras_minusculas2[random.randint(0,23)]
ramdom_num2 = numeros2[random.randint(0,9)]
ramdom_caracteres2 = carateres2[random.randint(0,2)]

ramdom_mayus3 = letras_mayusculas3[random.randint(0,23)]
ramdom_minus3 = letras_minusculas3[random.randint(0,23)]
ramdom_num3 = numeros3[random.randint(0,9)]
ramdom_caracteres3 = carateres3[random.randint(0,2)]

password = ramdom_mayus1 + ramdom_minus1 + ramdom_num1 + ramdom_caracteres1 + ramdom_mayus2 + ramdom_minus2 + ramdom_num2 + ramdom_caracteres2 + ramdom_mayus3 + ramdom_minus3 + ramdom_num3 + ramdom_caracteres3

print("Tu contraseña:" + password)