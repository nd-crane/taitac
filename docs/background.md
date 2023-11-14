## Starting Use Case for AI Curator -- CSV Column Type Annotation
[Column Type Annotation using ChatGPT](https://arxiv.org/abs/2306.00745) is a novel approach to annotate the semantic types of table columns using a large language model (LLM) called ChatGPT¹[1]. The proposed method is based on the idea that a language model can be used to generate natural language descriptions of table columns, which can then be used to infer their semantic types. The method is evaluated on the WikiTableQuestions dataset²[2] and achieves state-of-the-art performance in zero-shot and few-shot settings.

- **Column Type Annotation using ChatGPT**: A novel approach to annotate the semantic types of table columns using a large language model (LLM) called ChatGPT¹[1].
- **Prompt Design and Evaluation**: Different ways to formulate prompts for the column type annotation (CTA) task and their performance in zero- and few-shot settings.
- **Explicit Instructions and Message Roles**: How to improve the performance of ChatGPT by providing step-by-step instructions and using message roles to distinguish between system, user, and AI messages²[2].
- **In-Context Learning**: How to further boost the performance of ChatGPT by providing task demonstrations as part of the prompt in one-shot and five-shot setups.
- **Two-Step Pipeline**: A proposed method to deal with large label spaces by first predicting the domain of the table and then using only the relevant subset of labels for CTA³[3].
- **Comparison to Baselines**: A comparison of ChatGPT to state-of-the-art CTA methods based on pre-trained language models (PLMs) such as RoBERTa and DODUO.

## CSV Datasets for AI Curator
[SOTAB V2 - Table Annotation Benchmark](http://webdatacommons.org/structureddata/sotab/v2/) Code for constructing the benchmark: (https://github.com/wbsg-uni-mannheim/wdc-sotab):
[GitTables: a large-scale corpus of relational tables download.](https://gittables.github.io/)
[GitTables: A Large-Scale Corpus of Relational Tables](https://arxiv.org/pdf/2106.07258.pdf) -- [GitHub](https://github.com/madelonhulsebos/gittables)
[GitTables Download](https://zenodo.org/records/4943312)

- **SOTAB V2**: A benchmark for **table annotation** using **Schema.org** and **DBpedia** terms. It covers two tasks: **Column Type Annotation (CTA)** and **Columns Property Annotation (CPA)**¹[1]. It consists of **45,834 tables** annotated for CTA and **30,220 tables** annotated for CPA from **55,511 websites**²[2].
- **Table annotation tasks**: The goal of CTA is to assign a type to each table column, such as telephone, Duration, or Organization³[3]. The goal of CPA is to assign a property to each pair of columns, such as gtin, startDate, or recipeIngredient⁴[4].
- **Table annotation challenges**: The benchmark includes subsets of test tables that measure the performance of table annotation systems on specific challenges, such as missing values, value format heterogeneity, and corner cases.
- **Baseline methods**: Three methods are used to evaluate the benchmark: a non-deep learning method based on TF-IDF and Random Forest, a deep learning method called TURL that uses Transformer and TinyBERT, and a deep learning method called DODUO that uses BERT and table serialization.
- **Download and code**: The benchmark datasets and the code for building the benchmark are available for public download on github⁵[5]. The datasets are provided in JSON and CSV formats.