import qrcode #biblioteca para gerar QRcode

imagem = qrcode.make("https://github.com/gabrielcardozo29")#função para receber QRcode
imagem.save("qrcode.png")
print("QRcode gerado com sucesso.")