import gym
envs = gym.envs.registry.all()
print(envs)
print('Total envs available:', len(envs))
