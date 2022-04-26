from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
from custom_env.envs.SpaceTowerDefense import SpaceTowerDefense


class SpaceTowerDefense(Env):
    def __init__(self):
        super().__init__()

        self.pygame = SpaceTowerDefense()

        # aim left, aim right, fire
        self.action_space = Discrete(3)

        # number of asteroids
        self.observation_shape = (100,)
        self.observation_space = Box(
            low=np.ones(self.observation_shape)*-100,
            high=np.ones(self.observation_shape)*100,
            dtype=np.float16
        )

        # minute long rounds
        self.episode_length = 60

    def step(self, action):
        self.pygame.action(action)
        observation = self.pygame.observe()
        reward = self.pygame.get_reward()
        done = self.pygame.is_done()

        # return to OpenAI gym the environment, reward, status, and notes
        return observation, reward, done, {}

    def render(self):
        self.pygame.view()

    def reset(self):
        del self.pygame
        self.pygame = SpaceTowerDefense()
        observation = self.pygame.observe()
        return observation
