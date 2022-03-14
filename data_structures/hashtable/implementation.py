# Hashtable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Max Halpern



class HashTable:

    def __init__(self, size=20):
        """
        Initalize the setup of the HashTable Class.

        params size Int, the size of the hashtable.
        """
        self.size = size
        self.data = [[] for x in range(self.size)]

    def hash(self, index)-> int:
        """
        Turn a key into an int so it may be placed
        insde the hash map.

        params index The key to be turned into an int.
        returns Int a valid index to send the data into the proper
        location.
        """
        return hash(index) % self.size



    def __setitem__(self, key, value):
        """
        Set a value and key at a given index.

        params key The key associated to the value.
               value The value to be inserted.
        """
        hashed = self.hash(key)
        bucket = [key,value]
        
        if len(self.data[hashed]) == 0 or self.data[hashed][0][0] == key:
            self.data[hashed] = [bucket]
        else:
            self.data[hashed].append(bucket)
    

    
    def __getitem__(self, index):
        """
        Make this class iterable by giving it
        a __getitem__ method.

        params index Int the index of the key value pair.
        """
        
        hashed = self.hash(index)
        if len(self.data[hashed]) == 0:
            return None
        elif len(self.data[hashed]) == 1:
            for items in self.data[hashed]:
                return items[1]
        else:
            return self.data[hashed]

    
    def delete(self, key)-> None:
        """
        Delete the value and key associated with that value.

        params key The key to be searched for, then that and 
        the value will be deleted by becoming an empty list.

        returns None.
        """
        hashed = self.hash(key)
        self.data[hashed] = []
        return None
        
    def clear(self)-> None:
        """
        Clear the entire hash map so it only contains empty lists.

        reutrns None.
        """
        for elements in range(len(self.data)):
            if len(self.data[elements]) > 1:
                for items in self.data[elements]:
                    self.data[elements] = []
            else:
                self.data[elements] = []

        return None


    def keys(self)-> list:
        """
        Iterate through each index and capture the key.

        returns list The list of keys.
        """   
        key_list = []
        for bucket in self.data:            
            if len(bucket) > 0:
                for key in bucket:
                    key_list.append(key[0])           
        
        return key_list

    def values(self)-> list:
        """
        Iterate through each index and capture the value.

        returns list The list of values.
        """   
        value_list = []
        for bucket in self.data:
            if len(bucket) > 0:
                for value in bucket:
                    value_list.append(value[1])
                     
        return value_list

    def has_value(self, value)-> bool:
        """
        Checks the values for the given value.

        params value The value to be searched for.

        returns Bool True if found False if not.
        """
        values = self.values()
        if value in values:
            return True
        else:
            return False
    

    def has_key(self, key)-> bool:
        """
        Checks the keys for the given key.

        params key The key to be searched for.

        returns Bool True if found False if not.
        """
        keys = self.keys()
        if key in keys:
            return True
        else:
            return False

    def items(self)-> list:
        """
        Iterate through the entire structure and return
        a list of key and values from the hashtable.

        returns List of all keys and values.
        """
        item_list = []
        for bucket in self.data:
            if len(bucket) > 0:
                for item in bucket:
                    appended_item = [item[0],item[1]]
                    item_list.append(appended_item)        
        return item_list

    


    def __str__(self)-> str:
        """
        Display the Hashmap and all of its values.

        returns str Hashmap of key value pairs.
        
        """
       
        return "".join(str(x) for x in self.data)
 