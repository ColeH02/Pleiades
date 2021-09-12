import os
import tangram
import math
from PleiadesTracker import get_pleiades_pos, final_val, point_arr, point_to_str, earth, ra_hours, dec_degrees

def run_through_model(input):
    # Get the path to the .tangram file.
    model_path = os.path.join(os.path.dirname(__file__), 'hackdata3.tangram')
    # Load the model from the path.
    model = tangram.Model.from_path(model_path)

    # Make the prediction!
    output = model.predict(input)

    # Print the output.
    classification = getattr(output, 'class_name')
    confidence = getattr(output, 'probability')

    if classification == 'not at all':
        class_val = 0.1
    elif classification == '2-3 times a month':
        class_val = 0.25
    elif classification == 'weekly':
        class_val = 0.5
    elif classification == '2-3 per week':
        class_val = 0.75

    print('confidence:', confidence)
    print('class_val:', class_val)

    point = get_pleiades_pos(earth, ra_hours, dec_degrees)
    print(point)
    pleiades_location = final_val(point_arr(point_to_str(point)))
    print('pleiades_location:', pleiades_location)

    universe_freq = 0.432;
    zodiac_symbols = 12;
    pleiades_star_count = 800;

    ALQ = (abs(math.sin((((math.pow(confidence, class_val)) * pleiades_location) / (
                universe_freq / zodiac_symbols)) * pleiades_star_count))) * 100;
    print('ALQ:', ALQ)


def get_inputs():
    inputs = {}
    print("Hello, please answer these questions:")
    input[""]

if __name__ == "__main__":
    main()