"""
CSP Specification for Figure 4
"""
csp = {
'variables' : {
    'C11' : [1],
    'C12' : [1, 2, 3, 4],
    'C13' : [1, 2, 3, 4],
    'C14' : [1, 2, 3, 4],
    'C21' : [1, 2, 3, 4],
    'C22' : [2],
    'C23' : [1, 2, 3, 4],
    'C24' : [1, 2, 3, 4],
    'C31' : [1, 2, 3, 4],
    'C32' : [1, 2, 3, 4],
    'C33' : [3],
    'C34' : [1, 2, 3, 4],
    'C41' : [1, 2, 3, 4],
    'C42' : [1, 2, 3, 4],
    'C43' : [1, 2, 3, 4],
    'C44' : [4]
}
,
'constraints' : {
# First Row
    # C11
    ('C11', 'C12'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C11', 'C13'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C11', 'C14'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C11', 'C21'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C11', 'C31'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C11', 'C41'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C11', 'C22'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    # C12
    ('C12', 'C13'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C12', 'C14'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C12', 'C21'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C12', 'C22'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C12', 'C32'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C12', 'C42'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    # C13
    ('C13', 'C14'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C13', 'C23'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C13', 'C33'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C13', 'C43'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C13', 'C24'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    # C14
    ('C14', 'C24'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C14', 'C34'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C14', 'C44'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C14', 'C23'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
# Second Row
    # C21
    ('C21', 'C22'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C21', 'C23'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C21', 'C24'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C21', 'C31'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C21', 'C41'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    # C22
    ('C22', 'C23'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C22', 'C24'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C22', 'C32'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C22', 'C42'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    # C23
    ('C23', 'C24'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C23', 'C33'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C23', 'C43'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    # C24
    ('C24', 'C34'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C24', 'C44'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
# Third Row
    # C31
    ('C31', 'C32'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C31', 'C33'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C31', 'C34'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C31', 'C41'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C31', 'C42'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    # C32
    ('C32', 'C33'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C32', 'C34'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C32', 'C41'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C32', 'C42'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    # C33
    ('C33', 'C34'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C33', 'C43'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C33', 'C44'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    # C34
    ('C34', 'C43'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C34', 'C44'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
# Fourth Row
    # C41
    ('C41', 'C42'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C41', 'C43'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C41', 'C44'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    # C42
    ('C42', 'C43'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    ('C42', 'C44'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)],
    # C43
    ('C43', 'C44'): [(1, 2), (1, 3), (1, 4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)]
    # C44
}
}