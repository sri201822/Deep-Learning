# Open Anaconda command Prompt and type the following commands in sequence.
step 1 : conda create --name tensorflow python=3.6 # for python 3.6 version
step 2 :activate tensorflow
step 3: pip install tensorflow
step 4: pip install tensorflow-gpu
# check for tensorflow
>> activate tensorflow
>> python (activating python shell)
>> import tensorflow as tf
>> hello = tf.constant(‘Hello, Tensorflow!’)
>> sess = tf.Session()
>> print(sess.run(hello))
