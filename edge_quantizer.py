import torch

def quantize_tensors_to_int8(float_tensor):
    """
    Simulates uniform symmetric quantization. 
    Converts FP32 weights/activations down to INT8 for extreme edge AI hardware efficiency.
    """
    # 1. Determine the absolute dynamic range of your spatial data matrix
    max_val = torch.max(torch.abs(float_tensor))
    
    # 2. Calculate the scaling factor mapping the tensor limits to INT8 boundaries (-128 to 127)
    scale = max_val / 127.0
    
    # Avoid zero division errors if the tensor contains all zeros
    if scale == 0:
        scale = 1.0
        
    # 3. Scale, round to the nearest whole integer, and clamp into explicit signed 8-bit limits
    quantized_tensor = torch.clamp(torch.round(float_tensor / scale), -128, 127).to(torch.int8)
    
    return quantized_tensor, scale

def dequantize_tensors_to_fp32(quantized_tensor, scale):
    """
    Reconstructs the original spatial matrix framework back into floating-point format
    to calculate structural mathematical precision loss.
    """
    return quantized_tensor.to(torch.float32) * scale

if __name__ == "__main__":
    print("Initializing AlphaAlgebra Edge Hardware Quantization Pipeline...")

    # Simulate a matrix of 1,000 deep learning weights evaluating a spatial coordinate transformer
    spatial_layer_weights = torch.randn(1000) * 5.5
    print(f"Original Data Precision : {spatial_layer_weights.dtype}")
    print(f"Sample Original Vector   : {spatial_layer_weights[:3]}")

    # Run the hardware compression layer
    quantized, scale_factor = quantize_tensors_to_int8(spatial_layer_weights)
    print(f"\n[QUANTIZATION LAYER SUCCESSFUL]")
    print(f"Compressed Hardware Type: {quantized.dtype}")
    print(f"Sample Compressed Vector: {quantized[:3]}")
    print(f"Calculated Scale Factor : {scale_factor:.6f}")

    # Evaluate the exact precision loss to guarantee functional safety metrics
    reconstructed_weights = dequantize_tensors_to_fp32(quantized, scale_factor)
    mean_squared_error = torch.mean((spatial_layer_weights - reconstructed_weights) ** 2)
    print(f"\nQuantization Precision Loss (MSE): {mean_squared_error:.6f}")
