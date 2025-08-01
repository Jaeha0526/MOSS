import torch
import numpy as np

def tensor_product_xz(x, z):
    """
    Generate correct inputs for bx different xs and bz different zs.
    For each z we want to evaluate it at all xs and vice versa, so we need a tensor product between the rows of the two vectors.
    x: [bx, nx]
    z: [bz, nz]
    returns: [bx*bz, nx+nz]
    """
    z_tp = z.repeat_interleave(len(x), 0)
    x_tp = x.repeat(len(z), 1)
    # xz = torch.hstack([x_rep, z_rep])
    return x_tp, z_tp