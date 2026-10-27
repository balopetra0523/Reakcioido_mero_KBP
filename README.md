Reakcióidő-mérő 
Készítette:Kajári-Báló Petra

A program egy Python nyelven készült reakcióidő-mérő alkalmazás, 
amely garfikus felülettel rendelkezik.  A programot a main.py fájl futtatásával tudjuk elindítani.
A felhasználó az Inditás gombbal kezdi a programot,
majd utána 2-5 másodpercet vár eközben kiírja a Várj jelzésre... feliratot,
utána megjelenik a Most kattinthatsz! felirat. 
A felhasználónak ezután a Kattintsd ide! gombra kell nyomnia,
amilyen gyorsan tud, ez által a program megméri, hogy a jelzés és a kattintás között  mennyi idő telt el,
majd a végeredményt ezredmásodpercben jeleníti meg. 
A mérés időpontja is látható a végeredmény alatt. 
Ha szeretnénk újból mérni akkor arra is van lehetőség, 
ha megnyomjuk ismét az indítás gombot.


Felhasznált modulok:
tkinter és ttk:
A program ablakot,címkéket és gombokat használ. 
A gombokhoz eseménykezelő függvények kapcsolódnak. 

random:
A random.randint(2,5) függvény segítségével, 
a program véletlenszerűen várakozási időt választ.

time:
Három függvényt használ a modulból, a time.perf_counter() - a reakcióidő pontos mérése,
a time.localtime() - a mérés helyi időpontjának lekérése, és a time.time() - a mérés időbélyegének lekérése.

sajat_KBP:
A saját készítésű modul a reakcioidő átváltásához szükséges függvényt és a mérési eredményt tároló osztályt tartalmazza.

Saját függvény: 
 KBP_masodpercbol_ms(masodperc) - A függvény a másodpercben megadott időt ezredmásodpercre váltja át.

Saját osztály: KBP_ReakcioMeres - Az osztály a legutóbbi megadott időt tárolja a legutobbi_eredmeny attribútumban.

