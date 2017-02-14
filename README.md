# FancyRecommenderSystem

- This tiny system is made to work with OpenFoodFacts.org data.
- It provides a WebSocket interface to retrieve similar products given a selection.
- The WebSocket API receives a product and returns all similar products.
- The Engine is based on a graph structure that computes similarity using TF-IDF/Jaccard Index based on semantic data of the products instead of ratings.

```
pip install -r requirements.txt
```
