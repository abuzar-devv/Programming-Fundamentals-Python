# # #----------------- *args------------------
# # #------- “Take all extra arguments and pack them into a tuple”-----------
# # #---------We can add * with only 1 arg in a function-----------
# # #----------To take multiple entries for a argument enter a * before it-----------


# # # def info(name,*marks):
# # #     print(name)
# # #     print(marks)

# # # info("abuzar",1,2,3,4,5,6,7,8)


# # #----Default arg case------

# # def scores(name="abuzar",*marks):

# #     total=0
# #     for i in marks:
# #         total+=i

# #     print(f"{name} has got total score of {total}")

# # scores(marks=(12,3,4,12,54,23,61,24,54,23))









# #--------Gemini practice------------

# #Level 1: Easy
# # Ticket 1: The IoT Sensor Aggregator
# # Business Requirement:
# # We have a server room hooked up to a variable number of thermal sensors. Sometimes 2 sensors are active, sometimes 50 are active.
# # Build a Pure Function that accepts an infinite number of temperature readings (floats). The function must calculate and return the exact average temperature of the room.
# # Architect's Constraint: If the power goes out and zero sensor readings are passed into the function, 
# # it must return 0.0 to prevent the system from crashing via a "Division by Zero" error.

# def avg_temp(*temperature: float) -> float:
#     if len(temperature) == 0:
#         return 0.0
    
#     return sum(temperature) / len(temperature)


# print(f"Average temperature of sensor room is: {avg_temp(22,34,99.4,33.2):.2f}")





# #Ticket 2: The Network Pinger
# # Business Requirement:
# # The DevOps team needs a tool to ping IP addresses.
# # Build a Pure Function that accepts a timeout limit in milliseconds, followed by an infinite number of IP address strings.
# # Most of our servers respond quickly, so the timeout limit must have a default backup of 300 milliseconds.
# # The function must return a single formatted string that says exactly this:
# # "Pinging [count] servers with a [timeout]ms timeout." (e.g., "Pinging 4 servers with a 300ms timeout.").
# # Architect's Constraint: You must structure your parameters perfectly so the compiler does not throw a Syntax Error.


# def network_pinger(timeout=300,*ip_adresses:str) -> str:
#     return f"Pinging {len(ip_adresses)} servers with a {timeout} ms timeout"


# print(network_pinger(350,"192.168.1","198.45.2.1","192.345.1"))





# def average(*scores:float) -> float:
#     if not scores:
#         return 0.0

#     return ((sum(scores))/len(scores))

# print(f"Average is {average()}")




# def data(num,*args):
#     print(args)
#     print(num)


# data(2,"ali",1,2,0.5)












































































