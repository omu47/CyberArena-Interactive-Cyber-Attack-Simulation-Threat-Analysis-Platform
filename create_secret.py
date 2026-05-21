from stegano import lsb

secret = lsb.hide(
    "test.png",
    "CyberArena Secret Message"
)

secret.save("hidden_image.png")

print("Hidden image created.")