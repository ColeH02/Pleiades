import os
import tangram
import math
from skyfield.api import Topos, Loader, EarthSatellite
from skyfield.positionlib import position_of_radec
from skyfield.api import load, wgs84

from main.PleiadesTracker import get_pleiades_pos, final_val, point_arr, point_to_str, earth, ra_hours, dec_degrees


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
		'preference': 'exclusively female'
	}

	# Make the prediction!
	output = model.predict(input)

	# Print the output.
	print('Full Output:', output)
	classification = getattr(output, 'class_name')
	probability = getattr(output, 'probability')
	print('classification:', classification)
	print('probability:', probability)

	point = get_pleiades_pos(earth, ra_hours, dec_degrees)
	print(point)
	pleiades_location = final_val(point_arr(point_to_str(point)))
	print(pleiades_location)

	universe_freq = 0.432;

	ALQ = probability * pleiades_location / universe_freq * 12
	print('ALQ:', ALQ)


if __name__ == "__main__":
	main()