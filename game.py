import gym
from gym.utils.play import play, PlayPlot

def callback(obs_t, obs_tp1, action, rew, done, info):
    return [rew]

plotter = PlayPlot(callback, 30 * 5, ["reward"])
env = gym.make("Breakout-ramNoFrameskip-v4")
play(env, callback=plotter.callback, zoom=4)
