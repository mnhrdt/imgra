import iio                                        # image input/output
import imgra                                      # image processing with graphs
X = iio.read("http://gabarro.org/img/lenak.png")  # load a color image
h,w,d = X.shape                                   # extract shape
x = X.reshape(h*w, d)                             # flatten spatial dimension
B = imgra.grid_incidence(h, w)                    # gradient operator
L = - B.T @ B                                     # laplacian operator
iio.gallery([x, 127 - L@x, x + L@x/2, x - L@x/2]) # show various results
