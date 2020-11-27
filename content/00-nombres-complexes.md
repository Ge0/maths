# Nombres complexes

## Introduction

Vous connaissez l’ensemble des nombres réels 
$\mathbb R$ qui inclut l’ensemble des nombres possibles avec ou sans chiffre après la virgule.

Nous allons voir ici les nombres complexes, dont l’ensemble est représenté par le sigle $\mathbb C$.

Un nombre complexe est un nombre qui possède une partie **réelle** $a$ et une partie **imaginaire** $b$ et peut s’écrire sous la forme $z = a + ib$ avec $i^2 = -1$.

## Partie réelle, partie imaginaire

Nous utilisons aussi les définitions suivantes :

- $\Re(z) = a$ (partie réelle) ;
- $\Im(z) = b$ (partie imaginaire).

Par exemple, si $z = 5 + 3i$ alors $\Re(z) = 5$ et $\Im(z) = 3$.

Si $\Im(z) = 0$ alors $z \subset \mathbb R$. Autrement dit, si la partie imaginaire de $z$ est nulle, $z$ est un nombre réel (logique).

Si $\Re(z) = 0$, alors $z$ est un **nombre imaginaire pur** (parce que sa partie réelle est nulle).

## Nombre complexe conjugué

Soit le nombre complexe $z = a + ib$. On note
son conjugué $\overline{z}$ dont la partie imaginaire est l’opposée de celle de $z$. Ainsi $\overline{z} = a - ib$.

Par exemple, si $z = 5 + 3i$ alors $\overline{z} = 5 - 3i$ est le conjugué de $z$.

## Représentation graphique d'un nombre complexe

Si l’on peut représenter l’ensemble des nombres réels sur une droite, on constate que nous pouvons représenter les nombres complexes sur un repère orthonormé.

Par exemple, pour un nombre complexe $z$, nous pourrions le représenter par un point sur ce repère où sa partie réelle serait représentée sur *l’abscisse* et sa partie imaginaire serait représentée par *l’ordonnée*.

Ainsi, si nous voulions représenter le nombre complexe $z = 3i - 2$, qui aurait pour abscisse $-2$ et
pour ordonnée $3$, nous pourrions procéder comme suit :


\begin{center}
\begin{tikzpicture}[scale=2,cap=round,>=latex]
	% draw the coordinates
	\draw[->] (-1.5cm,0cm) -- (1.5cm,0cm) node[right,fill=white] {$x$};
	\draw[->] (0cm,-1.5cm) -- (0cm,1.5cm) node[above,fill=white] {$y$};

	% draw the unit circle
	\draw[thick] (0cm,0cm) circle(1cm);

	% draw the horizontal and vertical coordinates
	% the placement is better this way
	\draw (-1.25cm,0cm) node[above=1pt] {$(-1,0)$}
		  (1.25cm,0cm)  node[above=1pt] {$(1,0)$}
		  (0cm,-1.25cm) node[fill=white] {$(0,-1)$}
		  (0cm,1.25cm)  node[fill=white] {$(0,1)$};
\end{tikzpicture}
\end{center}