import pandas as pd
import matplotlib.pyplot as plt

data = {
    'effect lvl': ['None', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    'ground_sprint': [709, 591, 506, 443, 394, 354, 323, 295, 273, 253, 236, 221],
    'vanilla_jump':  [558, 539, 519, 503, 488, 473, 458, 445, 433, 421, 410, 399],
    'fmf_jump':      [558, 426, 376, 337, 305, 262, 242, 227, 212, 190, 179, 169],
}

df = pd.DataFrame(data)
df['vanilla_jump%diff'] = round(((df['ground_sprint'] - df['vanilla_jump']) / df['ground_sprint']) * 100, 1)
df['fmf_jump%diff'] = round(((df['ground_sprint'] - df['fmf_jump']) / df['ground_sprint']) * 100, 1)

print('\n', df)

LIGHT_GREEN_RGB = (0/255, 255/255, 0/255)

plt.style.use('dark_background')
plt.figure(figsize=(10, 6))
plt.plot(df['effect lvl'], df['vanilla_jump%diff'], label='Vanilla', marker='.', color='white')
plt.plot(df['effect lvl'], df['fmf_jump%diff'], label='Fast Movement Fix', marker='.', color=LIGHT_GREEN_RGB)
plt.xlabel('Speed Effect Level', color='white')
plt.ylabel('% Speed Increase', color='white')
plt.title('% Speed increase when sprint jumping under the speed effect\n 200 blocks distance in a straight line', color='white')  # Set text color
plt.axhline(y=0, color='white', linestyle='-', linewidth=0.5, zorder=-1)
plt.legend()
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()
