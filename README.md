# Vector Projection in R3

This project demonstrates how to decompose a vector into components parallel and perpendicular to another vector using the standard inner product.

## Description

Given two vectors in R3, the script computes the projection of one vector onto the other and then computes the residual vector. The result verifies the orthogonal decomposition of a vector relative to a given direction.

## Files

- `vector_projection.py`: Python script that computes a vector projection and verifies the decomposition.

## Example

For vectors u and v, the script computes:

- the projection of v onto u
- the residual vector r = v − proj_u(v)

The output confirms that the residual is orthogonal to u and that v is the sum of the projection and the residual.

## How to run

```bash
python3 vector_projection.py
