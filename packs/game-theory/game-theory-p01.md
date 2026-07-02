---
title: "Game theory (part 1/2)"
source: https://en.wikipedia.org/wiki/Game_theory
domain: game-theory
license: CC-BY-SA-4.0
tags: game theory, nash equilibrium, zero-sum game, cooperative game
fetched: 2026-07-02
part: 1/2
---

# Game theory

**Game theory** is the study of mathematical models of strategic interactions. It has applications in many fields of social science, and is used extensively in economics, logic, systems science and computer science. Initially, game theory addressed two-person zero-sum games, in which a participant's gains or losses are exactly balanced by the losses and gains of the other participant. In the 1950s, it was extended to the study of non zero-sum games, and was eventually applied to a wide range of behavioral relations. It is now an umbrella term for the science of rational decision making in humans, animals, and computers.

Modern game theory began with the idea of mixed-strategy equilibria in two-person zero-sum games and its proof by John von Neumann. Von Neumann's original proof used the Brouwer fixed-point theorem on continuous mappings into compact convex sets, which became a standard method in game theory and mathematical economics. His paper was followed by *Theory of Games and Economic Behavior* (1944), co-written with Oskar Morgenstern, which considered cooperative games of several players. The second edition provided an axiomatic theory of expected utility, which allowed mathematical statisticians and economists to treat decision-making under uncertainty.

Game theory was developed extensively in the 1950s, and was explicitly applied to evolution in the 1970s, although similar developments go back at least as far as the 1930s. Game theory has been widely recognized as an important tool in many fields. John Maynard Smith was awarded the Crafoord Prize for his application of evolutionary game theory in 1999, and fifteen game theorists have won the Nobel Prize in economics as of 2020, including most recently Paul Milgrom and Robert B. Wilson.


## History

Discussions on the mathematics of games began long before the rise of modern, mathematical game theory. Cardano wrote on games of chance in *Liber de ludo aleae* (*Book on Games of Chance*), written around 1564 but published posthumously in 1663. Influenced by the work of Fermat and Pascal on the problem of points, Huygens developed the concept of expectation on reasoning about the structure of games of chance, publishing his gambling calculus in *De ratiociniis in ludo aleæ* (*On Reasoning in Games of Chance*) in 1657.

In 1713, a letter attributed to Charles Waldegrave, an active Jacobite and uncle to British diplomat James Waldegrave, analyzed a game called "le her". Waldegrave provided a minimax mixed strategy solution to a two-person version of the card game, and the problem is now known as the Waldegrave problem.

In 1838, Antoine Augustin Cournot provided a model of competition in oligopolies. Though he did not refer to it as such, he presented a solution that is the Nash equilibrium of the game in his *Recherches sur les principes mathématiques de la théorie des richesses* (*Researches into the Mathematical Principles of the Theory of Wealth*). In 1883, Joseph Bertrand critiqued Cournot's model as unrealistic, providing an alternative model of price competition which would later be formalized by Francis Ysidro Edgeworth.

In 1913, Ernst Zermelo published *Über eine Anwendung der Mengenlehre auf die Theorie des Schachspiels* (*On an Application of Set Theory to the Theory of the Game of Chess*), which proved that the optimal chess strategy is strictly determined.

### Foundation

The work of John von Neumann established game theory as its own independent field in the early-to-mid 20th century, with von Neumann publishing his paper *On the Theory of Games of Strategy* in 1928. Von Neumann's original proof used Brouwer's fixed-point theorem on continuous mappings into compact convex sets, which became a standard method in game theory and mathematical economics. Von Neumann's work in game theory culminated in his 1944 book *Theory of Games and Economic Behavior*, co-authored with Oskar Morgenstern. The second edition of this book provided an axiomatic theory of utility, which reincarnated Daniel Bernoulli's old theory of utility (of money) as an independent discipline. This foundational work contains the method for finding mutually consistent solutions for two-person zero-sum games. Subsequent work focused primarily on cooperative game theory, which analyzes optimal strategies for groups of individuals, presuming that they can enforce agreements between them about proper strategies.

In his 1938 book *Applications aux Jeux de Hasard* and earlier notes, Émile Borel proved a minimax theorem for two-person zero-sum matrix games only when the pay-off matrix is symmetric and provided a solution to a non-trivial infinite game (known in English as Blotto game). Borel conjectured the non-existence of mixed-strategy equilibria in finite two-person zero-sum games, a conjecture that was proved false by von Neumann.

In 1950, John Nash developed a criterion for mutual consistency of players' strategies known as the Nash equilibrium, applicable to a wider variety of games than the criterion proposed by von Neumann and Morgenstern. Nash proved that every finite n-player, non-zero-sum (not just two-player zero-sum) non-cooperative game has what is now known as a Nash equilibrium in mixed strategies.

Game theory experienced a flurry of activity in the 1950s, during which the concepts of the core, the extensive form game, fictitious play, repeated games, and the Shapley value were developed. The 1950s also saw the first applications of game theory to philosophy and political science. The first mathematical discussion of the prisoner's dilemma appeared, and an experiment was undertaken by mathematicians Merrill M. Flood and Melvin Dresher, as part of the RAND Corporation's investigations into game theory. RAND pursued the studies because of possible applications to global nuclear strategy.

#### Prize-winning achievements

In 1965, Reinhard Selten introduced his solution concept of subgame perfect equilibria, which further refined the Nash equilibrium. Later he would introduce trembling hand perfection as well. In 1994 Nash, Selten and Harsanyi became Economics Nobel Laureates for their contributions to economic game theory.

In the 1970s, game theory was extensively applied in biology, largely as a result of the work of John Maynard Smith and his evolutionarily stable strategy. In addition, the concepts of correlated equilibrium, trembling hand perfection and common knowledge were introduced and analyzed.

In 1994, John Nash was awarded the Nobel Memorial Prize in the Economic Sciences for his contribution to game theory. Nash's most famous contribution to game theory is the concept of the Nash equilibrium, which is a solution concept for non-cooperative games, published in 1951. A Nash equilibrium is a set of strategies, one for each player, such that no player can improve their payoff by unilaterally changing their strategy.

In 2005, game theorists Thomas Schelling and Robert Aumann followed Nash, Selten, and Harsanyi as Nobel Laureates. Schelling worked on dynamic models, early examples of evolutionary game theory. Aumann contributed more to the equilibrium school, introducing equilibrium coarsening and correlated equilibria, and developing an extensive formal analysis of the assumption of common knowledge and of its consequences.

In 2007, Leonid Hurwicz, Eric Maskin, and Roger Myerson were awarded the Nobel Prize in Economics "for having laid the foundations of mechanism design theory". Myerson's contributions include the notion of proper equilibrium, and an important graduate text: *Game Theory, Analysis of Conflict*. Hurwicz introduced and formalized the concept of incentive compatibility.

In 2012, Alvin E. Roth and Lloyd S. Shapley were awarded the Nobel Prize in Economics "for the theory of stable allocations and the practice of market design". In 2014, the Nobel went to game theorist Jean Tirole.


## Different types of games

### Cooperative / non-cooperative

A game is *cooperative* if the players are able to form binding commitments externally enforced (e.g. through contract law). A game is *non-cooperative* if players cannot form alliances or if all agreements need to be self-enforcing (e.g. through credible threats).

Cooperative games are often analyzed through the framework of *cooperative game theory*, which focuses on predicting which coalitions will form, the joint actions that groups take, and the resulting collective payoffs. It is different from *non-cooperative game theory* which focuses on predicting individual players' actions and payoffs by analyzing Nash equilibria.

Cooperative game theory provides a high-level approach as it describes only the structure and payoffs of coalitions, whereas non-cooperative game theory also looks at how strategic interaction will affect the distribution of payoffs. As non-cooperative game theory is more general, cooperative games can be analyzed through the approach of non-cooperative game theory (the converse does not hold) provided that sufficient assumptions are made to encompass all the possible strategies available to players due to the possibility of external enforcement of cooperation.

### Symmetric / asymmetric

|   | E | F |
|---|---|---|
| E | 1, 2 | 0, 0 |
| F | 0, 0 | 1, 2 |
| *An asymmetric game* |   |   |

A symmetric game is a game where each player earns the same payoff when making the same choice. In other words, the identity of the player does not change the resulting game facing the other player. Many of the commonly studied 2×2 games are symmetric. The standard representations of chicken, the prisoner's dilemma, and the stag hunt are all symmetric games.

The most commonly studied asymmetric games are games where there are not identical strategy sets for both players. For instance, the ultimatum game and similarly the dictator game have different strategies for each player. It is possible, however, for a game to have identical strategies for both players, yet be asymmetric. For example, the game pictured in this section's graphic is asymmetric despite having identical strategy sets for both players.

### Zero-sum / non-zero-sum

|   | A | B |
|---|---|---|
| A | –1, 1 | 3, −3 |
| B | 0, 0 | –2, 2 |
| *A zero-sum game* |   |   |

Zero-sum games (more generally, constant-sum games) are games in which choices by players can neither increase nor decrease the available resources. In zero-sum games, the total benefit goes to all players in a game, for every combination of strategies, and always adds to zero (more informally, a player benefits only at the equal expense of others). Poker exemplifies a zero-sum game (ignoring the possibility of the house's cut), because one wins exactly the amount one's opponents lose. Other zero-sum games include matching pennies and most classical board games including Go and chess.

Many games studied by game theorists (including the famed prisoner's dilemma) are non-zero-sum games, because the outcome has net results greater or less than zero. Informally, in non-zero-sum games, a gain by one player does not necessarily correspond with a loss by another.

Furthermore, *constant-sum games* correspond to activities like theft and gambling, but not to the fundamental economic situation in which there are potential gains from trade. It is possible to transform any constant-sum game into a (possibly asymmetric) zero-sum game by adding a dummy player (often called "the board") whose losses compensate the players' net winnings.

### Simultaneous / sequential

Simultaneous games are games where both players move simultaneously, or instead the later players are unaware of the earlier players' actions (making them *effectively* simultaneous). Sequential games (a type of dynamic games) are games where players do not make decisions simultaneously, and player's earlier actions affect the outcome and decisions of other players. This need not be perfect information about every action of earlier players; it might be very little knowledge. For instance, a player may know that an earlier player did not perform one particular action, while they do not know which of the other available actions the first player actually performed.

The difference between simultaneous and sequential games is captured in the different representations discussed above. Often, normal form is used to represent simultaneous games, while extensive form is used to represent sequential ones. The transformation of extensive to normal form is one way, meaning that multiple extensive form games correspond to the same normal form. Consequently, notions of equilibrium for simultaneous games are insufficient for reasoning about sequential games; see subgame perfection.

In short, the differences between sequential and simultaneous games are as follows:

|   | Sequential | Simultaneous |
|---|---|---|
| Normally denoted by | Decision trees | Payoff matrices |
| Prior knowledge of opponent's move? | Yes | No |
| Time axis? | Yes | No |
| Also known as | Extensive-form game Extensive game | Strategy game Strategic game |

### Perfect information and imperfect information

An important subset of sequential games consists of games of perfect information. A game with perfect information means that all players, at every move in the game, know the previous history of the game and the moves previously made by all other players. An imperfect information game is played when the players do not know all moves already made by the opponent such as a simultaneous move game. Examples of perfect-information games include tic-tac-toe, checkers, chess, and Go.

Many card games are games of imperfect information, such as poker and bridge. Perfect information is often confused with complete information, which is a similar concept pertaining to the common knowledge of each player's sequence, strategies, and payoffs throughout gameplay. Complete information requires that every player know the strategies and payoffs available to the other players but not necessarily the actions taken, whereas perfect information is knowledge of all aspects of the game and players. Games of incomplete information can be reduced, however, to games of imperfect information by introducing "moves by nature".

### Bayesian game

One of the assumptions of the Nash equilibrium is that every player has correct beliefs about the actions of the other players. However, there are many situations in game theory where participants do not fully understand the characteristics of their opponents. Negotiators may be unaware of their opponent's valuation of the object of negotiation, companies may be unaware of their opponent's cost functions, combatants may be unaware of their opponent's strengths, and jurors may be unaware of their colleague's interpretation of the evidence at trial. In some cases, participants may know the character of their opponent well, but may not know how well their opponent knows his or her own character.

Bayesian game means a strategic game with incomplete information. For a strategic game, decision makers are players, and every player has a group of actions. A core part of the imperfect information specification is the set of states. Every state completely describes a collection of characteristics relevant to the player such as their preferences and details about them. There must be a state for every set of features that some player believes may exist.

For example, where Player 1 is unsure whether Player 2 would rather date her or get away from her, while Player 2 understands Player 1's preferences as before. To be specific, supposing that Player 1 believes that Player 2 wants to date her under a probability of 1/2 and get away from her under a probability of 1/2 (this evaluation comes from Player 1's experience probably: she faces players who want to date her half of the time in such a case and players who want to avoid her half of the time). Due to the probability involved, the analysis of this situation requires to understand the player's preference for the draw, even though people are only interested in pure strategic equilibrium.

### Combinatorial games

Games in which the difficulty of finding an optimal strategy stems from the multiplicity of possible moves are called combinatorial games. Examples include chess, shogi, and Go. Games that involve imperfect information may also have a strong combinatorial character, for instance backgammon. There is no unified theory addressing combinatorial elements in games. There are, however, mathematical tools that can solve some particular problems and answer some general questions.

Games of perfect information have been studied in combinatorial game theory, which has developed novel representations, e.g. surreal numbers, as well as combinatorial and algebraic (and sometimes non-constructive) proof methods to solve games of certain types, including "loopy" games that may result in infinitely long sequences of moves. These methods address games with higher combinatorial complexity than those usually considered in traditional (or "economic") game theory. A typical game that has been solved this way is Hex. A related field of study, drawing from computational complexity theory, is game complexity, which is concerned with estimating the computational difficulty of finding optimal strategies.

Research in artificial intelligence has addressed both perfect and imperfect information games that have very complex combinatorial structures (like chess, go, or backgammon) for which no provable optimal strategies have been found. The practical solutions involve computational heuristics, like alpha–beta pruning or use of artificial neural networks trained by reinforcement learning, which make games more tractable in computing practice.

### Discrete and continuous games

Much of game theory is concerned with finite, discrete games that have a finite number of players, moves, events, outcomes, etc. Many concepts can be extended, however. Continuous games allow players to choose a strategy from a continuous strategy set. For instance, Cournot competition is typically modeled with players' strategies being any non-negative quantities, including fractional quantities.

### Differential games

Differential games such as the continuous pursuit and evasion game are continuous games where the evolution of the players' state variables is governed by differential equations. The problem of finding an optimal strategy in a differential game is closely related to the optimal control theory. In particular, there are two types of strategies: the open-loop strategies are found using the Pontryagin maximum principle while the closed-loop strategies are found using Bellman's Dynamic Programming method.

A particular case of differential games are the games with a random time horizon. In such games, the terminal time is a random variable with a given probability distribution function. Therefore, the players maximize the mathematical expectation of the cost function. It was shown that the modified optimization problem can be reformulated as a discounted differential game over an infinite time interval.

### Evolutionary game theory

Evolutionary game theory studies players who adjust their strategies over time according to rules that are not necessarily rational or farsighted. In general, the evolution of strategies over time according to such rules is modeled as a Markov chain with a state variable such as the current strategy profile or how the game has been played in the recent past. Such rules may feature imitation, optimization, or survival of the fittest.

In biology, such models can represent evolution, in which offspring adopt their parents' strategies and parents who play more successful strategies (i.e. corresponding to higher payoffs) have a greater number of offspring. In the social sciences, such models typically represent strategic adjustment by players who play a game many times within their lifetime and, consciously or unconsciously, occasionally adjust their strategies.

### Stochastic outcomes (and relation to other fields)

Individual decision problems with stochastic outcomes are sometimes considered "one-player games". They may be modeled using similar tools within the related disciplines of decision theory, operations research, and areas of artificial intelligence, particularly AI planning (with uncertainty) and multi-agent system. Although these fields may have different motivators, the mathematics involved are substantially the same, e.g. using Markov decision processes (MDP).

Stochastic outcomes can also be modeled in terms of game theory by adding a randomly acting player who makes "chance moves" ("moves by nature"). This player is not typically considered a third player in what is otherwise a two-player game, but merely serves to provide a roll of the dice where required by the game.

For some problems, different approaches to modeling stochastic outcomes may lead to different solutions. For example, the difference in approach between MDPs and the minimax solution is that the latter considers the worst-case over a set of adversarial moves, rather than reasoning in expectation about these moves given a fixed probability distribution. The minimax approach may be advantageous where stochastic models of uncertainty are not available, but may also be overestimating extremely unlikely (but costly) events, dramatically swaying the strategy in such scenarios if it is assumed that an adversary can force such an event to happen. (See Black swan theory for more discussion on this kind of modeling issue, particularly as it relates to predicting and limiting losses in investment banking.)

General models that include all elements of stochastic outcomes, adversaries, and partial or noisy observability (of moves by other players) have also been studied. The "gold standard" is considered to be partially observable stochastic game (POSG), but few realistic problems are computationally feasible in POSG representation.

### Metagames

These are games the play of which is the development of the rules for another game, the target or subject game. Metagames seek to maximize the utility value of the rule set developed. The theory of metagames is related to mechanism design theory.

The term metagame analysis is also used to refer to a practical approach developed by Nigel Howard, whereby a situation is framed as a strategic game in which stakeholders try to realize their objectives by means of the options available to them. Subsequent developments have led to the formulation of confrontation analysis.

### Mean field game theory

Mean field game theory is the study of strategic decision making in very large populations of small interacting agents. This class of problems was considered in the economics literature by Boyan Jovanovic and Robert W. Rosenthal, in the engineering literature by Peter E. Caines, and by mathematicians Pierre-Louis Lions and Jean-Michel Lasry.


## Representation of games

The games studied in game theory are well-defined mathematical objects. To be fully defined, a game must specify the following elements: the *players* of the game, the *information* and *actions* available to each player at each decision point, and the *payoffs* for each outcome. (Eric Rasmusen refers to these four "essential elements" by the acronym "PAPI".) A game theorist typically uses these elements, along with a solution concept of their choosing, to deduce a set of equilibrium strategies for each player such that, when these strategies are employed, no player can profit by unilaterally deviating from their strategy. These equilibrium strategies determine an equilibrium to the game—a stable state in which either one outcome occurs or a set of outcomes occur with known probability.

Most cooperative games are presented in the characteristic function form, while the extensive and the normal forms are used to define noncooperative games.

### Extensive form

The extensive form can be used to formalize games with a time sequencing of moves. Extensive form games can be visualized using game trees (as pictured here). Here each vertex (or node) represents a point of choice for a player. The player is specified by a number listed by the vertex. The lines out of the vertex represent a possible action for that player. The payoffs are specified at the bottom of the tree. The extensive form can be viewed as a multi-player generalization of a decision tree. To solve any extensive form game, backward induction must be used. It involves working backward up the game tree to determine what a rational player would do at the last vertex of the tree, what the player with the previous move would do given that the player with the last move is rational, and so on until the first vertex of the tree is reached.

The game pictured consists of two players. The way this particular game is structured (i.e., with sequential decision making and perfect information), *Player 1* "moves" first by choosing either *F* or *U* (fair or unfair). Next in the sequence, *Player 2*, who has now observed *Player 1*'s move, can choose to play either *A* or *R* (accept or reject). Once *Player 2* has made their choice, the game is considered finished and each player gets their respective payoff, represented in the image as two numbers, where the first number represents Player 1's payoff, and the second number represents Player 2's payoff. Suppose that *Player 1* chooses *U* and then *Player 2* chooses *A*: *Player 1* then gets a payoff of "eight" (which in real-world terms can be interpreted in many ways, the simplest of which is in terms of money but could mean things such as eight days of vacation or eight countries conquered or even eight more opportunities to play the same game against other players) and *Player 2* gets a payoff of "two".

The extensive form can also capture simultaneous-move games and games with imperfect information. To represent it, either a dotted line connects different vertices to represent them as being part of the same information set (i.e. the players do not know at which point they are), or a closed line is drawn around them. (See example in the imperfect information section.)

### Normal form

|   | Player 2 chooses *Left* | Player 2 chooses *Right* |
|---|---|---|
| Player 1 chooses *Up* | **4**, **3** | **–1**, **–1** |
| Player 1 chooses *Down* | **0**, **0** | **3**, **4** |
| *Normal form or payoff matrix of a 2-player, 2-strategy game* |   |   |

The normal (or strategic form) game is usually represented by a matrix which shows the players, strategies, and payoffs (see the example to the right). More generally it can be represented by any function that associates a payoff for each player with every possible combination of actions. In the accompanying example there are two players; one chooses the row and the other chooses the column. Each player has two strategies, which are specified by the number of rows and the number of columns. The payoffs are provided in the interior. The first number is the payoff received by the row player (Player 1 in our example); the second is the payoff for the column player (Player 2 in our example). Suppose that Player 1 plays *Up* and that Player 2 plays *Left*. Then Player 1 gets a payoff of 4, and Player 2 gets 3.

When a game is presented in normal form, it is presumed that each player acts simultaneously or, at least, without knowing the actions of the other. If players have some information about the choices of other players, the game is usually presented in extensive form.

Every extensive-form game has an equivalent normal-form game, however, the transformation to normal form may result in an exponential blowup in the size of the representation, making it computationally impractical.

### Characteristic function form

In cooperative game theory the characteristic function lists the payoff of each coalition. The origin of this formulation is in John von Neumann and Oskar Morgenstern's book.

Formally, a characteristic function is a function $v:2^{N}\to \mathbb {R}$ from the set of all possible coalitions of players to a set of payments, and also satisfies $v(\emptyset )=0$ . The function describes how much collective payoff a set of players can gain by forming a coalition.

### Alternative game representations

Alternative game representation forms are used for some subclasses of games or adjusted to the needs of interdisciplinary research. In addition to classical game representations, some of the alternative representations also encode time related aspects.

| Name | Year | Means | Type of games | Time |
|---|---|---|---|---|
| Congestion game | 1973 | functions | subset of n-person games, simultaneous moves | No |
| Sequential form | 1994 | matrices | 2-person games of imperfect information | No |
| Timed games | 1994 | functions | 2-person games | Yes |
| Gala | 1997 | logic | n-person games of imperfect information | No |
| Graphical games | 2001 | graphs, functions | n-person games, simultaneous moves | No |
| Local effect games | 2003 | functions | subset of n-person games, simultaneous moves | No |
| GDL | 2005 | logic | deterministic n-person games, simultaneous moves | No |
| Game Petri-nets | 2006 | Petri net | deterministic n-person games, simultaneous moves | No |
| Continuous games | 2007 | functions | subset of 2-person games of imperfect information | Yes |
| PNSI | 2008 | Petri net | n-person games of imperfect information | Yes |
| Action graph games | 2012 | graphs, functions | n-person games, simultaneous moves | No |
