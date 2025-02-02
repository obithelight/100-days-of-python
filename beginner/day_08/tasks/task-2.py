'''
Create a function with multiple inputs.
'''
def greet_with_name(name: str, location: str) -> str:
    print(f"Hello {name}, how is {location} today?")

greet_with_name(location="London", name="Johnson")
