from flask import Flask, render_template, request, session

app = Flask(__name__)

def merge_sort(vector):
    length = len(list(vector))
    if length > 1:
        mid = length // 2
        left_vector = vector[:mid]
        right_vector = vector[mid:]

        
        merge_sort(left_vector)
        merge_sort(right_vector)

        merge(vector, left_vector, right_vector)

    return vector


def merge(vector, left_vector, right_vector):
    i = 0  # left_vector idx
    j = 0  # right_vector idx
    k = 0  # merged vector idx
    while i < len(left_vector) and j < len(right_vector):
        if left_vector[i] <= right_vector[j]:
            vector[k] = left_vector[i]
            i += 1
        else:
            vector[k] = right_vector[j]
            j += 1
        k += 1

    while i < len(left_vector):
        vector[k] = left_vector[i]
        i += 1
        k += 1

    while j < len(right_vector):
        vector[k] = right_vector[j]
        j += 1
        k += 1


@app.route('/', methods=['GET', 'POST'])

def index():
    ordered_value = None
    input_values =''

    if request.method == 'POST':
        input_values = request.form['values']
        my_vector = list(input_values.strip().lower().replace(" ", "")) 
        merge_sort(my_vector)
        ordered_value = "".join(my_vector)


    return render_template('index.html', ordered_value=ordered_value, input_values = input_values)

if __name__ == '__main__':
    app.run(debug=True)