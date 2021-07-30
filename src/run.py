import tensorflow as tf

from src import EPOCHS, DATA_PATH, LEARNING_RATE
from src.training import train
from src.test import test
from src.dataset import get_dataset
from src.loss import logistic_loss, softmax_cross_entropy_loss, sigmoid_cross_entropy_loss


def run_train():
    training_set, validation_set, train_step, val_step = get_dataset(show=False)
    train(training_set, validation_set, EPOCHS, train_step, val_step,
          plot_path='plot', image_path='image', loss_fn=softmax_cross_entropy_loss,
          optimizer=tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE), early_stopping=15)


def run_test(test_path=DATA_PATH):
    test_set = get_dataset(data_path=test_path, batch_size=1, split_perc=1, show=False)
    test(test_set, output_path='image')
