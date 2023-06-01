# digit-recognition

## Requirements

`Docker` must be installed on local machine. [Link](https://www.docker.com/)
~~`Node.js` and `Python` must be installed on local machine.~~

## Installation

### Step 1 (dataset)

Download MNIST dataset. [Link](https://www.kaggle.com/datasets/oddrationale/mnist-in-csv)
Put `mnist_train.csv` inside `shared` directory.

### Step 2 (containers)

1. Open terminal inside main directory (where docker-compose.yaml is located)
2. Run `docker compose up` command
3. After ~10 seconds all containers should be ready
   To stop and remove all containers run `docker compose down` command

### Step 3 (frontend)

1. Open `index.html` inside `frontend` directory or run a local webserver.
2. Try it out.
