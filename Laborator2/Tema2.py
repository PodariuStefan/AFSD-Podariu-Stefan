a = """Eu nu strivesc corola de minuni a lumii
şi nu ucid
cu mintea tainele, ce le-ntâlnesc
în calea mea
în flori, în ochi, pe buze ori morminte.
Lumina altora
sugrumă vraja nepătrunsului ascuns
în adâncimi de întuneric,
dar eu,
eu cu lumina mea sporesc a lumii taină
şi-ntocmai cum cu razele ei albe luna
nu micşorează, ci tremurătoare
măreşte şi mai tare taina nopţii,
aşa îmbogăţesc şi eu întunecata zare
cu largi fiori de sfânt mister
şi tot ce-i neînţeles
se schimbă-n neînţelesuri şi mai mari
sub ochii mei-
căci eu iubesc
şi flori şi ochi şi buze şi morminte."""

a1= a[:len(a)//2]
a2= a[len(a)//2:]

def rezolvare_problemă (a, b):
    b1 = a.upper().strip()
    b2 = b[::-1].capitalize().replace("."," ").replace(",", " ").replace("!", " ").replace("?", " ")
    print(b1 + b2)

rezolvare_problemă (a1, a2)




