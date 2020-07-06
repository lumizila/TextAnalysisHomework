# TextAnalysisHomework

This is the result of the first homework on Text Analysis class. 
The objective is learning about different representation methods of documents as well as distance metrics to analyse the similarity between a pair of documents. 

Requeriments:

- Use at least 10 documents for the analysis
- Use at least 2 representation methods of documents
- Use at least 2 distance metrics

**Files of this homework**

**Input Documents**

For this homework, I created 10 text documents based on the introduction text on the following Wikipedia pages:

https://en.wikipedia.org/wiki/Cat

https://en.wikipedia.org/wiki/Lion

https://en.wikipedia.org/wiki/Horse

https://en.wikipedia.org/wiki/Fox

https://en.wikipedia.org/wiki/Shark

https://en.wikipedia.org/wiki/Eagle

https://en.wikipedia.org/wiki/Jaguar

https://en.wikipedia.org/wiki/Ant

https://en.wikipedia.org/wiki/Dolphin

https://en.wikipedia.org/wiki/Dog

The resulting text files are inside the folder "rawData".

**Metrics**

The metrics used to compare the similarities between the document files were:

- Cosine similarity, as defined in https://en.wikipedia.org/wiki/Cosine_similarity
- Sørensen–Dice coefficient, as defined in https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient

**Representation Methods**

Two representation methods were used depending on the metric.

- For calculating the Cosine similarity, I used Bag-of-Words method to represent each document
- For calculating the Sørensen–Dice coefficient, I used sets of words to represent each document. all the words were converted to lowercase. There was no repetition of words inside each set. 

In the preprocessing stage, the texts were treated almost equally between the two representation methods:

- All words were converted to lowercase
- Symbols such as: ? ! . , were removed
- Newlines were substituted by spaces
- For calculating Sørensen–Dice coefficient repeated words inside each document were also removed

**Execution Results**

For this homework, I decided to compare the text describing a "cat" with that of other animals. 

The Cosine similarity is calculated by running the code with the command
```
python3 CosSimi.py
```

The Cosine similarity output can be seen below:

```
Sorting the cosine similarity in descending order, we have the result:
('cat', 1.0000000000000002)
('jaguar', 0.6670723700389919)
('lion', 0.6583253650631811)
('horse', 0.6348214818734654)
('shark', 0.6164683435990742)
('ant', 0.605652919648376)
('dog', 0.6036266726274103)
('dolphin', 0.5964125973529019)
('fox', 0.5366422245861782)
('eagle', 0.49714091545049294)
```

The Sørensen–Dice coefficients are calculated by running the code with the command
```
python3 SoreDice.py 
```
The Sørensen–Dice coefficients for each pair can be seen below:

```
Sorting the coefficient in descending order, we have the result:
('cat', 1.0)
('horse', 0.23556581986143188)
('lion', 0.235)
('dog', 0.22875816993464052)
('shark', 0.2140845070422535)
('jaguar', 0.2099125364431487)
('dolphin', 0.2079207920792079)
('fox', 0.19269102990033224)
('ant', 0.18912529550827423)
('eagle', 0.12931034482758622)
```

**Discussion**


As seen by the results of the execution, Cosine Similarity performed way better according to my expectations. 

**Code to the programs**
The code can be found on 
