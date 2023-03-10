# 2DEulerianFluidSolver
A interactive demo of 2D Eulerian Fluid Solver based on Taichi Lang

这是一个使用[太极语言](https://docs.taichi-lang.org/)编程的2D欧拉流体求解器，该项目支持：

- 水面能够与鼠标进行交互
- 添加旋度运算，更好的流体表现 ：）
- 支持切换流体的背景图片（图片位于img目录下方）
- 代码简短清晰，方便学习

![仿真效果](https://github.com/Lee-abcde/2DEulerianFluidSolver/blob/dev/img/cover.png)

### Demo依赖包安装

```
python version = 3.9.16
conda install taichi
conda install matplotlib
```

安装以上两个包之后，运行`main.py`即可以和demo玩耍

### 如何切换流体初始图片

```
eulerSimParam = {
    'load_image':'img/test1.jpg',
    'shape': [1200, 1200],
    'dt': 1 / 60.,
    'iteration_step': 50,
    'mouse_radius':0.01,# [0.0,1.0] float
    'mouse_pressure': 50.,
    'curl_param':15
}
```

修改代码中`load_image`为图片位置，并修改`shape`为图片的大小，即可切换。

### 参考

部分实现参考[Taichi_HW1_EulerianFluid](https://github.com/JerryYan97/Taichi_HW1_EulerianFluid) by [@JerryYan97](https://github.com/JerryYan97)

