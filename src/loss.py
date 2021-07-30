import tensorflow as tf


def get_balanced_weigths(balance_factor, label):
    label_true = (label + 1) / 2
    label_false = (label - 1) / 2
    weights = (1 - balance_factor) * label_true + balance_factor * label_false * -1
    return weights


def softmax_cross_entropy_loss(logits, label, balance_factor, training=True):
    cross_entropy = tf.compat.v1.nn.softmax_cross_entropy_with_logits_v2(labels=label, logits=logits)
    if training:
        cross_entropy = tf.expand_dims(cross_entropy, axis=3)
        weights = get_balanced_weigths(balance_factor, label)
        cross_entropy = tf.math.multiply(cross_entropy, weights)
        return tf.reduce_mean(cross_entropy)
    return cross_entropy


# l(y,v) = log(1 + exp(-yv)
# to avoid overflow when -yv < 0
# log(1 + exp(-yv)) = log(1 + exp(-abs(y,v)) -yv + max(0, yv)
def compute_logistic_loss(labels, logits):
    x = tf.math.multiply(logits, labels)
    loss = tf.math.log(1 + tf.math.exp(-1 * tf.math.abs(x))) - x + tf.math.maximum(tf.zeros(x.shape), x)
    return loss


def logistic_loss(logits, label, balance_factor, training=True):
    log_loss = compute_logistic_loss(label, logits)
    if training:
        weights = get_balanced_weigths(balance_factor, label)
        log_loss = tf.math.multiply(log_loss, weights)
    log_loss = tf.reduce_mean(log_loss)
    return log_loss


def sigmoid_cross_entropy_loss(logits, label, balance_factor, training=True):
    cross_entropy = tf.compat.v1.nn.softmax_cross_entropy_with_logits_v2(labels=label, logits=logits)
    if training:
        cross_entropy = tf.expand_dims(cross_entropy, axis=3)
        weights = get_balanced_weigths(balance_factor, label)
        cross_entropy = tf.math.multiply(cross_entropy, weights)
        return tf.reduce_mean(cross_entropy)
    return cross_entropy
