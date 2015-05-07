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

def scheduler(classes):

    queue = classes
    visited = {}
    
    if all(not d for d in classes):
        print "Error: No data contained in file"
        return

    possible_classes = [item.get('name') for item in classes]
    
    # Sanity check, make sure all prerequisites are actually valid classes
    
    for item in classes:
        prerequisites = item.get('prerequisites')
        if prerequisites and not set(prerequisites).issubset(set(possible_classes)):
            print "Error: prerequisite(s)", ", ".join(list(set(prerequisites) - set(possible_classes))), "are not valid classes."
            return
    
    while len(queue) > 0:
        item = queue.pop()
        f = []
        name = item.get('name')
        prerequisites = item.get('prerequisites')
        if len(prerequisites) > 0:
            all_satisfied = True
            for req in prerequisites:
                if req not in visited:
                    all_satisfied = False
            if all_satisfied:
                print name
                visited[name] = True
            else:
                #enque 
                queue.insert(0, item)
                
        else:
            print name
            visited[name] = True

def build_test_list():
    big_relation = []
    end_list = []
    n = 999999
    for i in xrange(0, n):
        tmp_dict = {}
        name = 'S' + str(i)
        tmp_dict['name'] = name
        tmp_dict['prerequisites'] = []
        big_relation.append(name)
        end_list.append(tmp_dict)
    
    final_dict = {}
    final_dict['name'] = 'S' + str(n+1)
    final_dict['prerequisites'] =  big_relation
    end_list.append(final_dict)
    
    return end_list
    
from random import shuffle
import time
#test_list = build_test_list()
#shuffle(test_list)
start = time.time()
shuffle(physics)
scheduler(physics)
end = time.time()
print end - start