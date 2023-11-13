from varasto import Varasto

def tulosta_varastot(mehu, olut):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehu}")
    print(f"Olutvarasto: {olut}")

def tulosta_olut_getterit(olut):
    print("Olut getterit:")
    print(f"saldo = {olut.saldo}")
    print(f"tilavuus = {olut.tilavuus}")
    print(f"paljonko_mahtuu = {olut.paljonko_mahtuu()}")

def tulosta_mehu_setterit(mehu):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehu.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehu}")
    print("Otetaan 3.14")
    mehu.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehu}")

def tulosta_virhetilanteita():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    tulosta_varastot(mehua, olutta)
    tulosta_olut_getterit(olutta)
    tulosta_mehu_setterit(mehua)
    tulosta_virhetilanteita()

if __name__ == "__main__":
    main()
