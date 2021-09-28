Title: Maintainable Machine Learning Code
Date: 2017-11-26
Category: Programming
Tags: MachineLearning, Programming
Slug: ReuseableML
Authors: Ravin Kumar
Status: published 

Creating a machine learning pipeline requires almost no thought these days but 
maintaining a reusable and understandable codebase the whole way
through is much more challenging. However there are some steps and 
ideas that can be borrowed from traditional programming that are
still relevant.

## Big Ball of Mud - Machine Learning Edition

Let's say you're starting out with Machine Learning and 
*you need an immediate fix for a small problem, or a quick prototype or proof of concept*.
Easy, below is a sample program to make predictions on the Iris dataset

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
iris_csv = ("https://raw.githubusercontent.com/"
             "uiuc-cse/data-fa14/gh-pages/data/iris.csv")
df = pd.read_csv(iris_csv)
y = LabelEncoder().fit_transform(df[species])
df = df.drop("species", axis=1)
clf = RandomForestClassifier()
clf.fit(df, y).predict(df)
```
Even to non programmers the above lines of code are pretty easy to read.
It's simple enough to just put that into a python script in some
directory with the data files next to it and start churning out predictions.

Later on you realize there's some steps you can do to make your model better.
It starts off innocently enough, perhaps just one line to normalize
the features, maybe a loop to perform cross validation
but within a couple of hours you'll end up with one large python
script that has true false statements all over the place, code chunks
that are commented out, and incoherent comments all over the place. Suddenly
the *piecemeal growth* of our project dawns on you.

Hopefully you're using version control but even then all your code commits will be
on the master branch with commit messages like "model 1" or "added pickling column".
You'll find some features are engineered off other features, or 
portions of your code relied on a datatype coercion you made somewhere between
the third and sixth commit. As your code progresses
*Different artifacts change at different rates* and you're trying
to remember which processing steps were required to run one of the predictions
you had that other day.

*Your code is now a [Big Ball of Mud](http://www.laputan.org/mud/).* Big Ball of
Mud is an excellent paper written in 1999 about what happens when code
is haphazardly written. The paper is still relevant today, with all the
text in italics copied and pasted straight from the paper. At
the core the paper is warning us that if architecture is not persistently considered
the final code base will become unmaintainable that it will eventually need to be 
totally torn down.
Unfortunately this is how I've seen so many machine learning implementations turn out.
The issue is present even at large companies like [Uber]("https://eng.uber.com/michelangelo/")
who have built dedicated platforms for creating maintainable machine learning
pipelines.

Even if you're just writing code for yourself there's still benefits intentionally
writing your code in a reusable way. You'll be able to iterate faster,
structure your experiments, and be able to revisit your code with minimal effort
later on. 

# General approaches
With some experimentation I've been able to find an approach that works for me.

## Start with a package
Whether you're using R, Python, or any other language really, study up
on what is typically done to package the code. 

With Python I immediately do four things at a minimum  

* Create a requirements.txt or environment.yml file  
* Create a source code directory  
* Write a README.md  
* Initialize a git repo and commit everything  

These are the minimum steps for reproducibility. Imagine how hard it would be
if someone handed you a flash drive full of Python files. How do you know
what is required to run it, or what packages are needed? Rather
than worry if they were using Python 2 or 3, or pandas .19, etc 
With these four basic steps you're guaranteeing that the environment
is reproducible.

A great tool that helps with this is CookieCutter templates,
specifically this [Data Science Template](https://github.com/drivendata/cookiecutter-data-science)
It's got even more than detailed here but really will make setting up a reusable
package easy.

## Write a library for reusable components of your code
Don't put everything in your main.py file. For code that loads datasets,
or writes predictions to a file, write a package that lets you abstract
that away from your machine learning code. Although it takes more 
effort up front, later on it means your actual prediction script
will be much easier to read.

In the example above we can write a function that looks like this
```python
def load_iris():
    """Loads iris dataset from github and returns (df,y_raw)"""
    iris_csv = ("https://raw.githubusercontent.com/"
                "uiuc-cse/data-fa14/gh-pages/data/iris.csv")
    df = pd.read_csv(iris_csv)
    y_raw = df["species"]
    df = df.drop("species", axis=1)
    return df, y_raw
```
Doing this has multiple benefits, if written in the package you can import
this into any script without any duplication. It also clearly demarcates
that this set of code has no dependencies on other lines.

## Use a testing package
Unittests are still relevant with machine learning code. You can use
tests for your own code. There are many examples of 
[test driven development](https://www.google.com/search?q=test+driven+development).
However I also use tests to test my own understanding of how machine
learning libraries work. By writing the following tests I can double-check
my understanding of word lemmatizers and CountVectorizer in scikit-learn.

```python
def test_lemmatization():
    """Test that Lemmatizer works"""
    wnl = WordNetLemmatizer()
    assert wnl.lemmatize('dogs') == 'dog'


def test_lemmatization_with_countvectorizer():
    """Test Lemmatization with Stop Words removal"""
    strings = ["I like Dogs and", "I like Churches and"]
    count = CountVectorizer(tokenizer=lemmatizer, stop_words='english')
    count.fit(strings)
    assert {'church', 'dog', 'like'} == set(count.get_feature_names())
```
It's not about my doubt that the code is implemented poorly, but moreso
to double check and reinforce my own understanding. By writing series
of these tests I find that I both understand what other libraries are doing and
that I double check my understanding fundamentals of the theory.

# Scikit-learn specific
If you use scikit there are some additional tools that are helpful.
scikit-learn itself is written in a way that makes machine learning composable.
It's so good that other non scikit-learn libraries
tend to build similar APIs to maintain compatibility, for example XGBoost
implements a scikit-learn abstraction layer.

## Use pipelines
scikit-learn makes it very easy to tie data processing steps together, without
storing intermediate results. It also makes it easy to turn off
or turn on portions of your pipeline without having to comment entire
blocks of code. And lastly it makes it very easy to use parameter grid searches
and cross validation in one or two lines.

## Write your own predictors and transformers
Most of the time however data will require some data munging before
scikit-learns transformers and predictors can use it. For these activities
scikit-learn provides all the scaffolding you need 
[in its base module](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.base)
By utilizing these it keeps you within the pipeline framework which
again makes it easy to use all the built-in tools for experimentation.

For example here is an implementation of a transformer I used in a Natural 
Language Processing Problem that found word count and string length for a given string.
```python
class TextTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, features):
        """Takes column of text and returns back array of features. Features list is specified by features
        Parameters
        ----------
        features : iter
            Iterable of features strings that correspond to class
        """

        self.features = features
        return

    def fit(self, X, y):
        return self

    def transform(self, X):
        """Accepts Pandas Series and returns back a dataframe where each column is a feature"""

        if self.features is None:
            raise ValueError("Features must be a list of features that will be used in this model")

        features = pd.DataFrame()

        for feature in self.features:
            transformer = getattr(self, feature)
            col = transformer(X)

            features[feature] = col

        return features.values

    @staticmethod
    def word_count(X):
        """Count the number of words in each string"""
        return X.apply(lambda x: len(x.split(" ")))

    @staticmethod
    def sentence_length(X):
        """Get the length of the string for each author"""
        return X.apply(lambda x: len(x))
```
While seemingly verbose, if using packages in my machine learning code
this entire feature processing portion of logic looked like this

```python
features = FeatureUnion(
    [
    ('basic_preprocessing', TextTransformer(features=['word_count', 'sentence_length'])),
    ("tfidf", TfidfVectorizer())
    ]
)
```
It made it dead simple for me to add or remove features with just one
line of code, making my experimentation and feature selection process
that much quicker.

## Conclusion
It's very much worth the effort to spend the extra effort to make your 
machine learning code be more like a package and less like a script.
You'll save anyone using your code time figuring out how to reproduce your 
results, but you'll also save yourself a bunch of time also trying to 
reproduce your results! The extra effort goes a long way in protecting
your sanity and also ensuring you're able to build more than just a prototype
prediction engine.


