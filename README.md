# SDMRL

<h1 align="center">
  <br>
Technion Sequential Decision Making and Reinforcement Learning (Fall 2024-2025)
  <br>
  <br>
  <img src="https://jingjingrenabc.github.io/ultrapixel/images/55pick_23.jpg?raw=true">
</h1>
  <p align ="center">
    <a href="mailto:sarahk@cs.technion.ac.il">Sarah Keren</a> 

  <p align="center">
    <a href="mailto:itaysegev@campus.technion.ac.il">Itay Segev</a> •
    <a href="mailto:yuval.goshen@campus.technion.ac.il">Yuval Goshen</a>
  </p>

Jupyter Notebook tutorials for the Technion's CS 236018 course Sequential Decision Making and Reinforcement Learning

<h4 align="center">
    <a href="https://colab.research.google.com/github/CLAIR-LAB-TECHNION/CLAI"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
    <a href="https://nbviewer.org/github/CLAIR-LAB-TECHNION/CLAI/tree/main/tutorials/"><img src="https://github.com/CLAIR-LAB-TECHNION/CLAI/blob/main/tutorials/assets/nbviewer_badge.svg" alt="Open In NBViewer"/></a>
</h4>


- [SDMRL](#SDMRL)
  * [Agenda](#agenda)
  * [Running The Notebooks](#running-the-notebooks)
    + [Running Online](#running-online)
    + [Running Locally](#running-locally)
  * [Installation Instructions](#installation-instructions)
    + [Libraries to Install](#libraries-to-install)


## Agenda 


|File       | Topics Covered |
|----------------|---------------|
|`Setting Up The Working Environment.pdf`| Guide for installing Anaconda locally with Python 3 and PyTorch, integration with PyCharm and using GPU on Google Colab |-|
|`tutorials//notebooks/Tools_tutorial/Jupyter101.ipynb`| Basic introduction to Jupyter Notebooks, covering essential features like creating and running cells, and writing markdown for documentation.|
|`tutorials//notebooks/Tools_tutorial/PytorchFundamentals.ipynb`| Basic of PyTorch, focusing on tensor operations, neural network construction, and training models.|
|`tutorials//notebooks/Tools_tutorial/Gymnasium.ipynb`| Using Gymnasium for creating and interacting with reinforcement learning environments, including setting up environments, running simulations, and implementing agents.|
|`tutorials//notebooks/Tools_tutorial/PettingZooDemo.ipynb`| Demonstration of the PettingZoo library for multi-agent reinforcement learning, covering environment setup, interaction, and agent implementation.|
|`tutorials//notebooks/Tools_tutorial/StableBaselines.ipynb`| Overview of the Stable Baselines3 library for reinforcement learning, covering setup, training, and evaluation of RL models.|
|`tutorials/notebooks/Imitation-learning_tutorial`| Tutorials on imitation learning techniques.|
|`tutorials/notebooks/Planning_tutorial`| Tutorials on planning algorithms in reinforcement learning.|
|`tutorials/notebooks/Policy-Gradient_tutorial`| Tutorials on policy gradient methods in reinforcement learning.|
|`tutorials/notebooks/Value-Based_tutorial`| Tutorials on value-based methods in reinforcement learning.|
|`tutorials/notebooks/DQN_tutorial`| Tutorials on Deep Q-Networks (DQN) in reinforcement learning.|
|`tutorials/notebooks/Actor-Critic_tutorial`| Tutorials on Actor-Critic methods in reinforcement learning.|
|`tutorials/notebooks/Model-Based_tutorial`| Tutorials on model-based reinforcement learning methods.|
|`tutorials/notebooks/MARL_tutorial`| Tutorials on Multi-Agent Reinforcement Learning (MARL).|

## Running The Notebooks
You can view the tutorials online or download and run locally.

### Running Online

|Service      | Usage |
|-------------|---------|
|Jupyter Nbviewer| Render and view the notebooks (can not edit) |
|Google Colab| Render, view, edit and save the notebooks to Google Drive (limited time) |


Jupyter Nbviewer:

[![nbviewer](https://github.com/CLAIR-LAB-TECHNION/CLAI/blob/main/tutorials/assets/nbviewer_badge.svg)](https://nbviewer.org/github/CLAIR-LAB-TECHNION/CLAI/tree/main/tutorials/)


Press on the "Open in Colab" button below to use Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CLAIR-LAB-TECHNION/CLAI)


### Running Locally

Press "Download ZIP" under the green button `Clone or download` or use `git` to clone the repository using the 
following command: `git clone https://github.com/CLAIR-LAB-TECHNION/CLAI.git` (in cmd/PowerShell in Windows or in the Terminal in Linux/Mac)

Open the folder in Jupyter Notebook (it is recommended to use Anaconda). Installation instructions can be found in `Setting Up The Working Environment.pdf`.


## Installation Instructions

For the complete guide, with step-by-step images, please consult `Setting Up The Working Environment.pdf`

1. Get Anaconda with Python 3, follow the instructions according to your OS (Windows/Mac/Linux) at: https://www.anaconda.com/download
2. Install the basic packages using the provided `environment.yml` file by running: `conda env create -f environment.yml` which will create a new conda environment named `CLAI`. If you did this, you will only need to install PyTorch, see the table below.
3. Alternatively, you can create a new environment for the course and install packages from scratch:
In Windows open `Anaconda Prompt` from the start menu, in Mac/Linux open the terminal and run `conda create --name CLAI`. Full guide at https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands
4. To activate the environment, open the terminal (or `Anaconda Prompt` in Windows) and run `conda activate CLAI`
5. Install the required libraries according to the table below (to search for a specific library and the corresponding command you can also look at https://anaconda.org/)

### Libraries to Install

|Library         | Command to Run |
|------------------|---------|
|`Jupyter Notebook`|  `conda install -c conda-forge notebook`|
|`numpy`|  `conda install -c conda-forge numpy`|
|`matplotlib`|  `conda install -c conda-forge matplotlib`|
|`tqdm`| `conda install -c conda-forge tqdm`|
|`gymnasium`| `pip install gymnasium`|
|`pettingzoo`| `pip install pettingzoo`|
|`stable-baselines3`| `pip install stable-baselines3`|
|`pytorch` (cpu)| `conda install pytorch torchvision torchaudio cpuonly -c pytorch` (<a href="https://pytorch.org/get-started/locally/">get command from PyTorch.org</a>)|
|`pytorch` (gpu)| `conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia` (<a href="https://pytorch.org/get-started/locally/">get command from PyTorch.org</a>)|



5. To open the notebooks, open Ananconda Navigator or run `jupyter notebook` in the terminal (or `Anaconda Prompt` in Windows) while the `CLAI` environment is activated.

<br>
<br>

<img src="https://github.com/CLAIR-LAB-TECHNION/CLAI/blob/main/tutorials/assets/CLAI_house_image.png?raw=true">
