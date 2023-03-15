import taichi as ti
import taichi.math as tm
#####################
#   Double Buffer
#####################
class TexPair:
    def __init__(self, cur, nxt):
        self.cur = cur
        self.nxt = nxt

    def swap(self):
        self.cur, self.nxt = self.nxt, self.cur

#####################
#   Bilerp fuction
#####################
@ti.func
def sample(vf, u, v, shape):
    i, j = int(u), int(v)
    # Nearest
    i = ti.max(0, ti.min(shape[0] - 1, i))
    j = ti.max(0, ti.min(shape[1] - 1, j))
    return vf[i, j]


@ti.func
def lerp(vl, vr, frac):
    # frac: [0.0, 1.0]
    return (1 - frac) * vl + frac * vr


@ti.func
def bilerp(vf, u, v, shape):
    # use -0.5 to decide where bilerp performs in cells
    s, t = u - 0.5, v - 0.5
    iu, iv = int(s), int(t)
    a = sample(vf, iu + 0.5, iv + 0.5, shape)
    b = sample(vf, iu + 1.5, iv + 0.5, shape)
    c = sample(vf, iu + 0.5, iv + 1.5, shape)
    d = sample(vf, iu + 1.5, iv + 1.5, shape)
    # fract
    fu, fv = s - iu, t - iv
    return lerp(lerp(a, b, fu), lerp(c, d, fu), fv)

#####################
#   Taichi Logo fuction
#####################
@ti.func
def inside(p, c, r):
  return (p - c).norm_sqr() <= r * r


@ti.func
def inside_taichi(p_):
  p = p_
  p = tm.vec2(0.5, 0.5) + (p - tm.vec2(0.5, 0.5)) * 1.11
  ret = -1
  if not inside(p, tm.vec2(0.50, 0.50), 0.55):
    if ret == -1:
      ret = 0
  if not inside(p, tm.vec2(0.50, 0.50), 0.50):
    if ret == -1:
      ret = 1
  if inside(p, tm.vec2(0.50, 0.25), 0.09):
    if ret == -1:
      ret = 1
  if inside(p, tm.vec2(0.50, 0.75), 0.09):
    if ret == -1:
      ret = 0
  if inside(p, tm.vec2(0.50, 0.25), 0.25):
    if ret == -1:
      ret = 0
  if inside(p, tm.vec2(0.50, 0.75), 0.25):
    if ret == -1:
      ret = 1
  if p[0] < 0.5:
    if ret == -1:
      ret = 1
  else:
    if ret == -1:
      ret = 0
  return ret

@ti.kernel
def paint(n_x:int,n_y:int,x:ti.template()):
  for i, j in ti.ndrange(n_x * 4, n_y * 4):
      ret = 1.0 - inside_taichi(tm.vec2(1.0 * i / n_x / 4, 1.0 * j / n_y / 4))
      x[i // 4, j // 4] += ret / 16