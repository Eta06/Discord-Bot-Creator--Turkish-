import time
import os
import random
while True:
    print("Bu adda başka bir dosya varsa o dosya silinecektir!")
    ad = input("Botun adını girin: ")
    with open(ad + '.py', 'w') as addd:
        addd.write("import discord" + "\n")
        addd.write("import random" + "\n")
        addd.write("from discord.ext import commands, tasks" + "\n")
        addd.write("import os" + "\n")
        addd.write("from discord import Member" + "\n")
        addd.write("from discord.ext.commands import has_permissions, MissingPermissions" + "\n")
        addd.write("import requests" + "\n")
        addd.write("import asyncio" + "\n")
    break
while True:
    prefix = input("Botun prefixini seçin. Örnek: ! , . , / bunlardan birini seçebilirisniz: ")
    if prefix == ".":
        with open (ad + '.py', 'a') as prefixx:
            prefixx.write("\n")
            prefixx.write("client = commands.Bot(command_prefix = '.')" + "\n")
            prefixx.write("bot = commands.Bot(command_prefix = '.')" + "\n")
            prefixx.write("\n")
            prefixx.write("@client.event" + "\n")
            prefixx.write("async def on_ready():" + "\n")
            prefixx.write("    print("Bot Çalışıyor! " + str(client.user))" + "\n")
            prefixx.write("\n")
        break
    elif prefix == "!":
        with open (ad + '.py', 'a') as prefixx:
            prefixx.write("\n")
            prefixx.write("client = commands.Bot(command_prefix = '!')" + "\n")
            prefixx.write("bot = commands.Bot (Bot_prefix = '!')" + "\n")
            prefixx.write("\n")
            prefixx.write("@client.event" + "\n")
            prefixx.write("async def on_ready():" + "\n")
            prefixx.write("    print("Bot Çalışıyor! " + str(client.user))" + "\n")
            prefixx.write("\n")
        break
    elif prefix == "/":
        with open (ad + '.py', 'a') as prefixx:
            prefixx.write("\n")
            prefixx.write("client = commands.Bot(command_prefix = '/')" + "\n")
            prefixx.write("bot = commands.Bot (Bot_prefix = '/')" + "\n")
            prefixx.write("\n")
            prefixx.write("@client.event" + "\n")
            prefixx.write("async def on_ready():" + "\n")
            prefixx.write("    print("Bot Çalışıyor! " + str(client.user))" + "\n")
            prefixx.write("\n")
        break
    else:
        print("Lütfen Seçiminizi Düzgün Girin!")
komutsayisi = 1
while True:
    komutsayisi = int(input("Kaç tane komut eklemek istersiniz?"))
    if komutsayisi >= 1:
        for i in range(1,komutsayisi+1):
            while True:
                komut = input("Komutu başında '{}' olmadan girin: ".format(prefix))
                cevap = input("Bot {}{} komutu karşsında ne cevap verecek: ".format(prefix,komut))
                if komut == "":
                    print("Komut kısmı boş olamaz!")
                elif cevap == "":
                    print("Cevap kısmı boş olamaz")
                else:
                    with open(ad + '.py', 'a') as komutlarr:
                        komutlarr.write("\n")
                        komutlarr.write("@client.command()")
                        komutlarr.write("\n")
                        komutlarr.write("async def {}(ctx):".format(komut))
                        komutlarr.write("\n")
                        komutlarr.write("    await ctx.send(f'{}')".format(cevap))
                        komutlarr.write("\n")
                    break
        break
    else:
        print("Lütfen düzgün bir değer girin! ")
while True:
    botid = input("Lütfen discord botunuzun tokenini girin: ")
    if botid == "":
        print("Lütfen düzgün bir token girin!")
    else:
        with open(ad + '.py', 'a') as tokenn:
            tokenn.write("\n")
            tokenn.write('client.run("{}")'.format(botid))
        break
dosyaadi = ad + '.py'
print("Botunuz {} adı ile oluşturuldu!".format(dosyaadi))

        
