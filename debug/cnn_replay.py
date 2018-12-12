import gym
import tensorflow as tf
from stable_baselines import A2C,PPO2
from stable_baselines.a2c.utils import linear
from stable_baselines.common.policies import ActorCriticPolicy, register_policy
from stable_baselines.common.vec_env import DummyVecEnv
from cnn_policy import CustomPolicy,CustomPolicy2

# Create and wrap the environment
env = gym.make('PathRandom-v0')
env = DummyVecEnv([lambda: env])
#model = PPO2(CustomPolicy, env, verbose=1,tensorboard_log="./ppo2_proj_tensorboard/")
<<<<<<< HEAD
model = PPO2.load('Pathplan_partial3', policy=CustomPolicy2)
=======
model = PPO2.load('Pathplan_static-1', policy=CustomPolicy2)
>>>>>>> 293dadf93c687995f32914f1d435a3c893243a52

obs = env.reset()

successCount = 0.0
total = 100
for i in range(total):
    while True:
        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)
        env.render()
        #time.sleep(0.1)
        if dones:
            if rewards[0] == 100.0:
                successCount += 1
            print(i,rewards[0])
            break

print("total success rate {}%".format(100.0*successCount/total))