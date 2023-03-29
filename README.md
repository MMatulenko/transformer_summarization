# XSum Text Summarization

This project uses a T5 Seq2Seq model to perform text summarization on the XSum dataset. The code is provided as a Colab notebook.

## Usage

To use this code, simply open the xsum_text_summarization.ipynb notebook file in a GitHub repository and click on the "Open in Colab" button. This will open the notebook in a new Colab environment, where you can run the code and explore the results.

The notebook loads the XSum dataset, preprocesses the data, and trains a T5 Seq2Seq model to perform text summarization. The code also includes a summarize() function that can be used to summarize new documents using the trained model.

## Results
The pretrained T5 models (t5-small and t5-base) show good performance on sentence summarization from the XSum dataset. As shown in the example summarization, the summarized sentences are not identical for all models. The pipeline shows identical summarization, but with an additional sentence. The pipeline's behavior can be adjusted with min_length and max_length parameters to control the length of the summary. However, the BLEU score of the pipeline with min_length=32 and max_length=64 is lower than that of the T5 Seq2Seq models. Additional training can improve the model's performance.

## Acknowledgments
This project was created with the help of the Hugging Face Transformers library and the XSum dataset. Thanks to the contributors of these resources for making this project possible.

## Installation

To install the dependencies for the project, you can run:

```python 
pip install -r requirements.txt
```

You can also include the setup.py file in your repository, and users can install the project by running:

Copy code

```python
pip install .
```
in the project directory.

In your README file, you can include the following instructions for installing and using the project:


To install the project, clone the repository and install the required dependencies:

bash

```python
git clone https://github.com/MMatulenko/transformer_summarization.git
cd transformer_summarization
pip install -r requirements.txt
```

## Usage
To use the project, simply run the xsum_text_summarization.ipynb notebook file in a Jupyter environment. The notebook includes all the code needed to preprocess the XSum dataset, train a T5 Seq2Seq model, and perform text summarization.

You can also use the summarize() function to summarize new documents using the trained model. Simply provide the document as input to the function, and it will return the summarized text.
