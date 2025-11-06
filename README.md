Deep reinforcement learning applied to the Taxi and CarRacing environments from [Gymnasium](https://gymnasium.farama.org/).

# Setup
In order to run the [deep_reinforcement_learning.ipynb](notebooks/deep_reinforcement_learning.ipynb) notebook you need to setup the virtual environment and install the required packages. 
You can do this by running the following commands from the **root** of the repository:
```bash
python -m venv venv
venv\Scripts\activate
pip install -e .
```

In order to run torch with CUDA support you need to install the appropriate version of [torch](https://pytorch.org/get-started/locally).
```bash
pip3 install torchvision torchaudio --index-url https://download.pytorch.org/whl/cu<version>
```