                                                                                                ; Insertion sort algorithm
                                                                                                ; Due to inexperience, the array to be sorted will be hardcoded
[ org 0x7c00 ]

ASSIGN_ARRAY:           LIST                    db                      34,21,11,1,25           ; First off, probably should assign an array

INSERTION_SORT:
                                                                                                ; Do from the second element (index 1) onwards
                                                                                                ; call the current element 'key'
                                                                                                ; loop through the array, from the element just before 'key', so long as its index > 1
                                                                                                ; reverse the order of elements
                                                                                                ; decrement index
                                                                                                ; Set the last element to 'key'
