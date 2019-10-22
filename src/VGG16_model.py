from keras.applications.vgg16 import VGG16
from keras.layers import Dense, Flatten
from keras.models import Model


def model_imagenet(img_width, img_height, num_classes, x_all=None, y_all=None,
				   optimizer=None):
	base_model = VGG16(weights='imagenet', include_top=False,
					   input_shape=(img_height, img_width, 3))

	x = base_model.output
	x = Flatten(name='flatten')(x)
	x = Dense(4096, activation='relu', name='fc1')(x)
	x = Dense(4096, activation='relu', name='fc2')(x)

	predictions = Dense(1, activation='sigmoid')(x) if num_classes == 2 \
		else Dense(num_classes, activation='softmax')(x)

	# this is the model we will train
	model = Model(inputs=base_model.input, outputs=predictions)

	return model, base_model


def VGG16_imagenet():
	return {"model": model_imagenet, "name": "VGG16_imagenet", "shape": (224, 224, 3),
			"pretrained": True}


def model_sinpesos(img_width, img_height, num_classes, x_all=None, y_all=None,
				   optimizer=None):
	base_model = VGG16(weights=None, include_top=False,
					   input_shape=(img_height, img_width, 3))

	x = base_model.output
	x = Flatten(name='flatten')(x)
	x = Dense(4096, activation='relu', name='fc1')(x)
	x = Dense(4096, activation='relu', name='fc2')(x)

	predictions = Dense(1, activation='sigmoid')(x) if num_classes == 2 \
		else Dense(num_classes, activation='softmax')(x)

	# this is the model we will train
	model = Model(inputs=base_model.input, outputs=predictions)

	return model, base_model


def VGG16_sinpesos():
	return {"model": model_sinpesos, "name": "VGG16_sinpesos", "shape": (224, 224, 3)}


def model_imagenet_transfer(img_width, img_height, num_classes, x_all=None, y_all=None,
							optimizer=None):
	base_model = VGG16(weights='imagenet', include_top=False,
					   input_shape=(img_height, img_width, 3))

	x = base_model.output
	x = Flatten(name='flatten')(x)
	x = Dense(4096, activation='relu', name='fc1')(x)
	x = Dense(4096, activation='relu', name='fc2')(x)

	predictions = Dense(1, activation='sigmoid')(x) if num_classes == 2 \
		else Dense(num_classes, activation='softmax')(x)

	# this is the model we will train
	model = Model(inputs=base_model.input, outputs=predictions)

	return model, base_model


def VGG16_transfer():
	return {"model": model_imagenet_transfer, "name": "VGG16_transfer", "shape": (224, 224, 3),
			"transfer": True}
