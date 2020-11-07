# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image alj surprise = im.FactorScale("alejandro/sorpresa.png", 0.2, xpos=380)
image bg altar = im.FactorScale("bg altarfull.jpg", 1)

define al = Character("Alejandro")#Nieto
define ab = Character("Marina")#Abuela
define n = Character("Ocelotl")#Narrador


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg altar

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show alj surprise

    # These display lines of dialogue.

    n "Marina y su nieto Alejandro como cada año se disponían a colocar la ofrenda para el día de muertos,al ver que su pequeño nieto se distraía y terminaba jugando con las flores le dijo: "
       
    ab "Más respeto por los muertos muchacho!"

    n 'Alejandro sin comprender,pregunto con una voz dudosa'
    
    al '"¿por qué es necesario esparcir flores en el suelo? y ¿dónde están los muertos abuela?"'

    n "Marina dejo las flores y sentó a su nieto en su regazo:" 
           
    ab "escucha Alejandro, hace mucho tiempo mucho más del que yo tengo en esta vida”

    n "Alejandro exclamo"
    
    al "Eso es mucho tiempo abuela"

    n "La abuela sólo sonrió y prosiguió"
    
    ab "En esta vida las cosas son distintas al más allá, a algunos les ira bien aquí, pero talvez después de la vida no sea así. Los mexicas creían que la vida después de la muerte estaba en un lugar llamado" 
  
    ab "Mictlán, que es el lugar donde van los muertos y que era gobernado por los dioses Mictlantecuhtli y Mictecacihuatl”

   ab "Pero el llegar ahí no era cosa fácil”

    n "Facil cómo, ¿te puedes perder? "
    
    ab "No hijo mío, es más que eso -respondió la abuela con voz dulce y continuo:- Existe solo un camino para llegar al Mictlán, este consta de nueve niveles, llenos de miedo y peligro, te voy a explicar por qué"
    
    ab "El viaje dura alrededor de 4 años, al finalizar serás recibido por Mictlantecuhtli y Mictlancihuatl, las deidades del inframundo, quienes le anunciaran el final del camino a las almas"

    ab "El primer nivel,es conocido como el Lugar donde los Xoloitzcuintles habitan y esperan a las almas, y son ellos quienes ayudan a cruzar un caudaloso rio que deberán cruzar con su ayuda, son perro de color pardusco y con poco pelaje, es por eso que en esta vida tienes que ser una buena persona con los perros. Exclamo la abuela a su nieto"

    al "-Si abuela, eso siempre me lo has dicho -respondió Alejandro con voz firme." 

    ab"La abuela continua- “el lugar donde los cerros de juntan”, es el segundo nivel, aquí existen dos grandes cerros que se abren y se cierran sin previo aviso, aqui es donde las almas deberán esperar el momento oportuno para cruzar, la paciencia es una virtud Alejandro –le dijo la abuela mirando a su nieto" 

    ab "el siguiente nivel es “IZTEPETL”, aquí los muertos tendrán que subir una gran cerrocubierto de filosísimos pedernales,que desgarrarán su piel pero tendrán que continuar para leegar al final del camino."

    al "Alejandro veía con asombro como su abuela le contaba aquel cuento"

    ab "el cuarto nivel, el lugar del viento de obsidiana” es un sitio desolado de hielo y piedra. Se trata de una sierra con aristas cortantes compuesta de ocho collados en los que siempre caía nieve"

    ab "En el quinto nivel,“El lugar donde la gente vuela y se voltea como banderas”. Se dice que este lugar se ubicaba al pie de una colina del Itzehecayan, donde los muertos perdían la gravedad y estaban a merced de los vientos, que los arrastraba hasta que finalmente eran liberados para pasar al nivel siguiente."

    al "Alejandro interrumpe, -¡espera abuela!"

    al "¿qué pasa si mueren en una de esas pruebas?"
 
    ab "Marina con una sonrisa en el rostro respondió, -las almas no pueden morir en el más allá, sentirán ese sufrimiento como si estuvieran con vida en esta vida terrenal, pero no morirán."

    n "Alejandro proceso la respuesta y la abuela continuo con el cuento"

    ab "El sexto nivel,“El lugar donde la gente es flechada”.En el, se encuentra un extenso sendero donde son lanzadas flechas de todos lados. Estas son flechas lanzadas durante las Guerras"

    ab "Una vez salido de ahí, las almas se dirigen a “TEOCOYOHUEHUALOYAN” es donde..."

    al "¡es muy gracioso ese nombre, abuela! interrumpe Alejandro sin pensarlo dos veces."

    ab "Bueno esos dices por que no sabes que aquí es donde los jaguares les abren el pecho a las almas y se comen su corazón"

    n "Alejandro borro su sonrisa y continuóescuchando a su abuela."

    ab "En el penúltimo nivel IZMICTLAN APOCHCALOLCA, que es la laguna de aguas negras, es donde los muertos dejan su cuerpo casi por completo y comienzan a liberar su alma."

    ab "Finalmente, las almas llegan a CHICUNAMICTLAN, en este lugar los muertos deberán atravesar las nueve aguas de Chiconauhhapany, una vez superado este último obstáculo, su alma sería liberada completamente de los padecimientos del cuerpo"

    ab "por Mictlantecuhtli yMictecacihuatl, esencia de la muerte"

    n "Alejandro reconocio esos nombres diciendo," 
    al "-Son las deidades que mencionaste al principio, ¿no es verdad abuela? -"

    n "con voz amable Marina respondió,"
    ab "creía que no me habias puesto atención, pero es verdad, aunque no te mencione que los difuntos deberán de ser enviados conalgunos amuletos y pertenencias para facilitar su camino, entre ello agua, mantas, armas y otras pertenencias"

    n "Comprendiendo eso, Alejandro respondió, "
    ab "claro, no sería justo llegar ante el mismísimo señor de la muerte con las manos vacías. –"

    n "La abuela con una sonrisa en el rostro dijo:"
    ab "bueno, ahora sabes porque hay que tenerles respeto a los muertos, ahora ayúdame a terminar de poner la ofrenda"


    return
