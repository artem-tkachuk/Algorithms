def quickselect(array, k):
    start, end = 0, len(array)
    
    assert end >= 1 and 0 < k <= end, "Incorrect arguments"

    while True:
        pos = k - 1
        pivot = getPrice(array[start])  # arbitrary choice

        left, right = start + 1, end - 1

        # partially sort the array
        while (left <= right):
            if getPrice(array[left]) > pivot and getPrice(array[right]) < pivot:
                swap(array, left, right)
                
            if getPrice(array[left]) <= pivot:
                left += 1
        
            if getPrice(array[right]) >= pivot:
                right -= 1

        # put the pivot in the correct position
        swap(array, start, right)

        # determine how to proceed
        if right == start + pos:
            return array[right]
        elif right > start + pos:
            end = right
        else:  # right < start + pos
            k -= (left - start)
            start = left



def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def getPrice(item):
    return item[1]


def getItems(entries):
    products, outputs = [], []
    k = 0
    
    for entry in entries:
        # It is guaranteed that at least one item is added to the database before user views for the first time
        if entry[0] == "VIEW":
            # Increment to respect the k-th item property
            k += 1
            # Calculate the current k-th smallest given the current inserts so far
            current_k_th_smallest = quickselect(products, k)
            # Append the current k-th smallest to the array of outputs
            outputs.append(current_k_th_smallest)

        else:  # entry[0] == "INSERT"
            itemname, price = entry[2], int(entry[1])
            products.append((itemname, price))
            
    # return all the results for running VIEW
    return outputs


def main():
     entries = [
                ('INSERT', '1', 'cola'), 
                ('INSERT', '3', 'croissant'), 
                ('VIEW', '', ''), 
                ('INSERT', '7', 'pizza'), 
                ('VIEW', '', ''), 
                ('INSERT', '-1', 'kick'), 
                ('VIEW', '', '')
            ]
     print(getItems(entries))

main()
    
