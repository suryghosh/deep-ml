import torch

def gaussian_elimination(A: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    """
    Solves the system Ax = b using Gaussian Elimination with partial pivoting.

    :param A: Coefficient matrix (torch.Tensor)
    :param b: Right-hand side vector (torch.Tensor)
    :return: Solution vector x (torch.Tensor)

    """
    return torch.linalg.solve(A,b)
    return torch.zeros_like(b, dtype=torch.float64)