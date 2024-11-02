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


###
