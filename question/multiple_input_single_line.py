def test_input(n, h):
    print(f"This is n: {n} \nAnd this is h: {h}")


# This is how to input
n, h = map(int, input().split())
test_input(n, h)

n = int(input("Enter the number of elements: "))  # Input the number of elements
elements = list(map(int, input("Enter the elements: ").split()))  # Input the elements and convert to a list of integers

output_string = "[" + ", ".join(map(str, elements)) + "]"  # Create the formatted output string
print("Output:", output_string)