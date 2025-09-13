import numpy as np

__all__ = ["GF2"]

class GF2(np.ndarray):
    """
    Implements an array of 0s and 1s (Galois field of length 2)
    Derives a numpy array to do so.
    
    In GF(2):
    - Addition is XOR
    - Multiplication is AND
    """
    def __new__(cls, input_array):
        """Creates a GF2 array, the proper numpy way.
        """
        # Convert input to boolean then view as GF2
        obj = np.asarray(input_array, dtype=bool).view(cls)
        return obj
    
    def __array_finalize__(self, obj) -> None:
        """More appropiate numpy stuff.
        """
        return super().__array_finalize__(obj)
    
    # Arithmetic operations
    def __add__(self, other):
        return GF2(np.logical_xor(self, other))

    def __radd__(self, other):
        return self + other     # Makes conmutativity explicit
    
    def __mul__(self, other):
        return GF2(np.logical_and(self, other))
    
    def __rmul__(self, other):
        return self * other     # Makes conmutatibity explicit
    
    def __matmul__(self, other):
        """
        If both matrices are GF2,
            Calls GF2 matrix multiplication (with GF2 addition and multiplication)
        If not,
            Calls normal matrix multiplication, which now behaves as linear transformation 
            from a Matrix over GF2 to a Matrix over the reals.
        """
        if isinstance(other, GF2):
            return GF2(self._gf2_matmul(self, other))
        return self._matmul(self, other)
    
    def __rmatmul__(self, other):
        """
        If both matrices are GF2,
            Calls GF2 matrix multiplication (with GF2 addition and multiplication)
        If not,
            Calls normal matrix multiplication, which now behaves as linear transformation 
            from a Matrix over GF2 to a Matrix over the reals.
        """
        if isinstance(other, GF2):
            return self._gf2_matmul(other, self)
        return GF2(self._matmul(other, self))
    
    @staticmethod
    def _gf2_matmul(a, b):
        """Implements GF2 matrix multiplication with GF2 addition adn multplication."""
        # Passes matrices to boolean, aka. GF2 in all but name
        a_bool = np.asarray(a, dtype=bool)
        b_bool = np.asarray(b, dtype=bool)

        # A TRICK. Makes sure both matrices have a shape that when multiplied results in a matrix that can then be...
        a_expanded = a_bool[:, np.newaxis, :]
        b_expanded = b_bool[np.newaxis, :, :].transpose(0, 2, 1)
        
        # ..."Multiplied" with each other
        # The result is an array with the coefficients of elements all columns multiplied by those of all rows
        products = a_expanded & b_expanded
        # Now the results of the multiplications can be "added" up with each other.
        return np.logical_xor.reduce(products, axis=2)
    
    @staticmethod
    def _matmul(a, b):
        """Implements normal matrxi multiplication in a GF2 matrix."""
        # Make sure the matrices to be multiplied are represented as integers
        a_int = np.asarray(a, dtype=int)
        b_int = np.asarray(b, dtype=int)

        # A TRICK, to put both matrices in shape that can then be multiplied and result int
        a_expanded = a_int[:, np.newaxis, :]
        b_expanded = b_int[np.newaxis, :, :].transpose(0, 2, 1)
        
        # The result are teh multiplicaitons of all the elements of all columns by htose of all rows
        products = a_expanded * b_expanded
        
        # The previous results are then added up in axis 2
        return np.sum(products, axis=2)

    def __repr__(self) -> str:
        return f"GF2({np.asarray(self, dtype=int)})"
    
    def __str__(self) -> str:
        return str(np.asarray(self, dtype=int))
    
    def __array_function__(self, func, types, args, kwargs):
        """Overrides numpy methods such as np.add so that they respect GF2 arithmatic."""
        if func is np.matmul:
            return self.__matmul__(args[1])
        elif func is np.add:
            return self.__add__(args[1])
        elif func is np.multiply:
            return self.__mul__(args[1])
        
        # Fallback, call defauult behavior
        return super().__array_function__(func, types, args, kwargs)