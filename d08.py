data = [int(i) for i in input()]
width = 25
height = 6
num_in_layer = width * height
layers = []

for i, c in enumerate(data):
    if (i % num_in_layer) is 0:
        layers.append([])

    layers[-1].append(c)

# for i, layer in enumerate(layers):
#     print("Layer " + str(i) + ": " + str(layer))


image = [0] * num_in_layer
pixel = range(0, num_in_layer)

for l in layers:
    pixels = [i for i in pixel if l[i] is not 2]
    pixel = [i for i in pixel if l[i] is 2]
    for i in pixels:
        image[i] = l[i]
    if len(pixel) is 0:
        break

for i in range(0, height):
    line = image[(i * width):((i + 1) * width)]
    print(str(line))
