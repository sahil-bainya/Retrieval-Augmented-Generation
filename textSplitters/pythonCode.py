from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text="""
class Car:
    # Constructor: initializes attributes for each new instance
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    # Method to start the car
    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.year} {self.make} {self.model}'s engine is now running.")
        else:
            print("The engine is already running.")

    # Method to stop the car
    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.year} {self.make} {self.model}'s engine is shut off.")
        else:
            print("The engine is already off.")

    # Method to display car info
    def display_info(self):
        status = "running" if self.is_running else "stopped"
        print(f"{self.year} {self.make} {self.model} (Status: {status})")


# --- Object Creation and Usage ---

# Instantiating two distinct objects from the Car class
car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Tesla", "Model 3", 2024)

# Accessing attributes and calling methods on car1
car1.display_info()
car1.start_engine()
car1.display_info()

print()

# Accessing attributes and calling methods on car2
car2.display_info()
car2.stop_engine()
"""
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0,
)

chunks = splitter.split_text(text)
print(len(chunks))
for chunk in chunks:
    print(chunk)
    print('------')