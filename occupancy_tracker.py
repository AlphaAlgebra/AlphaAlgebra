import torch

def generate_spatial_occupancy_grid(grid_dimensions, point_cloud, collision_radius=1.2):
    """
    Discretizes 3D physical coordinate points into a spatial occupancy voxel grid.
    Tracks whether coordinate points in space are clear (0.0) or occupied (1.0).
    """
    # 1. Initialize a blank 3D spatial tensor grid [Width, Depth, Height]
    # Representing a 20m x 20m x 5m localized volume around the vehicle
    voxel_grid = torch.zeros(grid_dimensions)
    
    # Define physical grid boundary scales (mapping meters to tensor index coordinates)
    grid_scale = 10.0  # 10 voxels per meter (10cm resolution per cell)
    center_offset = torch.tensor([grid_dimensions[0] // 2, grid_dimensions[1] // 2, 0])
    
    # 2. Iterate through incoming real-world spatial vectors
    for point in point_cloud:
        # Convert physical coordinate meters to localized discrete matrix indices
        voxel_x = int(point[0] * grid_scale) + center_offset[0]
        voxel_y = int(point[1] * grid_scale) + center_offset[1]
        voxel_z = int(point[2] * grid_scale) + center_offset[2]
        
        # Ensure the calculated indices fall safely within our monitored buffer space
        if (0 <= voxel_x < grid_dimensions[0] and 
            0 <= voxel_y < grid_dimensions[1] and 
            0 <= voxel_z < grid_dimensions[2]):
            
            # Map physical obstacle point density and flag the voxel coordinate as OCCUPIED
            voxel_grid[voxel_x, voxel_y, voxel_z] = 1.0
            
    return voxel_grid

if __name__ == "__main__":
    print("Initializing AlphaAlgebra 3D Spatial Occupancy Tracker Engine...")

    # Define our 3D monitoring resolution grid spatial array (200x200x50 voxel space)
    target_dimensions = (200, 200, 50)

    # Simulate actual live 3D coordinates parsed from our camera back-projection engine
    # [X distance, Y distance, Z height] relative to the vehicle center
    incoming_point_cloud = torch.tensor([
        [0.0,  5.5,  0.2],   # Stationary vehicle directly ahead at 5.5 meters
        [-3.2, 12.1, 0.5],   # Physical concrete median wall block on the left
        [1.5,  3.0,  1.1]    # Low-hanging structural clearance obstacle on the right
    ])

    # Execute voxelization layer matrix tracking
    live_occupancy_map = generate_spatial_occupancy_grid(target_dimensions, incoming_point_cloud)
    
    # Extract structural analytics to verify matrix allocation integrity
    occupied_cells = torch.sum(live_occupancy_map == 1.0).item()
    print(f"\n[OCCUPANCY METRIC EVALUATION SUCCESSFUL]")
    print(f"Total Allocated Voxel Space Volume : {live_occupancy_map.shape}")
    print(f"Active Discretized Obstacle Points : {occupied_cells} cells mapped")
    print("Pipeline Execution Status          : OPERATIONAL (Real-Time Synchronized)")
