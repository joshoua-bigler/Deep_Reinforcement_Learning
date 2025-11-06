import matplotlib.pyplot as plt
from time import sleep
from matplotlib import animation
from IPython.display import clear_output


def run_animation(experience_buffer):
  time_lag = 0.05 
  for experience in experience_buffer:
    clear_output(wait=True)
    plt.imshow(experience['frame'])
    plt.axis('off')
    plt.show()
    print(f'Episode: {experience['episode']}/{experience_buffer[-1]['episode']}')
    print(f'Epoch: {experience['epoch']}/{experience_buffer[-1]['epoch']}')
    print(f'State: {experience['state']}')
    print(f'Action: {experience['action']}')
    print(f'Reward: {experience['reward']}')
    sleep(time_lag)


def store_episode_as_gif(experience_buffer, path='./gifs/', filename='animation2.gif'):
  ''' Store episode as a gif animation. '''
  fps = 5  # Set framew per seconds
  dpi = 30  # Set dots per inch
  interval = 50  # Interval between frames (in ms)
  frames = []
  for experience in experience_buffer:
    frames.append(experience['frame'])
  plt.figure(figsize=(frames[0].shape[1] / dpi, frames[0].shape[0] / dpi), dpi=dpi)
  patch = plt.imshow(frames[0])
  plt.axis('off')
  def animate(i):
    patch.set_data(frames[i])
  anim = animation.FuncAnimation(plt.gcf(), animate, frames=len(frames), interval=interval)
  anim.save(path + filename, writer='imagemagick', fps=fps)


def gif(agent, name: str, num_episodes: int = 1):
  ''' Function to run agent in environment and store results as gif animation '''
  num_epochs = 0
  total_failed_deliveries = 0
  experience_buffer = []
  store_gif = True
  for episode in range(1, num_episodes + 1):
    my_env = agent.env.reset()
    state = my_env[0]
    epoch = 1
    num_failed_deliveries = 0
    cum_reward = 0
    done = False
    while not done:
      action = agent.get_action(state)
      state, reward, t1, t2, _ = agent.env.step(action)
      done = t1 or t2
      cum_reward += reward
      if reward == -10:
        num_failed_deliveries += 1
      experience_buffer.append({
          'frame': agent.env.render(),
          'episode': episode,
          'epoch': epoch,
          'state': state,
          'action': action,
          'reward': cum_reward
      })
      epoch += 1
    total_failed_deliveries += num_failed_deliveries
    num_epochs += epoch
    if store_gif:
      store_episode_as_gif(experience_buffer, filename=f'{name}.gif')
  run_animation(experience_buffer)
  print('\n')
  print(f'Test results after {num_episodes} episodes:')
  print(f'Mean # epochs per episode: {num_epochs / num_episodes}')
  print(f'Mean # failed drop-offs per episode: {total_failed_deliveries / num_episodes}')