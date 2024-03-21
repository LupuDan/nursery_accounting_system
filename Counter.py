class Counter:
    def __init__(self):
        self.value = 0

    def add(self):
        self.value += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.value != 0:
            raise RuntimeError("Counter object was not properly closed.")

if __name__ == "__main__":
    try:
        with Counter() as counter:
            # Perform operations here
            counter.add()
            print("Current counter value:", counter.value)
    except RuntimeError as e:
        print("Error:", e)