# wordGameList

A pandas project to further refine a word list to be used in games.
<br/>
<br/>
I needed a refined version of words for a word game I was making for my mom ❤️❤️
<br/>
<br/>
This is based on this list:
https://github.com/manassharma07/English-Dictionary-CSV

<br/>
<br/>

**The code is commented, but it can seem like a block of code.. Here's the jist of it.**

1. Import the game_dictionary.xlsx (the original file), and decide your output format (a csv)

2. There are a number of "definitions", like **"Aaron's rod"** that would be strange to have in a game, so we remove them.

3. The original game was a vocabulary game, so we remove plural words. They weren't fun to define in a game (e.g. Definition of "Abbeys" is "of Abbey") 

![image](https://user-images.githubusercontent.com/26286189/170828147-77b45aa4-1f4a-4af1-9d13-df2a1bd2c374.png)


4. Next we remove alternative words, and also definitions that are super long (< 250 characters), so we can have consistency when loading into a game. (in some cases you may just want all words, but in mine, I preferred consistency of definition length over word list length)

5. Then we replace the abberviated word type (e.g. prep. --> preposition).
<img width="1224" alt="word type" src="https://user-images.githubusercontent.com/26286189/170828504-757b79b7-d118-4935-99f7-f33f91c56b01.png">
(These could be grouped up in one line, but at the cost of readability, so it's done in steps)


6. Now we add a charCount row, so we can use it in game (i.e. increase difficulty by increasing word character count)

7. Finally we export to the csv!
<br/>
<br/>

 **I claim no ownership over the english language 😉, the original or revised list** Feel free to use as you like.
