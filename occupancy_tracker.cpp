#include <iostream>
#include <vector>

struct Point3D {
    float x, y, z;
};

int main() {
    std::cout << "Initializing AlphaAlgebra Native C++ 3D Occupancy Voxel Grid..." << std::endl;

    const int GRID_X = 200;
    const int GRID_Y = 200;
    const int GRID_Z = 50;
    
    std::vector<float> voxel_grid(GRID_X * GRID_Y * GRID_Z, 0.0f);

    std::vector<Point3D> incoming_point_cloud = {
        {0.0f,  5.5f,  0.2f},
        {-3.2f, 12.1f, 0.5f},
        {1.5f,  3.0f,  1.1f}
    };

    float grid_scale = 10.0f;
    int center_offset_x = GRID_X / 2;
    int center_offset_y = GRID_Y / 2;
    int center_offset_z = 0;
    int occupied_cells = 0;

    for (const auto& point : incoming_point_cloud) {
        int vx = static_cast<int>(point.x * grid_scale) + center_offset_x;
        int vy = static_cast<int>(point.y * grid_scale) + center_offset_y;
        int vz = static_cast<int>(point.z * grid_scale) + center_offset_z;

        if (vx >= 0 && vx < GRID_X && vy >= 0 && vy < GRID_Y && vz >= 0 && vz < GRID_Z) {
            int flattened_index = vx * (GRID_Y * GRID_Z) + vy * GRID_Z + vz;
            if (voxel_grid[flattened_index] == 0.0f) {
                voxel_grid[flattened_index] = 1.0f;
                occupied_cells++;
            }
        }
    }

    std::cout << "\n[NATIVE C++ OCCUPANCY TRACKER METRIC SUCCESS]" << std::endl;
    std::cout << "Allocated Matrix Volume  : " << GRID_X << "x" << GRID_Y << "x" << GRID_Z << " array space" << std::endl;
    std::cout << "Active Mapped Obstacles  : " << occupied_cells << " voxel cells flagged" << std::endl;
    return 0;
}
