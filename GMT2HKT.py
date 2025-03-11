from datetime import datetime
import pytz

# Define the time zones
gmt = pytz.timezone('GMT')
hkt = pytz.timezone('Asia/Hong_Kong')

# Function to convert GMT to HKT
def convert_gmt_to_hkt(gmt_input):
    # Parse the input date string (format 'DD MMM HHMM')
    gmt_time = datetime.strptime(gmt_input, '%d %b %H%M')
    
    # Set the current year (assuming the input doesn't specify a year)
    gmt_time = gmt_time.replace(year=datetime.now().year)
    
    # Localize the time to GMT
    gmt_time = gmt.localize(gmt_time)
    
    # Convert to HKT
    hkt_time = gmt_time.astimezone(hkt)
    
    # Return the converted time in HKT (formatted to 'DD MMM YYYY HHMM')
    return hkt_time.strftime('%d %b %Y %H%M')

# Input
gmt_input = input("Enter the date and time in GMT (e.g., '30 Oct 1800'): ")

# Convert and print the output
hkt_output = convert_gmt_to_hkt(gmt_input)
print("The corresponding time in HKT is:", hkt_output)