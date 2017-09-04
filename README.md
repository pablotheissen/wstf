# Wiener Sachtextformeln
Textverständlichkeit mit Hilfe der Wiener Sachtextformel in Python automatisch ermitteln.

# Was ist die Wiener Sachtextformel?
[Wikipedia](https://de.wikipedia.org/wiki/Lesbarkeitsindex#Wiener_Sachtextformel):<br/>
Die Wiener Sachtextformel dient zur Berechnung der Lesbarkeit deutschsprachiger Texte. Sie gibt an, für welche Schulstufe ein Sachtext geeignet ist. Die Skala beginnt bei Schulstufe 4 und endet bei 15, wobei ab der Stufe 12 eher von Schwierigkeitsstufen als von Schulstufen gesprochen werden sollte. Ein Wert von 4 steht demnach für sehr leichten Text, dagegen bezeichnet 15 einen sehr schwierigen Text.

Die Formel wurde aufgestellt von Richard Bamberger und Erich Vanecek.

MS ist der Prozentanteil der Wörter mit drei oder mehr Silben,
SL ist die mittlere Satzlänge (Anzahl Wörter),
IW ist der Prozentanteil der Wörter mit mehr als sechs Buchstaben,
ES ist der Prozentanteil der einsilbigen Wörter.

**Die erste Wiener Sachtextformel**<br/>
WSTF1=0,1935⋅MS+0,1672⋅SL+0,1297⋅IW−0,0327⋅ES−0,875

**Die zweite Wiener Sachtextformel**<br/>
WSTF2=0,2007⋅MS+0,1682⋅SL+0,1373⋅IW−2,779

**Die dritte Wiener Sachtextformel**<br/>
WSTF3=0,2963⋅MS+0,1905⋅SL−1,1144

**Die vierte Wiener Sachtextformel (›im Hinblick auf die Jahrgangsstufe‹)**<br/>
WSTF4=0,2656⋅SL+0,2744⋅MS−1,693
