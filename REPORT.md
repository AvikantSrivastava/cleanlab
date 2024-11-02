## REPORT

I have added a new submodule called `lexical_analysis` within the Cleanlab package.

It can be imported via a python import. It have 4 submodule, readability, coherence, spell_check and grammar_quality for Lexical analysis.
```python
from cleanlab.lexical_analysis.readability import ReadabilityPredictor
from cleanlab.lexical_analysis.grammar_quality import GrammarChecker
from cleanlab.lexical_analysis.coherence import Coherence
from cleanlab.lexical_analysis.coherence import GensimCoherence
from cleanlab.lexical_analysis.spell_check import SpellingChecker
```

To use the new functionality install the cleanlab package in the same way as before, I have updated the `requirements.txt` file so it should not have package dependency issue.

## Here are some examples to use the lexical analysis toolkit

#### ReadabilityPredictor
```python
ugly_sentence = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
nice_sentence = "The European Organization for Nuclear Research, known as CERN (/sɜːrn/; French pronunciation: [sɛʁn]; Organisation européenne pour la recherche nucléaire), is an intergovernmental organization that operates the largest particle physics laboratory in the world. Established in 1954, it is based in Meyrin, western suburb of Geneva, on the France–Switzerland border. It comprises 24 member states. Israel, admitted in 2013, is the only non-European full member. CERN is an official United Nations General Assembly observer."
gibberish_text = "hjfkjahs29134gkjh4gt21746827g"

from cleanlab.lexical_analysis.readability import ReadabilityPredictor
r = ReadabilityPredictor('DistilBERT')

r.compute_readability(ugly_sentence)
>>> 65.43140622476737

r.compute_readability(nice_sentence)
>>> 67.73471087217331

r.compute_readability(gibberish_text)
>>> 47.66284629702568
```


### Grammer score
```python
ugly_sentence = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
nice_sentence = "The European Organization for Nuclear Research, known as CERN (/sɜːrn/; French pronunciation: [sɛʁn]; Organisation européenne pour la recherche nucléaire), is an intergovernmental organization that operates the largest particle physics laboratory in the world. Established in 1954, it is based in Meyrin, western suburb of Geneva, on the France–Switzerland border. It comprises 24 member states. Israel, admitted in 2013, is the only non-European full member. CERN is an official United Nations General Assembly observer."

from cleanlab.lexical_analysis.grammar_quality import GrammarChecker
gc = GrammarChecker()

gc.check_grammar(ugly_sentence)
>>> 0.014834205933682374

gc.check_grammar(nice_sentence)
>>> 0.030710172744721688
```

### Coherence

```python
ugly_sentence = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
nice_sentence = "The European Organization for Nuclear Research, known as CERN (/sɜːrn/; French pronunciation: [sɛʁn]; Organisation européenne pour la recherche nucléaire), is an intergovernmental organization that operates the largest particle physics laboratory in the world. Established in 1954, it is based in Meyrin, western suburb of Geneva, on the France–Switzerland border. It comprises 24 member states. Israel, admitted in 2013, is the only non-European full member. CERN is an official United Nations General Assembly observer."


from cleanlab.lexical_analysis.coherence import GensimCoherence
from cleanlab.lexical_analysis.coherence import Coherence
c = Coherence()
g = GensimCoherence()

g.score(nice_sentence)
>>>0.9148681274464294

g.score(ugly_sentence)
>>> 0.821032320139112

c.score(nice_sentence)
>>> 0.8922893

c.score(ugly_sentence)
>>> 0.83343446
```


### SpellingChecker

```python

wrong_spelling = "The bueatiful garden was filled with flours of every color, their fragrant scent drifted through the air, attracting bumblebees and other insectes. Each bloom was unique, showcasing a stunning array of petells that danced gently in the breeze. The vibrant yellows, reds, and purples created a visual symphony that captivated all who visited. Children ran around, playing hide-and-seek among the foliage, while adults relaxed on the benches, soaking in the serene ambiance. As the sun set, the sky turned a magnificent shade of oranj, completing the picturesque scene that would remain in their memmories for years to come."
correct_spelling = "The beautiful garden was filled with flowers of every color, their fragrant scent drifted through the air, attracting bumblebees and other insects. Each bloom was unique, showcasing a stunning array of petals that danced gently in the breeze. The vibrant yellows, reds, and purples created a visual symphony that captivated all who visited. Children ran around, playing hide-and-seek among the foliage, while adults relaxed on the benches, soaking in the serene ambiance. As the sun set, the sky turned a magnificent shade of orange, completing the picturesque scene that would remain in their memories for years to come."

s = SpellingChecker(weight = 5)

s.score(wrong_spelling)
>>> 0.3404121699482067

s.score(correct_spelling)
>>> 0.4101463806480264
```



## Limitations and score of improvement
1. The algorithms that I used for calculating lexical score can be significantly improved via more research, re formulation of heuristic approach or simply by fine tuning or training transformer based models with more data
2. This `lexical_analysis` submodule could have been be well integrated with the `classification.CleanLearning` class, to automatically eliminate text examples if they are not of good quality.
3. Allow users to bring their own models, make the submodule plug and play by enabling users tp override of model names.
4. Instead of using transformer models directly look into classical NLP based lexical analysis approach, that can significantly improve the processing time and make the package scalable.
5. Add test cases and examples for the `lexical_analysis` submodule.
