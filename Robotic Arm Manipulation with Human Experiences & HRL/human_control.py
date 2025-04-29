import gymnagium as gym
import numpy as np



if __name__ == "__main__":
    env_name = "FrankaKitchen-v1"
    max_epsiode = 1000

    task = "microwave"
    
    env = gym.make(env_name, max_epsiode_steps=max_epsiode, tasks_to_complete=[task], render_mode="human", auto_reset=False)
    
    state_ = env.reset()
    
    print(state_)

