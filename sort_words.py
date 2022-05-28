import pandas as pd

input_file = "game_dictionary.xlsx"
output_file = "game_dictionary_filtered.csv"

# import file
dictionary = pd.read_excel(input_file)

# remove words with no Type (non-words)
dictionary = dictionary[dictionary["Type"].notnull()]

# remove words of type "pl. " - lots of "of *" words
dictionary = dictionary[dictionary["Type"] != "pl. "]

# remove the rest of the "of *" words (note the negate (invert) "~" ;)
dictionary = dictionary[~dictionary["Definition"].str.startswith('of ')]

# remove some other variations that wouldn't be fun inside of a game
dictionary = dictionary[~dictionary["Definition"].str.startswith('Alt of')]
dictionary = dictionary[~dictionary["Definition"].str.startswith('Alt. of')]
dictionary = dictionary[~dictionary["Definition"].str.startswith('See ')]

# remove any really long definitions, so we know it won't overflow
# this does remove many valuable words, but in our case, we have plenty of others
dictionary = dictionary[dictionary.Definition.apply(lambda x: len(str(x)) < 250)]

# replace each type with the full name (instead an abbreviation), NOTE: ORDER MATTERS (i.e. if "v. t." gets replaced, it will never find "v. t. & i.")
dictionary["Type"] = dictionary["Type"].str.replace('prep.','preposition', regex=False)
dictionary["Type"] = dictionary["Type"].str.replace('p.','preposition', regex=False)
dictionary["Type"] = dictionary["Type"].str.replace('n. sing. & pl.','singular & plural noun', regex=False)
dictionary["Type"] = dictionary["Type"].str.replace('n. pl.','plural noun', regex=False)
dictionary["Type"] = dictionary["Type"].str.replace('n.','noun', regex=False)
dictionary["Type"] = dictionary["Type"].str.replace('adv.','adverb', regex=False)
dictionary["Type"] = dictionary["Type"].str.replace('n.','noun', regex=False)
dictionary["Type"] = dictionary["Type"].str.replace('a.','adjective', regex=False)
dictionary["Type"] = dictionary["Type"].str.replace('v. t. & i.','transitive & intransitive verb', regex=False)
dictionary["Type"] = dictionary["Type"].str.replace('v. i. & t.','transitive & intransitive verb', regex=False)
dictionary["Type"] = dictionary["Type"].str.replace('v. i.','intransitive verb', regex=False)
dictionary["Type"] = dictionary["Type"].str.replace('v. t.','transitive verb', regex=False)
dictionary["Type"] = dictionary["Type"].str.replace('v.','verb', regex=False)
dictionary["Type"] = dictionary["Type"].str.replace('superl.','superlative', regex=False)


dictionary["CharCount"] = dictionary["Word"].str.len()


dictionary.to_csv(output_file, index=False)

#print(dictionary.head())
