import numpy as np


# =========================
#       对称量化
# =========================
def quantize_symmetric(x, num_bits=8):
    qmax = 2 ** (num_bits - 1) - 1  # int8: [-127, 127]
    scale = np.max(np.abs(x)) / qmax
    x_quant = np.round(x / scale).astype(np.int32)
    return x_quant, scale


def dequantize_symmetric(x, scale):
    return x.astype(np.float32) * scale


x = np.array([-1., 2., 3.])
w = np.array([[0.1, 0.2, 0.3],
              [0.4, 0.5, 0.6]]).T

y_float = x @ w
print("===== 原始浮点计算 =====")
print(f"x          : {x}")
print(f"w          : \n{w}")
print(f"y_float    : {y_float}\n")

x_quant, x_scale = quantize_symmetric(x)
w_quant, w_scale = quantize_symmetric(w)
print("===== 对称量化 =====")
print(f"x_quant    : {x_quant}")
print(f"x_scale    : {x_scale:.6f}")
print(f"w_quant    :\n{w_quant}")
print(f"w_scale    : {w_scale:.6f}")

y_int = x_quant @ w_quant
y_dequant = dequantize_symmetric(y_int, x_scale * w_scale)
mse = np.mean((y_dequant - y_float) ** 2)

# print(f"y_int      : {y_int}")
print(f"y_dequant  : {y_dequant}")
print(f"MSE(sym)   : {mse}\n")


# =========================
#        非对称量化
# =========================
def quantize_asymmetric(x, num_bits=8):
    q_min = 0
    q_max = 2 ** num_bits - 1
    x_min = np.min(x)
    x_max = np.max(x)
    scale = (x_max - x_min) / (q_max - q_min)
    zero_point = np.round(q_min - x_min / scale).astype(np.int32)
    x_quant = np.clip(np.round(x / scale + zero_point), q_min, q_max).astype(np.int32)
    return x_quant, zero_point, scale


def dequantize_asymmetric(x, zero_point, scale):
    return (x.astype(np.float32) - zero_point) * scale


x_quant, x_zero, x_scale = quantize_asymmetric(x)
w_quant, w_zero, w_scale = quantize_asymmetric(w)

print("===== 非对称量化 =====")
print(f"x_quant    : {x_quant}")
print(f"x_zero     : {x_zero}")
print(f"x_scale    : {x_scale:.6f}")

print(f"w_quant    :\n{w_quant}")
print(f"w_zero     : {w_zero}")
print(f"w_scale    : {w_scale:.6f}")

y_int = (x_quant - x_zero) @ (w_quant - w_zero)
y_dequant = y_int * x_scale * w_scale
mse = np.mean((y_dequant - y_float) ** 2)

# print(f"y_int      : {y_int}")
print(f"y_dequant  : {y_dequant}")
print(f"MSE(asym)  : {mse}")
