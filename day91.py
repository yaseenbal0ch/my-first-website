print("===== **kwargs EXAMPLE =====")

def student(**data):
    for key, value in data.items():
            print(key, ":", value)

            student(
                name="Yaseen",
                    age=20,
                        city="DG Khan",
                            country="Pakistan"
                            )