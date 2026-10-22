
def structure_to_dictionary(fields, values):
    if len(fields) != len(values):
        raise ValueError("Fields and values must have the same length.")

    return dict(zip(fields, values))


if __name__ == "__main__":
    fields = ["name", "age", "course"]
    values = ["Anupriya", 20, "B.Tech"]

    student = structure_to_dictionary(fields, values)
    print(student)
