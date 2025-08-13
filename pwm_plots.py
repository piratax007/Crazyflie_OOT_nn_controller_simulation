import pandas as pd
import matplotlib.pyplot as plt

firmware_df = pd.read_csv('pwm_log.csv')
gympybullet_pwm0_df = pd.read_csv('gympybullet_data/pwm0-0.csv', header=None, names=['time', 'pwm0'])
gympybullet_pwm1_df = pd.read_csv('gympybullet_data/pwm1-0.csv', header=None, names=['time', 'pwm1'])
gympybullet_pwm2_df = pd.read_csv('gympybullet_data/pwm2-0.csv', header=None, names=['time', 'pwm2'])
gympybullet_pwm3_df = pd.read_csv('gympybullet_data/pwm3-0.csv', header=None, names=['time', 'pwm3'])

firmware_df.columns = ['time', 'pwm0', 'pwm1', 'pwm2', 'pwm3']

figure, axes = plt.subplots(2, 2, figsize=(12, 8), sharex=True)

gympybullet_dataframes = [
    gympybullet_pwm0_df,
    gympybullet_pwm1_df,
    gympybullet_pwm2_df,
    gympybullet_pwm3_df
]
pwm_columns = ['pwm0', 'pwm1', 'pwm2', 'pwm3']

for idx, ax in enumerate(axes.flatten()):
    col = pwm_columns[idx]
    individual_df = gympybullet_dataframes[idx]

    ax.plot(firmware_df['time'].values, firmware_df[col].values, label=f'Firmware {col}')
    ax.plot(individual_df['time'].values, individual_df[col].values, label=f'GymPyBullet {col}', alpha=0.7)

    ax.set_title(f'Motor {idx} PWM comparison')
    ax.set_ylabel('PWM Value')
    ax.legend()

for ax in axes[1]:
    ax.set_xlabel('Time')

plt.tight_layout()
plt.show()