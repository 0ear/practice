from skimage import io,data
img = data.chelsea()
io.imshow(img)
io.show()   #jupyter不用加io.show()即可顯示
print(img.shape)
print('顯示三個通道資訊')
print(img.shape[0])
print(img.shape[1])
print(img.shape[2])
print(img.max())
print(img.min())
print(img.mean())
print(img[0][0])
io.imsave('./graph/cat1.jpg')