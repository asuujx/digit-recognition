# Digit Recognition

A handwritten digit recognizer that lets you draw a digit in the browser and
classifies it against the [MNIST](http://yann.lecun.com/exdb/mnist/) dataset
using a fuzzy-set nearest-neighbor algorithm (no neural network / ML
framework involved).

## How it works

1. **Frontend** — a 28×28 pixel grid in the browser. You draw a digit by
   clicking/dragging over the cells. On submit, the grid is serialized into a
   28×28 pixel frame and sent to the backend.
2. **Backend** — a small Express.js server that receives the frame, writes it
   to `python/sample.json`, and spawns a Python process to classify it.
3. **Classifier** — a Python script:
   - Loads a subset of the MNIST training set (`limit` samples per digit,
     0–9).
   - **Normalizes** every pixel to a binary value (`0` or `1`) by
     thresholding at half of the maximum pixel value ([process_data.py](python/process_data.py)).
   - Computes a **fuzzy Hamming distance** between the drawn sample and every
     training sample ([fuzzy_set.py](python/fuzzy_set.py)).
   - Returns the label of the **closest match** (1-nearest-neighbor).
   - The normalized training set is cached to `mnist_train_norm.csv` (with
     the limit used stored in `lastlimit.txt`) so it doesn't need to be
     re-normalized on every request if the limit hasn't changed.
4. The predicted digit is sent back to the backend, then to the frontend, and
   displayed on screen.

## Project structure

```text
.
├── frontend/          # Vanilla HTML/CSS/JS drawing UI
│   ├── index.html
│   ├── app.js
│   └── style.css
├── backend/            # Express.js API that bridges frontend <-> python
│   ├── server.js
│   └── package.json
└── python/             # MNIST loading, normalization and classification
    ├── main.py          # Entry point, invoked as: python main.py <limit>
    ├── load_data.py      # Loads/limits the MNIST training set + sample
    ├── process_data.py   # Binarizes pixel values
    ├── fuzzy_set.py       # Hamming-distance classification
    └── helpers.py          # Caches the last used sample limit
```

## Requirements

- [Node.js](https://nodejs.org/) and [Yarn](https://yarnpkg.com/)
- [Python 3](https://www.python.org/) with [pandas](https://pandas.pydata.org/)
  installed (`pip install pandas`)

## Setup

### 1. Dataset

Download the MNIST training set as CSV: [mnist_train.csv](https://www.kaggle.com/datasets/oddrationale/mnist-in-csv)

Place `mnist_train.csv` inside the `python/` directory.

### 2. Backend

```bash
cd backend
yarn install
yarn start
```

The server starts on `http://localhost:3000`.

### 3. Frontend

Open `frontend/index.html` directly in a browser, or serve the `frontend/`
directory with any static file server.

## Usage

1. Draw a digit on the grid (click or click-and-drag).
2. Set the **Limit** — the number of training samples used *per digit
   class* (0–9). Higher values improve accuracy but increase classification
   time, since every sample is compared against the drawing.
3. Click **Compute Data** to classify the drawing, or **Clear** to reset the
   grid.

## Notes

- Changing the limit forces the training set to be re-normalized and
  re-cached the next time you classify.
- The classifier is a simple fuzzy-set / Hamming-distance 1-NN model, not a
  trained neural network — accuracy depends heavily on the chosen limit and
  how closely your drawing matches the binarized MNIST samples.
