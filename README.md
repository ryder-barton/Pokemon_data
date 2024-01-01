WHAT THE CODE DOES:

pokedata.py extracts the ID number, name, types, height, and weight of the original 151 Pokemon from the Pokeapi website. pokedata_excel.py puts this data into an excel file titled "pokedata.xlsx". pokedata_type_excel.py puts the data into an excel file but seperates the pokemon by type and places each type into a different sheets in the workbook (note: if a pokemon has two types they will be placed in two sheets). 


WHY I CHOSE THIS PROJECT:

I wanted to start a simple project to gather some experience in data analysis. I originally wanted to scrape sports stats from a particular player, however, MLB does not allow web scraping.
I searched for stat-gathering APIs but they were either too complicated or cost money. After a quick Google search I came across Pokeapi and decided to gather data from this apis existence is free and promotes learning.
I decided to gather data to answer the following question: DOES A POKEMON'S TYPE HAVE ANY CORRELATION WITH THEIR HEIGHT AND WEIGHT?


WHAT I FOUND:

My results found that water and poison Pokemon make up the majority of the total height and weight of all the Pokemon. However, I believe that this was because water and poison types are the most common.
To get better results I decided to take the average of each type. By average height, dragon types are the tallest. By average weight ice is the heaviest. I do find it important to note that there are only 3 dragon types and 5 ice types out of the original 151 Pokemon.
Some interesting finds:
  Ghost and bug Pokemon weighed the least on average. This of course makes sense logically.
  Rock types were the second heaviest by average. Logically this also makes sense.
  Even though Snorlax, a normal type, is the heaviest Pokemon at 1000+lbs, normal types ranked in the bottom half of average weight.
  Only 5 Pokemon are over 10ft tall.
In conclusion, type has some correlation with the height or weight of each Pokemon, but no type dominates a particular field. This may be due to the fact I only used the first 151 Pokemon in my study. In the future, I will factor in the other Pokemon and see if my results change.
