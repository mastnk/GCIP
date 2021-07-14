# Python Samples of Image Processing

## How to clone on Google Colabratory

1. Vist [Google Colab site](https://research.google.com/colaboratory/).

1. Create new notebook.

1. Run the following code to mount the google drive.

```
# run once when you start the Google Colabratory session
# mount google drive
from google.colab import drive
drive.mount('/content/drive')
```

[More information](https://colab.research.google.com/notebooks/io.ipynb?hl=en)

1. Run the following code to clone the samples.

```
%cd "/content/drive/MyDrive/Colab Notebooks/"
!git clone https://github.com/mastnk/GCIP
```

## How to run on Google Colabratory

```
%cd "/content/drive/MyDrive/Colab Notebooks/GCIP"
%cd 01
%python3 imshow.py input.png
```


# 01/


# 02/
