name = input("Enter your name agent " )
gadget = input("Enter your favourite gadget " )

agent_num = 8
speed_Rate = 8.12
mission_count = 12
height = 1.48
is_active= True

print("type of name = ", type(name))

print("type of speed rate = ", type(speed_Rate))

print("type of misson count = ", type(mission_count ))

print("type of height = ", type(height))

print("type of is active = ", type(is_active))

agent_num_text = str(agent_num)
mission_count_text = str(mission_count)
is_active_text = str(is_active)
speed_rate_text = str(speed_Rate)

print("type of speed rate = ", type(speed_rate_text))

print("type of misson count = ", type(mission_count_text ))

print("type of agent number = ", type(agent_num_text))

print("type of is active = ", type(is_active_text))

first_name = name[0:3]
last_name = name[-1]
code_name = first_name + last_name
print(first_name)
print(last_name)
print(code_name)

print(gadget[::-1])