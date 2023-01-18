from Forum.forum import Forum

with Forum() as bot:
    bot.land_page()
    bot.wpisz_imie('Piotr Sygut')
    bot.wpisz_email('email@gmail.com')
    bot.wpisz_temat('temat')
    bot.wpisz_tekst('tekst')


