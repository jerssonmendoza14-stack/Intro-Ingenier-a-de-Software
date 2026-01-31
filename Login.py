# Usuario y contraseña guardados
usuario_correcto = "admin"
contrasena_correcta = "1234"

# Solicitar datos al usuario
usuario = input("Ingrese su usuario: ")
contrasena = input("Ingrese su contraseña: ")

# Validar login
if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("✅ Login exitoso. Bienvenido!")
else:
    print("❌ Usuario o contraseña incorrectos.")