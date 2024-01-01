WHAT THIS CODE DOES:

This code extracts data from the pokeapi website, shows the data in the terminal, and then places that data into an excel file. 
The data this code collects include the following:
  ID number for each pokemon
  Name of each pokemon
  Types of each pokemon
  Height of each pokemon
  Weight of each pokemon
This code only extracts the data from the original 151 pokemon. However, by changing the range in LINE 10, it is possible to gather data on more or less pokemon.


WHY I CHOSE THIS PROJECT:

I wanted to start a simple project to gather some experience in data analysis. I originally wanted to scrape sports stats from a particular player, however, mlb does not allow webscraping.
I searched for stat gathering apis but they were either too complicated or costed money. After a quick google search I came across pokeapi and decided to gather data from this apis existence is free and promotes learning.
I decided to gather data to answer the following question: DOES A POKEMON'S TYPE HAVE ANY CORRELATION WITH THEIR HEIGHT AND WEIGHT?


WHAT I FOUND:

My results found that water and poison pokemon make up the mojoirty of the total height and weight of all the pokemon. However, I believed that this was due to the fact that water and poison types are the most common.
To get beter results I decided to take the average of each type. By average height, dragon types are the tallest. By average weight ice is the heaviest. I do find it important to note that there are only 3 dragon types and 5 ice types out of the original 151 pokemon.
Some interesting finds:
  Ghost and bug pokemon weighed the least by average. This of course makes sense logically.
  Rock types were the second heaviest by average. Logically this also makes sense.
  Even though Snorlax, a normal type, is the heaviest pokemon at 1000+lbs, normal types ranked in the bottom half of average weight.
  Only 5 pokemon are over 10ft tall.
In conclusion, type has some correlation with the height of weight of each pokemon, but no type dominated a particular field. This may be due to the fact I only used the first 151 pokemon in my study. In the future I will factor in the other pokemon and see if my results changed.
