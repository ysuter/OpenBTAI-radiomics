# Code used to extract features

The code available here may be used to customize the feature extraction and tailor it to a target task.

### Input file for batch processing
The script "batchpyradprep.py" creates a CSV file with the paths to the images and masks and adds a line for each label in the image. It produces a CSV by iterating over the dataset. This is the input to the feature extraction script. You will have to change the path on line 10 to where you saved the dataset.

### Feature extraction with PyRadiomics
"batchextract.py" is the script for the feature extraction. Please adapt the paths on lines 18-21. The path on line 18 should point to the output CSV of batchpyradprep.py. The settings.yaml file sets the parameters for the feature extraction. This is heavily based on the [PyRadiomics examples](https://github.com/AIM-Harvard/pyradiomics/tree/master/examples)

### Post-processing the features
The script postprocess_feat.py was used to moves relevant columns to the front and removes two redundant ones.
