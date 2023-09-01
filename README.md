# Hackaton-Gorinchem
Hackaton Gorinchem -- What Will We Play


## voting phases:

- `adding`: you can add games
- `voting`: you can vote on games, but only games already added.
- `closed`: vote already concluded. something has already won.


## references

the keys are always lowercase, value does not need to be lowercase

## naming

je Vote op een Poll. Dus een vote is wat een persoon kiest. Een poll is het ding waar je op kan voten. Haal t niet door de war.

## todo
- in de getpolllist `command` kijken naar de state van elke poll, is ie al geclosed bijvoorbeeld? en of jouw stem daar ook tussen zit.
- `command` om poll te verwijderen
- `command` om poll informatie te krijgen, wie heeft gemaakt, hoeveel votes, waarop is gevote? Wat is de current winner.
- `command` om poll naar stage `closed` te zetten
- `command` om poll naar stage `voting` te zetten
  - delete admin `command`
  - add admin `command` (using the already made function)
- delete references `command`
- see references list `command`
- add references `command`
  - see who the bot admins are `command`
  - see if someone is admin and what rights they have `command` (use the function that we already have for it)
- optional: `command` die alleen de top 10% van de gevote games houdt om op te voten, en bij de rest de votes leegmaakt, dus iedereen die op mogus heeft gestemd zodra het afvalt, kan opnieuw stemmen.
- optional: pollDescription, is deze poll voor zaterdag of zondag bijvoorbeeld. of thema van de poll, whatever je maar wil.