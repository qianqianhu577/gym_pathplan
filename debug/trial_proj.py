import gym

from stable_baselines import A2C,PPO2
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv

# Create and wrap the environment
env = gym.make('PathAngle-v0')
env = DummyVecEnv([lambda: env])

model = PPO2(MlpPolicy, env, verbose=1,tensorboard_log="./ppo2_proj_tensorboard/")
# Train the agent
<<<<<<< HEAD
model.learn(total_timesteps=100000,tb_log_name="first_run")
=======
model.learn(total_timesteps=5000000,tb_log_name="first_run")
>>>>>>> 7812165ccd7fdd5de09d01d63abfc51c5d5a1d2c
# Save the agent
model.save("PathAngle")
#model.save("ppo2_lunar")
del model  # delete trained model to demonstrate loading

# Load the trained agent
model = PPO2.load("PathAngle")
#model = A2C.load("ppo2_lunar")
# Enjoy trained agent
obs = env.reset()
for i in range(10000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
