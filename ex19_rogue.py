def ip_address(first,second,third,fourth):
   print(f"{first}.{second}.{third}.{fourth}")
   print(f"Network Summary: {first}.{second}.{third}.0 /24")
   print(f"Gateway: {first}.{second}.{third}.254")

print("Manual Submission")
ip_address("192", "168", "100", "15")

print("Four different prompts")
ip_address(input(int), input(int), input(int), input(int))

print("single prompt to parse out")
ip_address(input())
