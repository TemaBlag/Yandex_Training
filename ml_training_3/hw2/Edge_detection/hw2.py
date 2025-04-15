import numpy as np
import math

def compute_sobel_gradients_two_loops(image):
    height, width = image.shape
    gradient_x = np.zeros_like(image, dtype=np.float64)
    gradient_y = np.zeros_like(image, dtype=np.float64)
    padded_image = np.pad(image, ((1, 1), (1, 1)), mode='constant', constant_values=0)
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]) 
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]) 
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            gradient_x[i-1][j-1] = np.sum(padded_image[i-1:i+2, j-1:j+2] * sobel_x)
            gradient_y[i-1][j-1] = np.sum(padded_image[i-1:i+2, j-1:j+2] * sobel_y)
    return gradient_x, gradient_y

def compute_gradient_magnitude(sobel_x, sobel_y):
    assert sobel_x.shape == sobel_y.shape, "sobel_x and sobel_y must have equal dimensions"
    magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    return magnitude


def compute_gradient_direction(sobel_x, sobel_y):
    assert sobel_x.shape == sobel_y.shape, "sobel_x and sobel_y must have equal dimensions"
    gradient_direction = np.arctan2(sobel_y, sobel_x)
    return gradient_direction



cell_size = 7
def compute_hog(image, pixels_per_cell=(cell_size, cell_size), bins=9):
    if len(image.shape) == 3:
        image = np.mean(image, axis=2)  
    gradient_x, gradient_y = compute_sobel_gradients_two_loops(image) 
    magnitude = compute_gradient_magnitude(gradient_x, gradient_y) 
    direction = compute_gradient_direction(gradient_x, gradient_y) 
    cell_height, cell_width = pixels_per_cell
    n_cells_x = image.shape[1] // cell_width
    n_cells_y = image.shape[0] // cell_height
    histograms = np.zeros((n_cells_y, n_cells_x, bins))
    bin_width = 2 * math.pi / bins
    for i in range(n_cells_y):
        for j in range(n_cells_x):
            window_magnitude = magnitude[i * cell_height : (i+1) * cell_height, j * cell_width : (j+1) * cell_width]
            window_direction = direction[i * cell_height : (i+1) * cell_height, j * cell_width : (j+1) * cell_width]
            direction_bins = np.floor((window_direction + math.pi)/bin_width).astype(int)
            direction_bins = np.clip(direction_bins, 0, bins - 1)
            hist = np.zeros((bins))
            np.add.at(hist, direction_bins.flatten(), window_magnitude.flatten())
            sum_hist = hist.sum()
            if sum_hist > 0:
                hist /= sum_hist
            histograms[i, j] = hist
    return histograms