import abc
import itertools
from typing import Any
from torch import nn
from torch.nn import functional as F
from torch import optim

import numpy as np
import torch
from torch import distributions

from cs236018.infrastructure import pytorch_util as ptu
from cs236018.policies.base_policy import BasePolicy


def build_mlp(
        input_size: int,
        output_size: int,
        n_layers: int,
        size: int
) -> nn.Module:
    """
        Builds a feedforward neural network

        arguments:
            n_layers: number of hidden layers
            size: dimension of each hidden layer
            activation: activation of each hidden layer

            input_size: size of the input layer
            output_size: size of the output layer
            output_activation: activation of the output layer

        returns:
            MLP (nn.Module)
    """
    layers = []
    in_size = input_size
    for _ in range(n_layers):
        layers.append(nn.Linear(in_size, size))
        layers.append(nn.Tanh())
        in_size = size
    layers.append(nn.Linear(in_size, output_size))

    mlp = nn.Sequential(*layers)
    return mlp


class MLPPolicySL(BasePolicy, nn.Module, metaclass=abc.ABCMeta):
    """
    Defines an MLP for supervised learning which maps observations to continuous
    actions.

    Attributes
    ----------
    mean_net: nn.Sequential
        A neural network that outputs the mean for continuous actions
    logstd: nn.Parameter
        A separate parameter to learn the standard deviation of actions

    Methods
    -------
    forward:
        Runs a differentiable forwards pass through the network
    update:
        Trains the policy with a supervised learning objective
    """
    def __init__(self,
                 ac_dim,
                 ob_dim,
                 n_layers,
                 size,
                 learning_rate=1e-4,
                 training=True,
                 nn_baseline=False,
                 **kwargs
                 ):
        super().__init__(**kwargs)

        # init vars
        self.ac_dim = ac_dim
        self.ob_dim = ob_dim
        self.n_layers = n_layers
        self.size = size
        self.learning_rate = learning_rate
        self.training = training
        self.nn_baseline = nn_baseline

        self.mean_net = build_mlp(
            input_size=self.ob_dim,
            output_size=self.ac_dim,
            n_layers=self.n_layers, size=self.size,
        )
        self.mean_net.to(ptu.device) # Moves the mean_net to the specified device (CPU or GPU) for computation.
        self.logstd = nn.Parameter( # learnable parameter representing the logarithm of the standard deviation of the policy's action distribution.

            torch.zeros(self.ac_dim, dtype=torch.float32, device=ptu.device)
        ) # This ensures it will be updated during training.
        self.logstd.to(ptu.device)
        self.optimizer = optim.Adam(
            itertools.chain([self.logstd], self.mean_net.parameters()),
            self.learning_rate
        )

    def save(self, filepath):
        """
        :param filepath: path to save MLP
        """
        torch.save(self.state_dict(), filepath)

    def forward(self, observation: torch.FloatTensor) -> Any:
        """
        Defines the forward pass of the network

        :param observation: observation(s) to query the policy
        :return:
            action: sampled action(s) from the policy
        """
        observation = observation.float().to(ptu.device)
        mean = self.mean_net(observation) # Passes the observation through the mean network to compute the mean of the action distribution.
        std = torch.exp(self.logstd)
        dist = distributions.Normal(mean, std) # Creates a normal (Gaussian) distribution with the computed mean and standard deviation.
        action = dist.rsample() # returns a sample that is a function of the distribution parameters and some independent random noise, which allows gradients to propagate through the sampling process for optimization
        return action

    def update(self, observations, actions):
        """
        Updates/trains the policy

        :param observations: observation(s) to query the policy
        :param actions: actions we want the policy to imitate
        :return:
            dict: 'Training Loss': supervised learning loss
        """
        self.optimizer.zero_grad()
        action_pred = self.forward(observations)
        loss = F.mse_loss(action_pred, actions)
        loss.backward()
        self.optimizer.step()
        return {
            'Training Loss': ptu.to_numpy(loss),
        }

    def get_action(self, obs: np.ndarray) -> np.ndarray:
        obs = torch.tensor(obs, dtype=torch.float32).to(ptu.device)
        with torch.no_grad():
            action = ptu.to_numpy(self.forward(obs))
        return action
