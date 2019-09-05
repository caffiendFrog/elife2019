# Word2Vec Based Method

Uses word2vec to detect suggest candidate list of equipments in a body of text

# Usage instructions
- Entry point is the main.py, a body of text can be provided for the application, and the application should return a list of suggested equipments it detects

- The config.py  can be configured to change the threshold for similarity between a detected word and the words in the seed set of instruments

# Approach 
- Detects noun phrase in the given corpus, and selects the noun phrases if its similarity to the any of the equipments from the equipment list is below a threshold 
- Word2Vec is used to compute the similarity between a noun phrase and corpus of equipments
- Word2Vec used is trained on pubmed corpus, and it is available at  https://figshare.com/articles/Improving_Biomedical_Word_Embeddings_with_Subword_Information_and_MeSH_Ontology/6882647

# TODOS
- Either 
    -   Subset the used word2vec to include just terms most similar to the terms in the equipments corpus to make it more efficient
    -   Or Train new pubmed word2vec with multigrams extracted from equipment corpus
- Optimize the technique used for the  noun phrase comparision with equipment corpus

