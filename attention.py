import tensorflow as tf


def attention(inputs):
    # Trainable parameters
    hidden_size = inputs.shape[-1].value
    print(hidden_size)
    print("input",inputs.shape)
    u_omega = tf.get_variable("u_omega", [hidden_size], initializer=tf.keras.initializers.glorot_normal())
    print("u_omega",u_omega.shape)
    with tf.name_scope('v'):
        v = tf.tanh(inputs)
        print("v",v.shape)


    # For each of the timestamps its vector of size A from `v` is reduced with `u` vector
    vu = tf.tensordot(v, u_omega, axes=1, name='vu')  # (B,T) shape
    print("vu",vu.shape)

    alphas = tf.nn.softmax(vu, name='alphas')  # (B,T) shape
    print("alphas",alphas.shape)

    # Output of (Bi-)RNN is reduced with attention vector; the result has (B,D) shape
    output = tf.reduce_sum(inputs * tf.expand_dims(alphas, -1), 1)
    print("output",output.shape)

    # Final output with tanh
    output = tf.tanh(output)
    print("output",output.shape)

    return output, alphas
