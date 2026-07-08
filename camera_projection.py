import torch

def project_pixels_to_3d(pixel_coordinates, depth_values, intrinsic_matrix):
    """
    Transforms flat 2D camera pixels into 3D world space coordinates.
    Essential for transforming video streams into a Bird's-Eye View (BEV).
    """
    # Extract intrinsic camera calibration parameters
    fx = intrinsic_matrix[0, 0] # Focal length X
    fy = intrinsic_matrix[1, 1] # Focal length Y
    cx = intrinsic_matrix[0, 2] # Principal point X
    cy = intrinsic_matrix[1, 2] # Principal point Y

    u = pixel_coordinates[:, 0]
    v = pixel_coordinates[:, 1]

    # Apply back-projection geometry: X = (u - cx) * Z / fx
    X = (u - cx) * depth_values / fx
    Y = (v - cy) * depth_values / fy
    Z = depth_values

    # Stack into a dense N x 3 spatial tensor coordinate layout
    return torch.stack((X, Y, Z), dim=1)

if __name__ == "__main__":
    print("Initializing AlphaAlgebra 2D-to-3D Spatial Projection Pipeline...")

    # Mock an intrinsic camera calibration matrix (Focal length and centers)
    # This matrix tells the AI how the camera lens distorts physical space
    K = torch.tensor([
        [1000.0,    0.0,  960.0],
        [   0.0, 1000.0,  540.0],
        [   0.0,    0.0,    1.0]
    ])

    # Simulate 3 bounding box centers detected on a 1080p camera feed [u_pixel, v_pixel]
    detected_pixels = torch.tensor([
        [960.0, 540.0],  # Exactly in the dead center of the screen
        [1100.0, 600.0], # Slightly to the right and closer to the ground
        [800.0, 480.0]   # Slightly to the left and higher up
    ])

    # Estimated distances (depth in meters) calculated by an occupancy tracker model
    estimated_depths = torch.tensor([15.0, 8.5, 22.1])

    # Execute geometric back-projection
    spatial_world_coordinates = project_pixels_to_3d(detected_pixels, estimated_depths, K)

    print("\n[SPATIAL TRANSLATION MATRIX CALCULATION COMPLETE]")
    for i, coords in enumerate(spatial_world_coordinates):
        print(f"Object {i+1} Vector -> X: {coords[0]:.2f}m, Y: {coords[1]:.2f}m, Depth: {coords[2]:.2f}m")
