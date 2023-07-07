# Function with output
def format_name(f_name, l_name):
    # here i am using title case which end up giving capital in first letter of each word
    first_name = f_name.title()   
    last_name = l_name.title()
    full_name = first_name + last_name
    return full_name
result = format_name("SUDIP", " praDhan")
print(result)