# Python Samples of Image Processing

## Get Started

### How to clone on Google Colabratory

1. Vist [Google Colab site](https://research.google.com/colaboratory/).

1. Create new notebook.

1. Run the following code to mount the google drive. [More information](https://colab.research.google.com/notebooks/io.ipynb?hl=en)

```
# run once when you start the Google Colabratory session
# mount google drive
from google.colab import drive
drive.mount('/content/drive')
```

1. Run the following code to clone the samples.

```
%cd "/content/drive/MyDrive/Colab Notebooks/"
!git clone https://github.com/mastnk/GCIP
```

### How to run on Google Colabratory

```
%cd "/content/drive/MyDrive/Colab Notebooks/GCIP"
%cd 01
%python3 loadsave.py input.png
```

## 01/

- loadsave.py

- datatype.py

- resize.py


## 02/

- boxfilter.py

- gaussianfilter.py

- sobelfilter.py

- laplacianfilter.py

- DoGfilter.py

- UnsharpMask.py

