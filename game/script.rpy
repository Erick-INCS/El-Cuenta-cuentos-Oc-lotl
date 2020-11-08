# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image alj surprise = im.FactorScale("alejandro/sorpresa.png", 0.2, xpos=380)
image bg altar = im.FactorScale("bg altarfull.jpg", 1)

# $ renpy.music.set_volume(0.1, delay=0, channel='music') #0.5 is set as default


define al = Character("Alejandro", color='#f0ad4e')#Nieto
define ab = Character("Marina", color='#d9534f')#Abuela
define n = Character("Ocelotl")#Narrador



label start:

    scene bg altar

    play music "audio/ambiente.mp3"
    $ renpy.music.set_volume(0.1, channel='music')


    show alj surprise

    # menu:
    #     "It's a videogame.":
    #         jump game

    #     "It's an interactive book.":
    #         jump book

    # label game:

    #     ab "It's a kind of videogame you can play on your computer or a console."

    #     jump marry

    # label book:

    #     al "It's like an interactive book that you can read on a computer or a console."

    #     jump marry

    # label marry:

    #     "And so, we become a visual novel creating duo."


    n "Marina y su nieto Alejandro como cada año se disponían a colocar la ofrenda para el día de muertos,al ver que su pequeño nieto se distraía y terminaba jugando con las flores le dijo:"


    ab "Más respeto por los muertos muchacho!"

    n 'Alejandro sin comprender,pregunto con una voz dudosa'

    play sound "audio/al1.mp3"
    al "¿por qué es necesario esparcir flores en el suelo? y ¿dónde están los muertos abuela?"

    n "Marina dejo las flores y sentó a su nieto en su regazo:"

    ab "escucha Alejandro, hace mucho tiempo mucho más del que yo tengo en esta vida"

    n "Alejandro exclamo"

    play sound "audio/al2.mp3"
    al "Eso es mucho tiempo abuela"

    n "La abuela sólo sonrió y prosiguió"

    ab "En esta vida las cosas son distintas al más allá, a algunos les ira bien aquí, pero talvez después de la vida no sea así. Los mexicas creían que la vida después de la muerte estaba en un lugar llamado"

    ab "Mictlán, que es el lugar donde van los muertos y que era gobernado por los dioses Mictlantecuhtli y Mictecacihuatl"

    ab "Pero el llegar ahí no era cosa fácil"

    n "Facil cómo, ¿te puedes perder?"

    ab "No hijo mío, es más que eso -respondió la abuela con voz dulce y continuo:- Existe solo un camino para llegar al Mictlán, este consta de nueve niveles, llenos de miedo y peligro, te voy a explicar por qué"

    ab "El viaje dura alrededor de 4 años, al finalizar serás recibido por Mictlantecuhtli y Mictlancihuatl, las deidades del inframundo, quienes le anunciaran el final del camino a las almas"

    ab "El primer nivel,es conocido como el Lugar donde los Xoloitzcuintles habitan y esperan a las almas, y son ellos quienes ayudan a cruzar un caudaloso rio que deberán cruzar con su ayuda, son perro de color pardusco y con poco pelaje, es por eso que en esta vida tienes que ser una buena persona con los perros. Exclamo la abuela a su nieto"

    play sound "audio/al3.mp3"
    al "-Si abuela, eso siempre me lo has dicho -respondió Alejandro con voz firme."

    ab 'La abuela continua- "el lugar donde los cerros de juntan", es el segundo nivel, aquí existen dos grandes cerros que se abren y se cierran sin previo aviso, aqui es donde las almas deberán esperar el momento oportuno para cruzar, la paciencia es una virtud Alejandro –le dijo la abuela mirando a su nieto'

    ab 'el siguiente nivel es "IZTEPETL", aquí los muertos tendrán que subir una gran cerrocubierto de filosísimos pedernales,que desgarrarán su piel pero tendrán que continuar para leegar al final del camino.'

    n "Alejandro veía con asombro como su abuela le contaba aquel cuento"

    ab 'el cuarto nivel, el lugar del viento de obsidiana es un sitio desolado de hielo y piedra. Se trata de una sierra con aristas cortantes compuesta de ocho collados en los que siempre caía nieve'

    ab 'En el quinto nivel"El lugar donde la gente vuela y se voltea como banderas". Se dice que este lugar se ubicaba al pie de una colina del Itzehecayan, donde los muertos perdían la gravedad y estaban a merced de los vientos, que los arrastraba hasta que finalmente eran liberados para pasar al nivel siguiente.'

    play sound "audio/al4.mp3"
    al "Alejandro interrumpe, -¡espera abuela!"


    play sound "audio/al5.mp3"
    al "¿qué pasa si mueren en una de esas pruebas?"

    ab "Marina con una sonrisa en el rostro respondió, -las almas no pueden morir en el más allá, sentirán ese sufrimiento como si estuvieran con vida en esta vida terrenal, pero no morirán."

    n "Alejandro proceso la respuesta y la abuela continuo con el cuento"

    ab 'El sexto nivel"El lugar donde la gente es flechada".En el, se encuentra un extenso sendero donde son lanzadas flechas de todos lados. Estas son flechas lanzadas durante las Guerras'

    ab 'Una vez salido de ahí, las almas se dirigen a "TEOCOYOHUEHUALOYAN" es donde...'

    play sound "audio/al6.mp3"
    al "¡es muy gracioso ese nombre, abuela! interrumpe Alejandro sin pensarlo dos veces."

    ab "Bueno esos dices por que no sabes que aquí es donde los jaguares les abren el pecho a las almas y se comen su corazón"

    n "Alejandro borro su sonrisa y continuóescuchando a su abuela."

    ab "En el penúltimo nivel IZMICTLAN APOCHCALOLCA, que es la laguna de aguas negras, es donde los muertos dejan su cuerpo casi por completo y comienzan a liberar su alma."

    ab "Finalmente, las almas llegan a CHICUNAMICTLAN, en este lugar los muertos deberán atravesar las nueve aguas de Chiconauhhapany, una vez superado este último obstáculo, su alma sería liberada completamente de los padecimientos del cuerpo"

    ab "por Mictlantecuhtli yMictecacihuatl, esencia de la muerte"

    n "Alejandro reconocio esos nombres diciendo"

    play sound "audio/al7.mp3"
    al "Son las deidades que mencionaste al principio, ¿no es verdad abuela?"

    n "con voz amable Marina respondió"
    ab "creía que no me habias puesto atención, pero es verdad, aunque no te mencione que los difuntos deberán de ser enviados conalgunos amuletos y pertenencias para facilitar su camino, entre ello agua, mantas, armas y otras pertenencias"

    n "Comprendiendo eso, Alejandro respondió"
    ab "Claro, no sería justo llegar ante el mismísimo señor de la muerte con las manos vacías."

    n "La abuela con una sonrisa en el rostro dijo:"
    ab "bueno, ahora sabes porque hay que tenerles respeto a los muertos, ahora ayúdame a terminar de poner la ofrenda"


    return
