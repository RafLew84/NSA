# NanoSurface Analyzer Documentation

**NEtCAT NanoSurface Analyzer** application! This documentation will guide you through the key features and usage instructions.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
   - [File Read](#file-read)
   - [Preprocessing](#preprocessing)
   - [Processing](#processing)
   - [Measurement](#measurement)
   - [File Write](#file-write)
4. [About](#about)
5. [Contact](#contact)

## Introduction

**NanoSurface Analyzer** tool is designed for the analysis and measurement of surface data at the nanoscale. This application is developed to support researchers working with surface data by providing tools for reading, processing, and analyzing data.

Handles `mpp`, `stp (WSxM)`, and `s94` files, extracting both header information and image data for comprehensive analysis.

## Installation

To install the NanoSurface Analyzer, follow these steps:

1. Clone the repository:
   `git clone https://github.com/RafLew84/NSA`

2. Navigate to the project directory:
   `cd nanosurface-analyzer`

3. Install the required dependencies:
   `pip install -r requirements.txt`

## Usage

Follow these steps to utilize the NanoSurface Analyzer effectively:

- **Perform Preprocessing:** Start by preparing your images through the preprocessing steps. This is essential for accurate area and nearest neighbor detection.
- **Select Image for Analysis:** The last option in the options list is automatically set as the image for area determination. You can change this by using the "Move for Analysis" button to select a different image if needed.
- **Use Binary Images:** Ensure that only binary images are used for area and nearest neighbor determination. The analysis functions are designed to work specifically with binary images.
- **View Detected Areas:** After the analysis, you can view the image with marked detected areas by using the dropdown menu. Choose either the "Contours" or "WContours" options to visualize the results.
- **Review Detected Data:** The detected data will be displayed in a treeview format, providing a structured view of the analysis results.
- **Save Data:** To save the analysis results, use the "Save" button. The data can be saved in Excel format for further review and reporting.

### File Reading

The application supports the following file formats: `s94`, `stp (WSxM)`, and `mpp (WSxM)`. For `s94` and `stp` files, both header information and image data will be extracted. In the case of `mpp` files, data from each frame will be extracted individually.

Files can be read using one of the following methods:

1. **Selected Folder:** Reads all files of the chosen type within the selected folder.
2. **Open Files:** Allows for the selection and reading of multiple files of the chosen type.

### Preprocessing

The NanoSurface Analyzer provides the following preprocessing methods:

- **Intensity:** This preprocessing step involves adjusting the brightness and contrast of the image, typically using techniques like gamma correction and histogram equalization.
  - **Adaptive Equalization:** (Contrast Limited Adaptive Histogram Equalization - `skimage.exposure.equalize_adapthist`) Enhances contrast in small areas of the image, making local details more visible. This method adjusts contrast on a localized basis, which helps in bringing out details that might be lost in standard histogram equalization.
    - Parameters:
      - Image: `ndarray`
      - clip limit: `int` - Clipping limit, normalized between 0 and 1 (higher values give more contrast).
  - **Contrast Stretching:** (`skimage.exposure.rescale_intensity`) Expands the range of intensity values in an image to utilize the full spectrum of available intensities. This technique enhances the contrast of the entire image by stretching the histogram, making dark regions darker and bright regions brighter.
    - Parameters:
      - Image: `array`
      - min: `int` - Minimum percentile for contrast stretching.
      - max: `int` - Maximum percentile for contrast stretching.
  - **Gamma Adjustment:** (`skimage.exposure.adjust_gamma`) Modifies the overall brightness of the image by adjusting the gamma curve. Lowering the gamma value makes shadows more visible, while increasing it can brighten darker areas, effectively balancing the exposure.
    - Parameters:
      - Image: `ndarray`
      - gamma: `float` - Non-negative real number. Default value is 1.
- **Morphology:** Morphological operations are applied to help eliminate small noise and refine the shapes of features.
  - **Binary Greyscale Erosion:** (`scipy.ndimage.grey_erosion`) A morphological operation that removes pixels on object boundaries, effectively shrinking objects in a binary image. This method is used to eliminate small noise and separate connected objects, making features in the surface data more defined.
    - Parameters:
      - Input: `array_like`
      - kernel size: `int` - Shape of a flat and full structuring element used for the grayscale erosion.
      - kernel type: `str` - Structuring element used for the grayscale erosion. Available structuring elements: `re` - rectangle, `el` - ellipse, `cr` - cross
  - **Binary Greyscale Dilation:** (`scipy.ndimage.grey_dilation`) Opposite to erosion, this operation adds pixels to the boundaries of objects, causing them to grow. It helps in closing small holes within objects and connecting disjointed components, making features more prominent in the binary image.
    - Parameters:
      - Input: `array_like`
      - kernel size: `int` - Shape of a flat and full structuring element used for the grayscale erosion.
      - kernel type: `str` - Structuring element used for the grayscale erosion. Available structuring elements: `re` - rectangle, `el` - ellipse, `cr` - cross
  - **Binary Greyscale Opening:** (`scipy.ndimage.grey_opening`) A combination of erosion followed by dilation. This operation removes small objects or noise while preserving the shape and size of larger objects. It's useful for cleaning up the image by eliminating minor surface irregularities.
    - Parameters:
      - Input: `array_like`
      - kernel size: `int` - Shape of a flat and full structuring element used for the grayscale erosion.
      - kernel type: `str` - Structuring element used for the grayscale erosion. Available structuring elements: `re` - rectangle, `el` - ellipse, `cr` - cross
  - **Binary Greyscale Closing:** (`scipy.ndimage.grey_closing`) A combination of dilation followed by erosion. This operation fills small gaps or holes within objects and smooths the contours, making the features more uniform and connected. It's useful for enhancing surface continuity in the image.
    - Parameters:
      - Input: `array_like`
      - kernel size: `int` - Shape of a flat and full structuring element used for the grayscale erosion.
      - kernel type: `str` - Structuring element used for the grayscale erosion. Available structuring elements: `re` - rectangle, `el` - ellipse, `cr` - cross
  - **Propagation:** (`skimage.morphology.reconstruction`) Expands regions in an image by iteratively applying a morphological operation. This technique is often used for region growing and segmentation, allowing the identification and expansion of specific features or regions of interest on the surface. Implemented using morphological propagation (dilation/erosion) on an image using reconstruction.
    - Parameters:
      - Image: `ndarray`
      - type: `str` - Type of propagation (`dilation` or `erosion`).
      - marker value: `int` - Control parameter for how much of the image is altered during the propagation process
  - **White Top-Hat Transformation:** (`skimage.morphology.white_tophat`) Extracts small bright features from the background by subtracting the result of an opening operation from the original image. This method enhances small, bright details on the surface, making them more prominent for analysis. The white top hat of an image is defined as the image minus its morphological opening
    - Parameters:
      - Image: `ndarray`
      - selem type: `str` - Type of structuring element (`disk`, `square`, `diamond`, `star`).
      - selem size: `int` - Size of the structuring element.
  - **Black Top-Hat Transformation:** (`skimage.morphology.black_tophat`) Extracts small dark features from the background by subtracting the original image from the result of a closing operation. This technique emphasizes small, dark details on the surface, helping to highlight depressions or pits.
    - Parameters:
      - Image: `ndarray`
      - selem type: `str` - Type of structuring element (`disk`, `square`, `diamond`, `star`).
      - selem size: `int` - Size of the structuring element.
- **Noise Reduction:** Noise reduction techniques aim to eliminate random variations in the data that do not correspond to actual surface features. This can include methods like averaging, median filtering, or more advanced techniques to smooth out the data while preserving important details.
  - **Non-Local Means Denoising:** (`cv2.fastNlMeansDenoising`) Reduces noise in an image while preserving details by comparing the similarity between small patches of pixels throughout the image. This method works well for images with significant noise while maintaining sharp edges and important features.
    - Parameters:
      - Image: `ndarray` - The input image to be denoised.
      - h: `float` - Filter strength. A higher value results in a stronger filter, which may remove more noise but can also blur details.
      - TemplateWindowSize: `int` - Size of the window used to compute the denoising filter.
      - SearchWindowSize: `int` - Size of the window used to search for similar patches in the image.
  - **Gaussian Filtering:** (`scipy.ndimage.gaussian_filter`) Applies a Gaussian filter to smooth the image, reducing high-frequency noise and making features more distinguishable. This method is useful for general noise reduction and blurring, especially when a Gaussian kernel is appropriate for the type of noise present.
    - Parameters:
      - Image: `ndarray`
      - sigma: `float` - Standard deviation of the Gaussian filter. A higher value results in more smoothing.
- **Segmentation:** Image segmentation involves dividing an image into distinct regions or segments based on characteristics like intensity, color, or texture. This process helps in identifying and isolating specific features or regions of interest on the surface.
  - **Thresholding:** (`skimage.filters.threshold_otsu`) Separates objects in an image from the background based on a threshold value. Otsu's method automatically determines an optimal threshold to maximize the separation between foreground and background, which is useful for binary segmentation.
    - Parameters:
      - Image: `ndarray`
  - **Connected Components:** (`skimage.measure.label`) Labels connected regions in a binary image, making it possible to analyze and count individual objects or features. This method is useful for identifying and quantifying distinct regions in the image after thresholding.
    - Parameters:
      - Image: `ndarray`
  - **Watershed:** (`skimage.segmentation.watershed`) Segments an image based on topological features, treating pixel intensities as a topographic surface and finding basins or catchment areas. This technique is useful for separating overlapping or touching objects in the image.
    - Parameters:
      - Image: `ndarray`
      - markers: `ndarray` - Markers used to define starting points for the segmentation.
      - connectivity: `int` - Determines the connectivity for the watershed algorithm.
- **Measurement:** After preprocessing, the tool measures various properties of the surface features to analyze the data.

### Processing

The processing section involves further analysis and refinement of the preprocessed surface data to extract meaningful features and enhance the quality of the data.

- **Morphology:** These methods are useful for refining surface features and removing small artifacts.
  - **Binary Erosion:** (`skimage.morphology.binary_erosion`) A morphological operation that removes pixels on object boundaries, effectively shrinking objects in a binary image. This method is used to eliminate small noise and separate connected objects, making features in the surface data more defined.
    - Parameters:
      - Image: `ndarray` - The input image to be filtered.
      - footprint type: `str` - The shape of the structural element (`disk`, `square`, `diamond`, `star`).
      - footprint size: `int` - The size of the structural element that determines the extent of erosion.
  - **Binary Dilation:** (`skimage.morphology.binary_dilation`) Opposite to erosion, this operation adds pixels to the boundaries of objects, causing them to grow. It helps in closing small holes within objects and connecting disjointed components, making features more prominent in the binary image.
    - Parameters:
      - Image: `ndarray` - The input image to be filtered.
      - footprint type: `str` - The shape of the structural element (`disk`, `square`, `diamond`, `star`).
      - footprint size: `int` - The size of the structural element that determines the extent of dilation.
  - **Binary Opening:** (`skimage.morphology.binary_opening`) A combination of erosion followed by dilation. This operation removes small objects or noise while preserving the shape and size of larger objects. It's useful for cleaning up the image by eliminating minor surface irregularities.
    - Parameters:
      - Image: `ndarray` - The input image to be filtered.
      - footprint type: `str` - The shape of the structural element (`disk`, `square`, `diamond`, `star`).
      - footprint size: `int` - The size of the structural element that determines the extent of opening.
  - **Binary Closing:** (`skimage.morphology.binary_closing`) A combination of erosion followed by dilation. This operation removes small objects or noise while preserving the shape and size of larger objects. It's useful for cleaning up the image by eliminating minor surface irregularities.
    - Parameters:
      - Image: `ndarray` - The input image to be filtered.
      - footprint type: `str` - The shape of the structural element (`disk`, `square`, `diamond`, `star`).
      - footprint size: `int` - The size of the structural element that determines the extent of closing.
  - **Remove Small Holes:** (`skimage.morphology.remove_small_holes`) Removes small holes in a binary image, effectively filling in areas below a given size threshold. This method is useful for cleaning up noise and improving the clarity of features in binary surface data.
    - Parameters:
      - Image: `ndarray` - The input binary image from which small holes will be removed.
      - area threshold: `int` - The maximum area (in pixels) of holes that should be removed. Holes larger than this threshold will be preserved.
      - connectivity: `int` - The connectivity parameter defines the pixel neighborhood for the operation. Typically 1 (4-connectivity) or 2 (8-connectivity).
  - **Remove Small Objects:** (`skimage.morphology.remove_small_objects`) Removes small connected components (objects) in a binary image that are smaller than a specified size. This method is useful for cleaning up noise and isolating significant features in surface data.
    - Parameters:
      - Image: `ndarray` - The input binary image from which small objects will be removed.
      - min_size: `int` - The minimum size (in pixels) of objects that should be retained. Objects smaller than this threshold will be removed.
      - connectivity: `int` - The connectivity parameter defines the pixel neighborhood for the operation. Typically 1 (4-connectivity) or 2 (8-connectivity).

- **Thresholding:** Converts grayscale images into binary images by applying a threshold value. This method is useful for separating objects of interest from the background or segmenting specific features.
  - **Otsu Threshold:** (`skimage.filters.threshold_otsu`) A global thresholding method that automatically determines the optimal threshold value by maximizing the variance between the foreground and background classes. This method is widely used for binarizing grayscale images.
    - Parameters:
      - Image: `ndarray` - The input grayscale image to be thresholded.
  - **Local Threshold:** (`skimage.filters.threshold_local`) This method applies adaptive thresholding, where the threshold is calculated for smaller regions of the image, allowing for better segmentation in images with varying lighting conditions. It is particularly useful for unevenly illuminated images.
    - Parameters:
      - Image: `ndarray` - The input grayscale image to be thresholded.
      - method: `str` - The method for calculating the local threshold (e.g., `gaussian`).
      - block size: `int` - The size of the block used to calculate the threshold.
      - offset: `float` - A constant value subtracted from the calculated local threshold.
  - **Niblack Threshold:** (`skimage.filters.threshold_niblack`) This method applies Niblack's thresholding, which calculates the threshold based on the local mean and standard deviation within a window around each pixel. It's particularly useful for images with varying foreground and background intensities.
    - Parameters:
      - Image: `ndarray` - The input grayscale image to be thresholded.
      - window size: `int` - The size of the window used to calculate the local mean.
      - k: `float` - A tuning parameter that adjusts the threshold relative to the local mean (positive values raise the threshold, negative values lower it).
  - **Sauvola Threshold:** (`skimage.filters.threshold_sauvola`) This method applies Sauvola's thresholding, which adapts the thresholding value based on local mean and standard deviation, with an additional parameter to adjust the dynamic range of the standard deviation. It is effective for images with varying lighting conditions and contrast.
    - Parameters:
      - Image: `ndarray` - The input grayscale image to be thresholded.
      - window size: `int` - The size of the window used to calculate the local mean and standard deviation.
      - k: `float` - A tuning parameter that adjusts the threshold relative to the local mean and standard deviation (positive values typically raise the threshold).
      - r: `float` - The dynamic range of the standard deviation, which scales the standard deviation to enhance or suppress local contrast.
  - **Yen Threshold:** (`skimage.filters.threshold_yen`) This method applies Yen's thresholding, which calculates the optimal threshold value by maximizing the variance of the background and foreground. It is useful for images with well-separated foreground and background intensity distributions.
    - Parameters:
      - Image: `ndarray` - The input grayscale image to be thresholded.
  - **ISODATA Threshold:** (`skimage.filters.threshold_isodata`) This method applies ISODATA thresholding, which determines the optimal threshold by iteratively minimizing the intra-class variance of the background and foreground. It is particularly effective for images with bimodal intensity distributions.
    - Parameters:
      - Image: `ndarray` - The input grayscale image to be thresholded.
  - **Binary Threshold:** (`cv2.threshold`) This method applies binary thresholding to an image using a fixed threshold value. Pixels in the image with intensity values above the threshold are set to the maximum value (255), while those below the threshold are set to 0. This technique is useful for separating objects from the background in grayscale images.
    - Parameters:
      - Image: `ndarray` - The input grayscale image to be thresholded.
      - threshold: `int` - The fixed threshold value to binarize the image. Pixels with intensity values above this threshold are set to 255, and those below are set to 0.

- **Manual Edit:** Allows users to directly modify the image by manually selecting and editing specific regions. This method is often used for correcting errors or refining specific areas that require detailed attention. Interactive editing is facilitated through matplotlib's `RectangleSelector`, which enables users to select regions of the image and modify them as needed.
  - **Image Edit Remove:** Removes white areas from the binary image by allowing users to interactively select and edit specific regions.
    - Parameters:
      - Image: `ndarray` - The input binary image.

### Measurement

How to measure surface data using the NanoSurface Analyzer.

- **Area Measurement:** Calculates the area of each labeled region in a binary image. The area of each region is measured by counting the number of pixels that belong to that region. The function `calculate_regions` uses `skimage.measure.regionprops` to compute the properties of each labeled region, including its area.
  - Parameters:
    - Image: `ndarray` - The input binary image with labeled regions.

- **Nearest Neighbor Distance Measurement:** Calculates the distance between each centroid of labeled regions and its nearest neighbor. The distances are computed using a KDTree for efficient nearest-neighbor queries. The function `compute_nearest_neighbor_distances` performs this computation and provides distances along with names of the nearest neighbors.
  - Parameters:
    - Centroids: `ndarray` - The coordinates of the centroids of the labeled regions.
    - Names: `list` - The labels or names associated with each centroid.

### File Write

Instructions for saving the processed data back to a file.

- **Saving Images:** Converts and saves images in various formats using OpenCV. The function `save_image` takes an image and the desired file name as inputs and saves the image in the specified format (e.g., JPEG, PNG). This method is useful for exporting processed images for further analysis or reporting.
  - Parameters:
    - Image: `ndarray` - The image to be saved.
    - Filename: `str` - The name of the file where the image will be saved.

- **Saving Measurements:** Saves calculated measurements to a CSV file. The function `save_measurements` takes measurement data and writes it to a CSV file using pandas. This method allows for easy storage and retrieval of measurement data for further analysis.
  - Parameters:
    - Measurements: `DataFrame` - The measurement data to be saved.
    - Filename: `str` - The name of the CSV file where the measurements will be saved.

### About

The NanoSurface Analyzer is developed as part of the NEtCAT project, aiming to provide advanced tools for nanosurface analysis. The tool is designed to handle various file formats and offer a range of preprocessing and analysis techniques.

## Contact

For more information, feedback, or support, please contact:

- **Email:** rafal.lewandkow2@uwr.edu.pl
- **Website:** [https://netcat.uwr.edu.pl/](https://netcat.uwr.edu.pl/)

