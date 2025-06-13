#  Movie Success Prediction Notebook

This notebook presents the training and evaluation of a machine learning pipeline for predicting movie success based on the [TMDB Movies Dataset](https://www.kaggle.com/datasets/juzershakir/tmdb-movies-dataset?resource=download).

##  Dataset

The dataset was sourced from Kaggle and includes metadata on thousands of movies such as cast, director, genre, budget, revenue, and textual descriptions like `overview` and `tagline`.

##  Methodology

The preprocessing pipeline combines:

-  **Structured Data Processing**: Handling of categorical and numerical features using classical ML techniques such as encoding, normalization, and statistical aggregation.
- **Textual Data Enrichment**: Feature extraction from natural language fields (`overview`, `title`, `tagline`) using NLP tools including sentiment analysis, readability scoring, and sentence embeddings.

The pipeline is fully modular, scalable, and implemented using `scikit-learn` components and custom Python functions.

##  Model

We trained a multi-output regressor based on XGBoost to predict:

-  **Viewer Rating**
-  **Adjusted revenue**

##  Results

The final model achieved the following performance:

- **Rating Prediction**: RMSE = `0.006`, R² = `0.997`
- **Revenue Prediction**: RMSE = `0.004`, R² = `0.999`

These results reflect a strong fit, driven by the integration of rich semantic features and data-driven statistical signals.


##  Notes

- No GPU is required for training or inference.
- The full training process runs in 10 - 15 minutes on a standard CPU.
- The notebook is ready for adaptation and deployment.
