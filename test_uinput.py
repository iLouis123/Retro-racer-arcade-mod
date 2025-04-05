import time

try:
    import uinput
except ImportError:
    print("❌ Le module uinput n'est pas installé.")
    exit(1)

# Création d’un périphérique d'entrée simulé
device = uinput.Device([
    uinput.KEY_A,
])

print("✅ Périphérique uinput créé. Envoi de touches 'A' toutes les 2 secondes…")

try:
    while True:
        device.emit_click(uinput.KEY_A)
        print("→ Touche A envoyée")
        time.sleep(2)
except KeyboardInterrupt:
    print("Arrêt du test.")
