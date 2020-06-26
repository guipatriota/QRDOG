import pyqrcode

dog_name = input('Qual o nome do seu cachorro?')
user_name = input('Qual o nome de usuário do seu pet no instagram?')
dog = ''.join(a for a in dog_name.title().replace(' ', '_'))
user = ''.join(a for a in user_name.lower().replace('@', ''))
print ('@'+user)
url = pyqrcode.create ('https://www.instagram.com/{}'.format(user), error = 'Q', version = 5, mode = 'binary')
url.svg ('QRDOG_{}.svg'.format(dog), scale = 8, module_color = "black", background = "white")
url.eps ('QRDOG_{}.eps'.format(dog), scale = 2)
url.png ('QRDOG_{}.png'.format(dog), scale = 6, module_color = [0, 0, 0, 255], background = [0xFF, 0xFF, 0xFF])
url.show ()
#print (url.terminal (quiet_zone = 1))