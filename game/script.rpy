# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image alj surprise = im.FactorScale("alejandro/sorpresa.png", 0.2, xpos=380)
image bg altar = im.FactorScale("bg altarfull.jpg", 1)

define al = Character("Alejandro")
define ab = Character("Océlotl")#Abuela
define n = Character("Narrador")


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

    n "Abuela (Océlotl) y su nieto (Alejandro) como cada año se disponían a colocar la ofrenda para el día de muertos."
    n "La abuela al ver que su pequeño nieto se distraía y terminaba jugando con las flores exclamó:"
    
    ab "Más respeto por los muertos muchacho!"
    n 'Alejandro sin comprender, le pregunta la abuela con voz dudosa'
    al '"¿por qué es necesario esparcir unas simples flores en el suelo? Ademas  ¿dónde están los muertos abuela?"'

    n 'Océlotl deja las flores y sienta a su nieto en su regazo'
    
    ab "escucha Alejandro, hace mucho tiempo, mucho más del que yo tengo en esta vida" 

    n "Alejandro exclama"
    
    al "Eso es mucho tiempo abuela"

    n "Océlotl sonríe, le saca la lengua prosigue"
    
    ab "En esta vida las cosas son distintas al más allá, a algunos les ira bien aquí, pero talvez después de la vida no sea así."
    ab 'Los antiguos mexicas creían que la vida después de la muerte estaba en el "Mictlán", que es el lugar de los muertos. Pero llegar ahí no era cosa fácil, además de que existían otros ríenos dependiendo de cómo morías'
    
    n 'Le entrega una hoja con la historia, Alejandro la y lee los lugares con dificultad' 
    
    ab "depende de muriese te mandaban a reinos extrenos, si te ahogabas ibas al tlaloc,  si morias luchando al omeyocán, los niños moridos al chichihuanahuco y los que morian de muerte natural al mictlán donde los esperaban Mictlantecuhtli y micccccc mictla..." 
    al "YO NO PUEDO PRONUNCIAR ESTO ABUELA" 

    # Abuela – se rie y responde- "Mictlancihuatl" 

    # Alejandro-"¿Y si el mictlan era peligro pa’ que iban ?" 

    # Abuela - "No hijo mío,el mictlan no era peligroso pero es camino que consta de nueve niveles, llenos de miedo y peligro, continua leyendo por favor".- 

    # Alejandro-se imagina con su abuela en el vieje al mictlan -"El viaje dura alrededor de 4 años, primero llegas al Lugar de los perros, las almas se encuentran en un caudaloso rio que deberán cruzar con ayuda de un xolo xolo que ???"- 

    # Abuela- "xoloitzcuintle el perro que esta calvo ? por eso que en esta vida tienes que ser una buena persona con los perros". Exclamo la abuela a su nieto.  

    # Alejandro – " esta bien no le vuelvo a pegar paletas al Fix" 

    # La abuela continua- "despues vamos al lugar donde los cerros de juntan", es el segundo nivel, aquí existen dos grandes cerros que se abren y se juntan sin previo aviso, es donde las almas deberán esperar el momento oportuno para cruzar, la paciencia es una virtud Alejandro – le dijo la abuela mirando a su nieto directamente a los ojos, - el siguiente nivel es "IZTEPETL", aquí los muertos tendrán que subir una gran cerro  cubierto de filosísimos pedernales, que desgarrarán sus cuepor pero tendrán que continuar si quieren salir de ahí. – 

    # Alejandro veía asombrado como su abuela contaba una travesía pero con cara de molestia por el dolor del viaje  

    # La abuela continua, - el cuarto nivel, el "lugar del viento de obsidiana" es un sitio desolado de hielo y piedra abrupta.  Se trata de una sierra con aristas cortantes compuesta de ocho collados en los que siempre caía nieve."  

    # Alejandro- "¿ por que tiene que doler tanto esta madr......?" 

    # Abuelo- lo ve feo y la da un sape 

    # Alejandro- " ¿.....no podemos acelerar el viaje ?" 

    # Abuela- toma aire -"En el quinto nivel, "El lugar donde la gente vuela y se voltea como banderas". Se dice que este lugar se ubicaba al pie del último collado o colina del Itzehecayan, donde los muertos perdían la gravedad y estaban a merced de los vientos, que los arrastraba hasta que finalmente eran liberados para pasar al nivel siguiente. – 

    # Alejandro interrumpe, - ¡espera abuela!  ¿qué pasa si mueren en una de esas pruebas? –  

    # Abuela - con una sonrisa en el rostro respondió, - alejandro las almas no pueden morir en el más allá, sentirán ese sufrimiento como si estuvieran con vida en esta vida terrenal, pero no morirán. –  

    # Alejandro proceso la respuesta-"no pues como que les gusta mucho el dolor aqui........" 

    # Abuela- prosiguió con los siguientes niveles.  – El sexto nivel, "El lugar donde la gente es flechada". En el, se encuentra un extenso sendero a cuyos lados manos invisibles envían puntiagudas saetas para acribillar a los cadáveres de los muertos que lo atravesaban. Estas son saetas pérdidas durante las batallas. 

    # Alejandro- interrumpe Alejandro son pensarlo dos veces -"¡aparete de que me aplastan, me cortan y me lanzan por los aires aun me van a dar de flechasos!"  

    # Abuela . Uy mijo el siguiente nivel es el TEOCOYOHUEHUALOYAN"  donde los jaguares les abren el pecho a las almas y se comen su corazón. –  

    # Alejandro- borro su sonrisa "  A NO NI MA.....".  

    # abuela– GRITA - "ALEJANDRO " - LE DA UN SAPE – continuo En el penúltimo nivel IZMICTLAN APOCHCALOLCA, que es la laguna de aguas negras, es donde los muertos dejan su cuerpo casi por completo y comienzan a liberan su alma.  

    # Alejandro-" jejej te ves muy chistosa de calavera abuela "- se tropieza en el rio  

    # Abuela –rie y continua-"Finalmente, las almas llegan a CHICUNAMICTLAN, en este lugar los muertos deberán atravesar las nueve aguas de Chiconauhhapan y, una vez superado este último obstáculo, su alma sería liberada completamente de los padecimientos del cuerpo, por los dioses de la muerte . – 

    # Alejandro familiarizo esos nombres diciendo, - Mictlantecuhtli y Mictecacihuatl, ¿no es verdad abuela? -  

    # Abuela -con voz amable respondió, - creí que no sabias pronunciarlo,pero bueno  se olvido mencionar que los difuntos deberán de ser enviados con algunos amuletos y pertenencias para facilitar su camino, entre agua, mantas, armas y otras pertenencias. –  

    # Comprendiendo eso, Alejandro respondió, - claro, no sería justo despues del matirio de camino y ademas llegar ante los mismísimo señores de la muerte con las manos vacías. – 

    # La abuela con una sonrisa en el rostro dijo: "bueno, ahora sabes por que hay que tenerles respeto a los muertos, ahora ayúdame a terminar la ofrenda".  

    return
