# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#part 1

scorer_1 = "Ruud Gullit"
scorer_2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = scorer_1 + " " + str(goal_0) + ", " + scorer_2 + " " + str(goal_1)
print(scorers)
report = ( f"{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute" )
print(report)

#part 2

player = "Ruud Gullit"
first_name = player[0:player.find(" ")]
print(first_name)
player.find("Gullit")
last_name_len = len("Gullit")
print(last_name_len)
name_short = first_name[0] + ". " + player[len("Gullit")-1:]
print(name_short)
first_name = player[0:len("Ruud")]
first_name
chant = (first_name + "! ")* 3 + (first_name + "!")
print(chant)
good_chant = (first_name + "! ")* 3 + (first_name + "!") != (first_name + "! ")* 4
print((first_name + "! ")* 3 + (first_name + "!") != (first_name + "! ")* 4 )
print((first_name + "! ")* 4 != (first_name + "! ")* 4 )