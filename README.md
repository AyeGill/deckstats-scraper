# Deckstats scraper

A collection of scripts to scrape [deckstats](https://deckstats.net) for decklists.
Mostly intended for EDH decklists.
So fragile that practically any update will break it - don't use it for something important!


- `page2deckjson` is just a super-simple regex script that takes the output of `curl <decklist-page>` and outputs the json string corresponding to the decklist.
- `json2decklist.py` is a simple python script that reads json input and outputs a list of cards and quantities. Has special logic for commanders, does not output sideboards (unless the commander is there).
- `search-link-scraper` reads all the 500 pages of most recent edh lists into the file `list-links.txt`.
- `list-scraper` reads from `list-links.txt`, and reads the decklist of each of the lists there, into sequentially numbered files in the `decks/` directory.

Decklists are output in this format:
Each line is a number, followed by a space, followed by a card name.
Optionally, the first line can have the letter `C` instead of a number, signifying that this is the commander.
(This should always be the case, but currently the behaviour on malformed or incomplete lists is mostly undetermined).

Note that sending too many requests to deckstats can result in getting your IP temporarily blocked :(.

Currently there's an unresolved issue from the 20th deck on when running `list-scraper`.
Strangely, does not seem to be connected to the IP blocking.