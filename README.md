# 2DEulerianFluidSolver
A interactive demo of 2D Eulerian Fluid Solver based on Taichi Lang

这是一个使用[太极语言](https://docs.taichi-lang.org/)编程的2D欧拉流体求解器，该项目支持：

- 水面能够与鼠标进行交互
- 添加旋度运算，更好的流体表现 ：）
- 支持切换流体的背景图片（图片位于img目录下方）
- 代码简短清晰（200 lines)，方便阅读

![仿真效果](https://github.com/Lee-abcde/2DEulerianFluidSolver/blob/dev/img/cover.png)

### Demo依赖包安装

```
python version = 3.9.16
conda install taichi
conda install matplotlib
```

安装以上两个包之后，运行`main.py`即可以和demo玩耍（如果提示读入图片报错，请参照下文**切换流体初始图片**进行参考修改相对路径）

### 代码阅读指北

`scr/main.py`：流体求解器主要代码，建议先看最后的循环部分。

`src/Util.py`：双Buffer类和双线性差值函数的实现

### 如何切换流体初始图片

```
eulerSimParam = {
    'load_image':'../img/test2.jpg',
    'shape': [512, 512],
    'dt': 1 / 60.,
    'iteration_step': 20,
    'mouse_radius':0.01,# [0.0,1.0] float
    'mouse_speed': 125.,
    'mouse_respondDistance':0.5, # for every frame, only half the trace of the mouse will influence water
    'curl_param':15
}
```

修改代码中`load_image`为图片位置，并修改`shape`为图片的大小，即可切换。

### 参考

部分实现参考[Taichi_HW1_EulerianFluid](https://github.com/JerryYan97/Taichi_HW1_EulerianFluid) by [@JerryYan97](https://github.com/JerryYan97)

## To do list

* 修复底部有部分黑色的渗漏问题

