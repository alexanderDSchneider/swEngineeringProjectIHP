# Author: Austin Thompson
# File: Algorithm.py
# Date: 4/23/2020


from abc import ABC, abstractmethod
import random
import time

class AlgorithmInterface(ABC):
    @abstractmethod
    def __init__(self, name, size, min_value, max_value, data):
        pass
    
    @abstractmethod
    def display(self):
        pass
        
    @abstractmethod
    def pause(self):
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
    


class Algorithm(AlgorithmInterface):
    def __init__(self, name, size, min_value, max_value, data):
        self.name = name
        self.size = size
        self.min_value = min_value
        self.max_value = max_value
        self.data = data
        
    def display(self):
        print("display")
        
    def pause(self):
        print("pause")
        
    def generate_random_array(self):
        #clear the attribute
        self.data = []
        x = 0
        while x < self.size:
            self.data.append(random.randrange(self.min_value, self.max_value + 1))
            x += 1
        return self.data
        
        
    def animate_bubble(self, canvas, draw, speed):
        for x in range (len(self.data)-1):
            for j in range (len(self.data)-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    draw(self, canvas, ['green' if x == j or x == j+1 else 'orange' for x in range(len(self.data))] )
                    time.sleep(float(speed.get()))
        draw(self, canvas, ['green' for x in range(len(self.data))])
        
        
    def animate_insertion(self, canvas, draw, speed):
        for index in range(1, len(self.data)):
            # Find the next value to be sorted
            value = self.data[index]
            i = index - 1
            
            draw(self, canvas, ['orange' if i<index else 'red' if self.data[i] == value else 'white' for i in range(len(self.data))] )
            time.sleep(float(speed.get()))
            
            # Locate the position for the value to be inserted
            while i >= 0 and value < self.data[i]:
                self.data[i+1] = self.data[i]
                i = i - 1
            
            self.data[i+1] = value
            draw(self, canvas, ['orange' if i<index else 'red' if self.data[i] == value else 'white' for i in range(len(self.data))] )
            time.sleep(float(speed.get()))
            
            
        draw(self, canvas, ['orange' for i in range(len(self.data))] )
        time.sleep(float(speed.get()))
        
        
    def animate_quick(self, canvas, draw, speed, head, tail):
        
        if head < tail:
            index_partition = self.partition(canvas, draw, speed, head, tail)
            
            #left partition
            self.animate_quick(canvas, draw, speed, head, index_partition-1)
            #right partition
            self.animate_quick(canvas, draw, speed, index_partition+1, tail)
            
            draw(self, canvas, ['white' for x in range(len(self.data))])
        
        
    def partition(self, canvas, draw, speed, head, tail):
        border = head
        pivot = self.data[tail]
        
        draw(self, canvas, self.color_array(len(self.data), head, tail, border, border))
        time.sleep(float(speed.get()))
        
        for j in range(head, tail):
            if self.data[j] < pivot:
                draw(self, canvas, self.color_array(len(self.data), head, tail, border, j, True))
                time.sleep(float(speed.get()))
                
                self.data[border], self.data[j] = self.data[j], self.data[border]
                border += 1
            draw(self, canvas, self.color_array(len(self.data), head, tail, border, tail, True))
            time.sleep(float(speed.get()))
                
            
        draw(self, canvas, self.color_array(len(self.data), head, tail, border, tail, True))
        time.sleep(float(speed.get()))
        
        self.data[border], self.data[tail] = self.data[tail], self.data[border]
        return border
    
    
    def color_array(self, length, head, tail, border, index, swapping = False):
        
        # create an empty color array to make displaying algorithm easier
        array = []
        
        for z in range(length):
            if z >= head and z <= tail:
                array.append('gray')
            else:
                array.append('white')
                
            if z == tail:
                array[z] = 'blue'
            elif z == border:
                array[z] = 'red'
            elif z == index:
                array[z] = 'yellow'
            
            if swapping:
                if z == border or z == index:
                    array[z] = 'green'
                    
        return array
    
    
        
        
        
        
        
        