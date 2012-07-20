#!/usr/bin/env python

from __future__ import division
import numpy as np
import math

def cooccurence(f, direction, output=None, symmetric=True):
    '''
    cooccurence_matrix = cooccurence(f, direction, output={new matrix})

    Compute grey-level cooccurence matrix

    Parameters
    ----------
    f : ndarray of integer type
        The input image
    direction : integer
        Direction as index into (horizontal [default], diagonal
        [nw-se], vertical, diagonal [ne-sw])
    output : np.long 2 ndarray, optional
        preallocated result.
    symmetric : boolean, optional
        whether return a symmetric matrix (default: False)

    Returns
    -------
      cooccurence_matrix : cooccurence matrix
    '''
    _verify_is_integer_type(f, 'mahotas.cooccurence')
    if len(f.shape) == 2:
        assert direction in (0,1,2,3), 'mahotas.texture.cooccurence: `direction` %s is not in range(4).' % direction
    elif len(f.shape) == 3:
        assert direction in xrange(13), 'mahotas.texture.cooccurence: `direction` %s is not in range(13).' % direction
    else:
        raise ValueError('mahotas.texture.cooccurence: cannot handle images of %s dimensions.' % len(f.shape))

    if output is None:
        mf = f.max()
        output = np.zeros((mf+1, mf+1), np.int32)
    else:
        assert np.min(output.shape) >= f.max(), 'mahotas.texture.cooccurence: output is not large enough'
        assert output.dtype == np.int32, 'mahotas.texture.cooccurence: output is not of type np.int32'
        output.fill(0)

    if len(f.shape) == 2:
        Bc = np.zeros((3, 3), f.dtype)
        y,x = _2d_deltas[direction]
        Bc[y+1,x+1] = 1
    else:
        Bc = np.zeros((3, 3, 3), f.dtype)
        y,x,z = _3d_deltas[direction]
        Bc[y+1,x+1,z+1] = 1
    _texture.cooccurence(f, output, Bc, symmetric)
    return output

_2d_deltas= [
    (0,1),
    (1,1),
    (1,0),
    (1,-1)]

_3d_deltas = [
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
    (1,-1, 0),
    (0, 0, 1),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 1),
    (1,-1, 1),
    (1, 0,-1),
    (0, 1,-1),
    (1, 1,-1),
    (1,-1,-1) ]

def feat0(f):
    fm1 = f.max()+1
    cmat = np.empty((fm1, fm1), np.int32)
    T = cmat.sum()
    p = cmat / float(T)
    pravel = p.ravel()
    