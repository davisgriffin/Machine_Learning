from gym.envs.registration import register

register(
    id='SpaceTowerDefense-v0',
    entry_point='custom_env.envs:CustomEnv',
    max_episode_steps=2000,
)
