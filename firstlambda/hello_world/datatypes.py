def simple_types(event, context):
    print(event)
    return event


def list_types(event, context):
    print(event)
    student_scores = {"anand": 100, "neha": 89, "guddi": 99}
    scores = []
    for name in event:
        scores.append(student_scores[name])
    return scores


def dict_types(event, context):
    print(event)
    print(event["anand"])
    return event
