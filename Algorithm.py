# Author: Austin Thompson
# File: Algorithm.py
# Date: 4/23/2020
    # 5/5/2020: Added comments


from abc import ABC, abstractmethod
import random
import time


#Algorithm class interface
class AlgorithmInterface(ABC):
    @abstractmethod
    def __init__(self, name, size, min_value, max_value, data):
        pass
    
    @abstractmethod
    def generate_random_array(self):
        pass
    
    @abstractmethod
    def animate_bubble(self, canvas, draw, speed):
        pass
    
    @abstractmethod
    def animate_insertion(self, canvas, draw, speed):
        pass
    
    @abstractmethod
    def animate_quick(self, canvas, draw, speed, head, tail):
        pass
    
    @abstractmethod
    def partition(canvas, draw, speed, head, tail):
        pass
    
    @abstractmethod
    def color_array(length, low, high, index, swapping = False):
        pass
    

# Algorithm class to handle non-GUI sorting activities
class Algorithm(AlgorithmInterface):
    # Initializer - Constructor
    def __init__(self, name, size, min_value, max_value, data):
        self.name = name
        self.size = size
        self.min_value = min_value
        self.max_value = max_value
        self.data = data
        
    # Generate random array method
    def generate_random_array(self):
        
        # Clear data every time method is called
        self.data = []
        x = 0
        
        # Keep appending items to the array for the objects given size
        while x < self.size:
            
            # Generate a random number between the min and max values of the object
            self.data.append(random.randrange(self.min_value, self.max_value + 1))
            x += 1
            
        # Return the randomly generated array
        return self.data
        
        
    # Animation for bubble sort - swap adjacent elements if they are unsorted
    def animate_bubble(self, canvas, draw, speed):
        # Iterate of the entire array
        for x in range (len(self.data)-1):
            
            for j in range (len(self.data)-1):
                
                # If index j is greater than j+1 then swap
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    
                    # If x is equal to j or j+1 then change their color to signal they are being swapped
                    # Call the draw method from GUI Driver to visualize the sorting algorithm and wait the object's set time
                    draw(self, canvas, ['green' if x == j or x == j+1 else 'orange' for x in range(len(self.data))] )
                    time.sleep(float(speed.get()))
        draw(self, canvas, ['green' for x in range(len(self.data))])
        
        
    
    # Animate insertion sort
    def animate_insertion(self, canvas, draw, speed):
        for index in range(1, len(self.data)):
            
            # Find the next value to be sorted
            value = self.data[index]
            i = index - 1
            
            # Draw the array and wait to help visualize
            draw(self, canvas, ['orange' if i<index else 'red' if self.data[i] == value else 'white' for i in range(len(self.data))] )
            time.sleep(float(speed.get()))
            
            # Locate the position for the value to be inserted and swap them
            while i >= 0 and value < self.data[i]:
                self.data[i+1] = self.data[i]
                i = i - 1
            
            # Update the key value
            self.data[i+1] = value
            
            # Draw the updated array
            draw(self, canvas, ['orange' if i<index else 'red' if self.data[i] == value else 'white' for i in range(len(self.data))] )
            time.sleep(float(speed.get()))
            
        # Once sorting is completed, make all items the same color
        draw(self, canvas, ['orange' for i in range(len(self.data))] )
        time.sleep(float(speed.get()))
        
        
        
    
    # Animate quick sort
    def animate_quick(self, canvas, draw, speed, head, tail):
        
        if head < tail:
            index_partition = self.partition(canvas, draw, speed, head, tail)
            
            # Left partition
            self.animate_quick(canvas, draw, speed, head, index_partition-1)
            
            # Right partition
            self.animate_quick(canvas, draw, speed, index_partition+1, tail)
            
            # Make all items white once completed sorted
            draw(self, canvas, ['white' for x in range(len(self.data))])
        
    
    # Partition for quick sort
    def partition(self, canvas, draw, speed, head, tail):
        
        # Create edge of partition and pivot values for sorting
        edge = head
        pivot = self.data[tail]
        
        # Draw the values and wait
        draw(self, canvas, self.color_array(len(self.data), head, tail, edge, edge))
        time.sleep(float(speed.get()))
        
        # Iterate over the array
        for j in range(head, tail):
            
            # If current index is less than the pivot swap
            if self.data[j] < pivot:
                
                # Draw before swap
                draw(self, canvas, self.color_array(len(self.data), head, tail, edge, j, True))
                time.sleep(float(speed.get()))
                
                # Swap and update the edge of the partition
                self.data[edge], self.data[j] = self.data[j], self.data[edge]
                edge += 1
            
            # Draw after the swap
            draw(self, canvas, self.color_array(len(self.data), head, tail, edge, tail, True))
            time.sleep(float(speed.get()))
                
        # Draw all in one color once complete
        draw(self, canvas, self.color_array(len(self.data), head, tail, edge, tail, True))
        time.sleep(float(speed.get()))
        
        # Swap edge and tail values before returning the new partion
        self.data[edge], self.data[tail] = self.data[tail], self.data[edge]
        return edge
    
    
    # Color array method for quick sort - this creates the returned array for the draw method
        # Abstracted from partition method to simplify system functionality
    def color_array(self, length, head, tail, partition, index, swapping = False):
        
        # Create an empty color array to make displaying algorithm easier
        array = []
        
        
        # Check to see what each value in the array is and assign it a color based on
            # the quick sort's current point in sorting
        for z in range(length):
            # Set the borders to grey
            if z >= head and z <= tail:
                array.append('grey')
            else:
                array.append('white')
                
            if z == tail:
                array[z] = 'blue'
            elif z == partition:
                array[z] = 'red'
            
            if swapping:
                if z == partition or z == index:
                    array[z] = 'green'
                    
        return array
    