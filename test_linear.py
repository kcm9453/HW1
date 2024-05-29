'''
문제 2
* 신호를 입력받아 주어진 함수가 선형인지 비선형인지 검증하는 함수를
  만들어라
* 함수의 입력은 두 개의 입력값 x1,x2 그리고 a,b로 주어진다
'''

import numpy as np
import matplotlib.pyplot as plt

# 테스트를 하는 함수 생성

def test_system(function, x1, x2, a, b):
    # 선형인지 아닌지 판단하는 판별식
    output1 = a * function(x1) + b * function(x2)
    output2 = function(a*x1 + b*x2)

    if np.allclose(output1, output2, atol=1e-8):
        print("선형")

    else:
        print("비선형")


    input = np.linspace(-10, stop : 10, num : 400)
    output = function(input)

    plt.figure(figsize = (8,4))
    plt.plot(input, output,
             label=f'{function.__name__} outputs')
    plt.scatter([x1, x2, a *x1 + b * x2],
                [function(x1), function(x2),
                 function(a * x1 + b * x2)]





