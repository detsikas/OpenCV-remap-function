## OpenCV-remap-function
 A tutorial on the use of OpenCV remap function

 The code of this repository demonstrates the use of the remap function. It creates a waving flag effect by applying the remap function on the axes of an image.
 
 The code is explained [here] (http://www.peeknpoke.net/single-post/2016/10/29/OpenCV-remap-function)

## Update:
 I have added python versions of the same code. Here is what they are doing
 
# ripple_effect.py
 Stay away from this one! This is just to indicate how slow matrix operations can be without the use of numpy
 
# ripple_effect_with_numpy.py
 This one uses numpy operations for creating the mapping arrays with the for loops and it is really fast

# ripple_effect_with_numpy_with_convert_maps.py
 Like the previous one but uses fixed point representation for the mapping arrays. This makes remap faster
 
 I have timed and compared all the operations above and details are provided [here]
