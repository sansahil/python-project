email = input('enter email')
password = input('enter password')

if email == 'sanatana.sahu@ gmail.com' and password == '12345':
  print('welcome')
elif email == 'sanatana.sahu@ gmail.com' and password != '12345':
  # tell the user
  print('incorrect password')
  password = input('enter password again')
  if password == '12345':
    print('wlecome ,finally')
  else:
    print('tumse na ho paayega')
else:
  print('not correct')