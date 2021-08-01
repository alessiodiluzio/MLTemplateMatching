import platform

OS = platform.system()

# PATH
DATA_PATH = 'samples'

# PREPROCESSING
IMAGE_DIM = 255
IMAGE_OUTPUT_DIM = 22
CROP_OUTPUT_DIM = 6
OUTPUT_CHANNELS = 128
OUTPUT_DIM = 17

CHANNELS = 3
CROP_SIZE = 127
CROP_BOX = (CROP_SIZE, CROP_SIZE)
NUM_BOXES = 1

# TRAINING
BATCH_SIZE = 5
EPOCHS = 50
LEARNING_RATE = 0.0000099

# UTILS
X_1 = 0
Y_1 = 1
X_2 = 2
Y_2 = 3
