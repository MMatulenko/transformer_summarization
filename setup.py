from setuptools import setup, find_packages

setup(
    name='xsum-text-summarization',
    version='1.0',
    description='Text summarization with T5 Seq2Seq model on the XSum dataset',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'datasets',
        'transformers',
        'rouge-score',
        'nltk',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
