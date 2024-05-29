'''
문제 1번
* 5Hz의 최대 주파수를 가지는 연속 신호를
* 서로 다른 샘플링 주파수를 사용하여 이 신호를 샘플링
* 원본신호 : 5Hz의 최대 주파수를 가진 사인파, 1초 동안 1000개의
  포인트로 만듬
* 샘플링 주파수는 각 2 F_max, 2,4, F_max, 1,6 F_max
'''

import numpy as np
import matplotlib.pyplot as plt

f_max = 5 # 5Hz
# 1초를 1000등분해서 시간 공간을 만들어 준다.

t = np.linspace(start : 0, stop : 1, num = 1000, endpoint = False)
#원본 신호 설정
#2*pi*f*t
continuous_signal = np.sin(2*np.pi*f_max*t)
#sampling frequency
sampling_Frequencies = [2*f_max, 2.4*f_max, 1.6 * f_max]

#가상의 공간을 나누는 작업이전에 큰 공간을 만듬

plt.figure(Figsize=(12,9))
for i, fs in enumerate(sampling_Frequencies);
    smapling_inver







