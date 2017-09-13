from die import Die
import pygal

die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(100):
    results.append(die_1.roll() + die_2.roll())


frequencies = []

max_result = die_1.num_slides + die_2.num_slides

for value in range(2,die_1.num_slides+ die_2.num_slides):
    frequencies.append(results.count(value))


hist = pygal.Bar()

hist.title = "Results of rolling two D6 1.000 times"
hist.x_labels = ['1','2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add("D6 + D6",frequencies)
hist.render_to_file('dice_visual.svg')
