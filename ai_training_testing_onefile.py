from stable_baselines3 import PPO, A2C

import TouchBall1

import threading

class AITesting():
    def __init__(self, model_path, env):
        self.model = PPO.load(model_path, env=env)
    def recieved_field_data(self, field):
        action, _state = self.model.predict(field)
        return action, _state

def AITraining():
    def __init__(self):
        env = TouchBall1()
        self.model = A2C("MultiInputPolicy", env, verbose=1, device='cuda')
        self.model.learn(100000)
    def recieved_field_data(self, field):
        self.field = field
    def callback_get_obs(self):
        return self.field
    