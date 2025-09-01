"""
Galois Field GF(2) Implementation for NumPy
"""
import numpy as np

__all__ = ["GF2"]

class GF2(np.ndarray):
    def __new__(cls, input_array, dtype=None):
        obj = np.asarray(input_array, dtype=bool).view(cls)
        return obj
    
    def __array_finalize__(self, obj) -> None:
        return super().__array_finalize__(obj)
    
    # Arithmetic operations
    def __add__(self, other):
        return GF2(np.logical_xor(self, other))

    def __radd__(self, other):
        return self + other
    
    def __mul__(self, other):
        return GF2(np.logical_and(self, other))
    
    def __rmul__(self, other):
        return self * other
    
    def __matmul__(self, other):
        if not (isinstance(other, GF2)):
            return self._matmul(self, other)
        return GF2(self._gf2_matmul(self, other))
    
    def __rmatmul__(self, other):
        if not (isinstance(other, GF2)):
            return self._matmul(other, self)
        return GF2(self._gf2_matmul(other, self))
    
    @staticmethod
    def _gf2_matmul(a, b):
        a_bool = np.asarray(a, dtype=bool)
        b_bool = np.asarray(b, dtype=bool)

        a_expanded = a_bool[:, np.newaxis, :]
        b_expanded = b_bool[np.newaxis, :, :].transpose(0, 2, 1)
        
        products = a_expanded & b_expanded
        return np.logical_xor.reduce(products, axis=2)
    
    @staticmethod
    def _matmul(a, b):
        a_int = np.asarray(a, dtype=int)

        b_int = np.asarray(b, dtype=int)
        a_expanded = a_int[:, np.newaxis, :]
        b_expanded = b_int[np.newaxis, :, :].transpose(0, 2, 1)
        
        products = a_expanded * b_expanded
        return np.sum(products, axis=2)

    def __repr__(self) -> str:
        return f"GF2({np.asarray(self, dtype=int)})"
    
    def __str__(self) -> str:
        return str(np.asarray(self, dtype=int))