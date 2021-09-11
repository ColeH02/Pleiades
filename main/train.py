import os
import tangram

def main():

	# Get the path to the .tangram file.
	model_path = os.path.join(os.path.dirname(__file__), 'hackdata2.tangram')
	# Load the model from the path.
	model = tangram.Model.from_path(model_path)

	# Create an example input matching the schema of the CSV file the model was trained on.
	# Here the data is just hard-coded, but in your application you will probably get this
	# from a database or user input.
	input = {
		'sex': 'female',
		'zodiac': 'cancer',
		'sexsex5': 'exclusively female'
	}

	# Make the prediction!
	output = model.predict(input)

	# Print the output.
	print('Full Output:', output)
	classification = getattr(output, 'class_name')
	probability = getattr(output, 'probability')
	print('classification:', classification)
	print('probability:', probability)


if __name__ == "__main__":
	main()