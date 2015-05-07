math = [
    {
        "name": "Algebra 1",
        "prerequisites": []
    },
    {
        "name": "Geometry",
        "prerequisites": []
    },
    {
        "name": "Algebra 2",
        "prerequisites": ["Algebra 1", "Geometry"]
    },
    {
        "name": "Pre Calculus",
        "prerequisites": ["Algebra 2"]
    }
]

physics = [
    {
        "name": "Calculus",
        "prerequisites": []
    },
    {
        "name": "Scientific Thinking",
        "prerequisites": []
    },
    {
        "name": "Differential Equations",
        "prerequisites": ["Calculus"]
    },
    {
        "name": "Intro to Physics",
        "prerequisites": ["Scientific Thinking"]
    },
    {
        "name": "Relativity",
        "prerequisites": ["Differential Equations", "Intro to Physics"]
    }
]


bad = [
     {
        'name': 'S1',
        'prerequisites': []
      },
     {
        'name': 'S2',
        'prerequisites': []
      },
     {
        'name': 'S3',
        'prerequisites': []
      },
     {
        'name': 'S4',
        'prerequisites': []
      },
     {
        'name': 'S5',
        'prerequisites': []
      },
     {
        'name': 'S6',
        'prerequisites': ['S1', 'S2', 'S3', 'S4', 'S5', 'S7', 'S8']
      },
     ]

good = [
     {
        'name': 'S1',
        'prerequisites': []
      },
     {
        'name': 'S2',
        'prerequisites': []
      },
     {
        'name': 'S3',
        'prerequisites': []
      },
     {
        'name': 'S4',
        'prerequisites': []
      },
     {
        'name': 'S5',
        'prerequisites': []
      },
     {
        'name': 'S6',
        'prerequisites': ['S1', 'S2', 'S3', 'S4', 'S5']
      },
     ]

empty_test = [
              {},
              {}
    ]
def scheduler(classes):
    # Make sure we have data...
    if all(not d for d in classes):
        print "Error: No data contained in file"
        return
    
    taken = {}
    priority = []

    possible_classes = [item.get('name') for item in classes]
    
    # Sanity check, make sure all prerequisites are actually valid classes
    for item in classes:
        prerequisites = item.get('prerequisites')
        if prerequisites and not set(prerequisites).issubset(set(possible_classes)):
            print "Error: prerequisite(s)", ", ".join(list(set(prerequisites) - set(possible_classes))), "are not valid classes."
            return
    
    for item in classes:
        name = item.get('name')
        prerequisites = item.get('prerequisites')
        if name is None or prerequisites is None or name in taken:
            continue
        # Now check to see if any pre-reqs
        if len(prerequisites) > 0:
            # then we have pre-reqs and need to see if we have taken them
            missing = missing_prerequisites(prerequisites, taken)
            if len(missing) == 0:
                #then all pre-missing are satisfied, we can add it to the taken classes
                print name
                taken[name] = True
            else:
                # Store for checking later
                priority.append(item)
        else:   
            taken[name] = True
            print name
    
    while len(priority) > 0:
        item = priority.pop()
        name = item.get('name')
        prerequisites = item.get('prerequisites')
        missing = missing_prerequisites(prerequisites, taken)
        if len(missing) == 0:
            #then all pre-reqs are satisfied, we can add it to the taken classes
            print name
            taken[name] = True
        else:
            # Store for checking later
            priority.insert(0, item)

def missing_prerequisites(prerequisites, taken):
    return set(prerequisites) - set(taken.keys())


def build_test_list():
    big_relation = []
    end_list = []
    for i in range(0, 999999):
        tmp_dict = {}
        name = 'S' + str(i)
        tmp_dict['name'] = name
        tmp_dict['prerequisites'] = []
        big_relation.append(name)
        end_list.append(tmp_dict)
    
    final_dict = {}
    final_dict['name'] = 'S1000000'
    final_dict['prerequisites'] =  big_relation
    end_list.append(final_dict)
    #print end_list[-1]
        
        
    return end_list

scheduler(empty_test)

from random import shuffle
import time
test_list = build_test_list()
start = time.time()
shuffle(test_list)
scheduler(test_list)
end = time.time()
print end - start


