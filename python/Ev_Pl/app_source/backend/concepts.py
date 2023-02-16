# Objects to represent Events, Tasks, Reminders and Notes

# ___________________________ Classes

class Event(object):

    def __init__(self, desc_value_set, para_value_set):
        self.event_name = desc_value_set['name']
        self.event_desc = desc_value_set['desc']
        self.event_date = para_value_set['date']
        self.event_visibility = para_value_set['visibility']
        self.task_bool = True if para_value_set['task'] == 'yes' else False


class Task(object):

    PRIORITIES = {'high': 0, 'mid': 1, 'low': 2}
    PRIORITIES_REVERSE_DICT = {value: key for key, value in PRIORITIES.items()}

    def __init__(self, desc_value_set, para_value_set):
        self.task_name = desc_value_set['name']
        self.task_desc = desc_value_set['desc']
        self.date = para_value_set['date']
        self.start = para_value_set['start']
        self.end = para_value_set['end']
        self.priority = self.PRIORITIES[para_value_set['priority']]
        self.repeat = True if para_value_set['repeat'] == 'yes' else False

    @classmethod
    def from_event_values(cls, event_desc_value_set, event_para_value_set):
        event_para_value_set['start'] = '00:00:00'
        event_para_value_set['end'] = '23:59:00'
        event_para_value_set['priority'] = 'low'
        event_para_value_set['repeat'] = 'no'
        return cls(event_desc_value_set, event_para_value_set)

    @classmethod
    def from_tuple(cls, value_tuple):
        desc_value_set = {'name': value_tuple[2], 'desc': value_tuple[3]}
        para_value_set = {
            'date': value_tuple[4], 'repeat': value_tuple[5], 'start': value_tuple[6],
            'end': value_tuple[7], 'priority': Task.PRIORITIES_REVERSE_DICT[value_tuple[8]]
        }
        return cls(desc_value_set, para_value_set)

# ___________________________
